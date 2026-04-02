import pandas as pd
from db.connection import engine
from schema.transaction_input import TransactionInput
from services.predict_service import prediction

def data(query):
    return pd.read_sql(query, engine)

def get_data(skip=0, limit=20, status=None):
    query = "SELECT * FROM transactions"

    if status is not None and status != "":
        query += f" WHERE status = '{status}'"

    if limit is not None:
        query += f" LIMIT {limit}"
        if skip is not None:
            query += f" OFFSET {skip}"

    df = data(query)

    return df.where(pd.notnull(df), None).to_dict(orient="records")

def total():
    df = data("SELECT COUNT(*) as total FROM transactions")
    return int(df['total'][0])

def amount_per_hour():
    df = data("SELECT * FROM transactions")
    df['Hour_from_start_mod24'] = df['Time'].apply(lambda t: int((t//3600)%24))
    
    df_grouped = df.groupby(["Hour_from_start_mod24", "status"])["Amount"].sum().reset_index()
    df_pivot = df_grouped.pivot(index="Hour_from_start_mod24", columns="status", values="Amount").fillna(0)
    
    return df_pivot.reset_index().to_dict(orient="records")


def amount_per_status():
    df = data("SELECT * FROM transactions")
    df_grouped = df.groupby("status")["Amount"].sum().reset_index()
    total_amount = df_grouped["Amount"].sum()
    df_grouped["percent"] = df_grouped["Amount"] / total_amount * 100
    df_grouped["bg"] = ["#f5b041", "#2e86de", "#ff7f0e"][:len(df_grouped)]
    
    return df_grouped.to_dict(orient="records")