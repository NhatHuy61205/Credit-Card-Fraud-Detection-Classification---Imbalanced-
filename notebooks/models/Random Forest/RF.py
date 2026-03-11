from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from pathlib import Path
import pandas as pd

path = Path("data/creditcard.csv")

# Load dữ liệu
data = pd.read_csv(path)

# Chia feature và label
X = data.drop("Class", axis=1)
y = data["Class"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Tạo model Random Forest
model = RandomForestClassifier(
    n_estimators=100,     
    max_depth=None,        
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:,1]

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_prob))