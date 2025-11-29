import pandas as pd

dados = pd.read_csv('MostStreamedSpotifySongs2024.csv', encoding='ISO-8859-1', sep=',')
print(dados.head(10))