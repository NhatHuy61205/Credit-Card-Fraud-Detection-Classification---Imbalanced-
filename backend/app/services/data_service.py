import pandas as pd
import os
import joblib
from sklearn.preprocessing import StandardScaler
from utils import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
CSV_PATH = os.path.join(BASE_DIR, "data", "creditcard.csv")

df = pd.read_csv(CSV_PATH)
df = create_features(df)
df_sorted = df.sort_values("Time").reset_index(drop=True)
df = df_sorted.iloc[int(0.8 * len(df_sorted)):]
scaler = StandardScaler()
df[['_log_amount']] = scaler.fit_transform(df[['_log_amount']])
df['hour_sin'] = np.sin(2 * np.pi * df['Hour_from_start_mod24']/24)
df['hour_cos'] = np.cos(2 * np.pi * df['Hour_from_start_mod24']/24)
df['time_diff'] = df['Time'].diff().fillna(0)
threshold = df['Amount'].quantile(0.95)  
df['is_high_amount'] = (df['Amount'] > threshold).astype(int)
df['is_rapid_transaction'] = (df['time_diff'] < 60).astype(int)
temp = df.copy()
temp.drop(["Class","Amount","Time","Hour_from_start_mod24"], axis=1, inplace=True)

MODEL_PATH = Path(__file__).parent.parent.parent.parent / "artifacts" / "Random_Forest.joblib"
model = joblib.load(MODEL_PATH)

proba_all = model.predict_proba(temp)

df["fraud_proba"] = proba_all[:, 1] * 100

conditions = [
    (df["fraud_proba"] < 50),   
    (df["fraud_proba"] >= 90),                       
    (df["fraud_proba"] >= 50) & (df["fraud_proba"] < 90) 
]

choices = ["success", "early", "disputed"]

df["status"] = np.select(conditions, choices, default="success")

def get_data(skip=0, limit=1000):
    return df.iloc[skip:skip+limit].to_dict(orient="records")

def total():
    return len(df)

def amount_per_hour():
    df_grouped = df.groupby(["Hour_from_start_mod24", "status"])["Amount"].sum().reset_index()
    df_pivot = df_grouped.pivot(index="Hour_from_start_mod24", columns="status", values="Amount").fillna(0)

    return df_pivot.reset_index().to_dict(orient="records")

def amount_per_status():
    df_grouped = df.groupby("status")["Amount"].sum().reset_index()
    total_amount = df_grouped["Amount"].sum()
    df_grouped["percent"] = df_grouped["Amount"] / total_amount * 100
    df_grouped["bg"] = ["#f5b041","#ff7f0e", "#2e86de"]
    return df_grouped.to_dict(orient="records")

