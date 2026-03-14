from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from pathlib import Path
import pandas as pd

# tìm root project
ROOT = Path(__file__).resolve().parents[3]

# dataset path
path = ROOT / "data" / "creditcard.csv"

# load data
data = pd.read_csv(path)

# feature và label
X = data.drop("Class", axis=1)
y = data["Class"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = LogisticRegression(max_iter=1000, class_weight="balanced")

# train
model.fit(X_train, y_train)

# predict
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))