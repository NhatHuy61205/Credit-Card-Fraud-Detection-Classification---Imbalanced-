import pandas as pd
import numpy as np 

def split_data(df, features, target): 
    df_sorted = df.sort_values("Time").reset_index(drop=True)
    cut = int(0.8 * len(df_sorted))
    
    train_df = df_sorted.iloc[:cut]
    test_df = df_sorted.iloc[cut:]
    
    cut_in = int(0.8 * len(train_df))
    train__df = train_df.iloc[:cut_in]
    val_df = train_df.iloc[cut_in:]
    
    X_train , y_train = train__df[features], train__df[target].astype(int)
    X_val, y_val = val_df[features], val_df[target].astype(int)
    X_test, y_test = test_df[features], test_df[target].astype(int)
    
    print("X_train:", X_train, "y_train:", y_train)
    print("X_val:", X_val, "y_val:", y_val)
    print("X_test:", X_test, "y_test:", y_test)
    print("Fraud rate in train:", y_train.mean())
    print("Fraud rate in test:", y_test.mean())
    
    return X_train, y_train, X_val, y_val, X_test, y_test 