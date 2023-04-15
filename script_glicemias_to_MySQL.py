import pandas as pd
import os
from sqlalchemy import create_engine

#1 - abre o arquivo txt e coleta o valor da glicemia
glicemias = pd.read_csv('arquivo/Glicemia.txt', sep = ",", names=['glic_valor','glic_data'])

#2 Conectar ao banco de dados MySQL
engine = create_engine("mysql+pymysql://root:senhalocalhost/Glicemia")

#3 Levando dados do txt (dataframe) para o MySQL
glicemias.to_sql('glic_medicoes', engine, if_exists="append", index=False)

#4 - Apaga o conteúdo do arquio CSV
with open('arquivo/Glicemia.txt', "w") as file:
    pass
