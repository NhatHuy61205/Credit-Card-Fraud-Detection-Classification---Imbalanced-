from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, confusion_matrix
from pathlib import Path
import pandas as pd
import sys
import os

# tìm root project
ROOT = Path(__file__).resolve().parents[3]

# thêm src vào python path
sys.path.append(str(ROOT / "src"))

# import preprocessing
from utils.preprocess import create_features

# dataset path
path = ROOT / "data" / "creditcard.csv"

# load data
data = pd.read_csv(path)

# feature engineering (giống notebook)
data = create_features(data)

# feature và label
X = data.drop("Class", axis=1)
y = data["Class"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# scaling (Logistic Regression nên scale)
scaler = MinMaxScaler()

scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)

# model
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

# train
model.fit(scaled_X_train, y_train)

# predict
y_pred = model.predict(scaled_X_test)
y_prob = model.predict_proba(scaled_X_test)[:,1]

# accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# confusion matrix
confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion)

# classification report
print(classification_report(y_test, y_pred))

# ROC AUC
print("ROC AUC:", roc_auc_score(y_test, y_prob))