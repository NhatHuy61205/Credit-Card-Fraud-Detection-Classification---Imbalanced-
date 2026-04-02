import joblib
import pandas as pd

ensemble = joblib.load("model/ensemble_overall.pkl")

MODEL_VERSION = "1.0.0"

def predict_output(transaction_input: dict):

    df = pd.DataFrame([transaction_input])

    xgb_pred = ensemble["models"]["xgb"].predict_proba(df)[:,1]  
    lgb_pred = ensemble["models"]["lgbm"].predict_proba(df)[:,1]

    final_pred = xgb_pred * ensemble["weights"]["xgb"] + lgb_pred * ensemble["weights"]["lgbm"]

    predicted_category = int(final_pred > ensemble["threshold"])
    proba = float(final_pred[0]) * 100

    if proba > 0.9:
        flag = "warning"
    elif proba >= 0.6:
        flag = "disputed"
    else:
        flag = "success"

    return {
        "class": predicted_category,
        "proba": proba,
        "status": flag
    }