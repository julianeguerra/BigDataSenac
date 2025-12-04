import pandas as pd
import numpy as np
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('track_data_final.csv', encoding='utf-8', sep=',')
print(df.head())
df.info()
df.describe()