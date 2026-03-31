import pandas as pd
from sqlalchemy import create_engine

# 1. Kết nối MySQL
engine = create_engine("mysql+pymysql://root:root@localhost/mldb")

# 2. Đọc file CSV
df = pd.read_csv("creditcard.csv")

df = df.sort_values("Time").reset_index(drop=True)

# 4. Lấy 20% cuối
df_last_20 = df.iloc[int(0.8 * len(df)) :]

# 5. Đẩy vào MySQL
df_last_20.to_sql(
    name="transactions",
    con=engine,
    if_exists="replace",
    index=False
)

print("✅ Đã import 20% dữ liệu cuối")