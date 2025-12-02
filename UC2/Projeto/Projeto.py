import pandas as pd

df = pd.read_csv('MostStreamedSpotifySongs2024.csv', encoding='latin1', sep=',')
print(df.head(10))