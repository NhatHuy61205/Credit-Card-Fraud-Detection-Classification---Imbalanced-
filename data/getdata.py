import pandas as pd
from sqlalchemy import create_engine
import numpy as np

engine = create_engine("mysql+pymysql://root:root@localhost/mldb")

df = pd.read_csv("part_2.csv")

# chia 5 phần
parts = np.array_split(df, 5)

# lưu file tự động
for i, part in enumerate(parts):
    part = pd.DataFrame(part, columns=df.columns)
    part.to_csv(f"test_{i+1}.csv", index=False)