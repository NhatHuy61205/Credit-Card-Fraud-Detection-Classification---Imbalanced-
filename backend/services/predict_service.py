import pandas as pd
from db.connection import SessionLocal, engine
from schema.transaction_input import TransactionInput
from model.predict import predict_output
from sqlalchemy import text

def prediction():
    query = "SELECT * FROM transactions WHERE proba IS NULL "
    df = pd.read_sql(query, engine)
    
    if df.empty:
        return 
    
    df['time_diff'] = df['Time'].diff().fillna(0)
    df['is_rapid_transaction'] = (df['time_diff'] < 60).astype(int)

    updates = []

    for idx, row in df.iterrows():
        try:
            tx = TransactionInput(**row.to_dict())

            features = {
                **{f'V{i}': row[f'V{i}'] for i in range(1,29)},
                '_log_amount': tx.log_amount,
                'is_night_proxy': tx.is_night_proxy,
                'is_business_hours_proxy': tx.is_business_hours_proxy,
                'hour_sin': tx.hour_sin,
                'hour_cos': tx.hour_cos,
                'time_diff': row['time_diff'],
                'is_high_amount': tx.is_high_amount,
                'is_rapid_transaction': row['is_rapid_transaction']
            }

            pred = predict_output(features)

            updates.append({
                'id': row['id'],
                'class': pred['class'],
                'proba': pred['proba'],
                'status': pred['status']
            })
        except Exception as e:
            print(f"Error at row {idx}: {e}")


    session = SessionLocal()
    try:
        for u in updates:
            session.execute(
                text("""
                    UPDATE transactions
                    SET class=:class, proba=:proba, status=:status
                    WHERE id=:id
                """), params=u
            )
        session.commit()

    except Exception as e:
        session.rollback()

    finally:
        session.close()

    return df
    