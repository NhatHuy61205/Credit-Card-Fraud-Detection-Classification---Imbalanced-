import numpy as np
import pandas as pd

def create_features(df):
    """Hàm tạo các đặc trưng mới từ dữ liệu gốc."""
    df = df.drop_duplicates().reset_index(drop=True)
    df['_log_amount'] = np.log1p(df['Amount'])
    df['Hour_from_start_mod24'] = ((df['Time'] // 3600) % 24).astype(int)
    df['is_night_proxy'] = df['Hour_from_start_mod24'].isin([22,23,0,1,2,3,4,5]).astype(int)
    df['is_business_hours_proxy'] = df['Hour_from_start_mod24'].between(9,17).astype(int)

    return df