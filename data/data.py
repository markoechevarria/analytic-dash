import os
import pandas as pd

BASE_DIR = os.path.dirname(__file__)
CSV_PATH = os.path.join(BASE_DIR, "sales.csv")

def load_data():
    return pd.read_csv(CSV_PATH, nrows=1_000, low_memory=False)

df = load_data()