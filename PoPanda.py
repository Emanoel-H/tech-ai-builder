import pandas as pd
from pathlib import Path

path = Path.home() / "Downloads" / "meu_csv.csv"

df = pd.read_csv(path)

print(df.head())