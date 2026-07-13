import pandas as pd

df = pd.read_excel('ATC_GKV_AI_2026.xlsx', sheet_name='WIdO-Index 2026 ATC-Sortiert')
print(df.iloc[0:20])
