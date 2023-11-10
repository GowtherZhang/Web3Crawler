import pandas as pd

df = pd.read_csv('data2.csv')
for index, row in df.iterrows():
    print(row.tolist())