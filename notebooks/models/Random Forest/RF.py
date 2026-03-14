from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
from pathlib import Path
import pandas as pd

path = Path("data/creditcard.csv")

