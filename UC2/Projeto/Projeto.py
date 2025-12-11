# import pandas as pd
# import numpy as np
# import mysql.connector
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv('track_data_final.csv', encoding='utf-8', sep=',')
# print(df.head())
# df.info()
# df.describe()


# import pandas as pd
# import numpy as np
# import mysql.connector
# import matplotlib.pyplot as plt
# import seaborn as sns
# import mysql.connector

# df = pd.read_csv('high_popularity_spotify_data', encoding='utf-8', sep=',')
# # print(df.head())
# # df.info()
# # df.describe()

# for linha in df["album_release_date"]:
#     if len(linha) > 4:
#         pass
#     else:
#         df["album_release_date"].add("-01-01")

# print(df["album_release_date"].head(30))

import mysql.connector

# 1. Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="spotify"
)

cursor = conexao.cursor()

query_popularidade = "SELECT track_name, track_popularity, track_artist FROM high_popularity_spotify_data WHERE track_popularity > 50"

cursor.execute(query_popularidade)

resultados_popularidade = cursor.fetchall()

# 6. Exibir os resultados
for linha in resultados_popularidade:
    print(linha)

# 7. Fechar a conexão
cursor.close()
conexao.close()