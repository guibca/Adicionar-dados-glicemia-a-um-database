#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install sqlalchemy')
get_ipython().system('pip install pymysql')
import pandas as pd
import os
from sqlalchemy import create_engine


# In[2]:


#1 - abre o arquivo txt e coleta o valor da glicemia
glicemias = pd.read_csv('arquivo/Glicemia.txt', delimiter = ",", names=['glic_valor','glic_data'])
print(glicemias)


# In[3]:


#2 Conectar ao banco de dados MySQL
engine = create_engine("mysql+pymysql://root:34153416@localhost/Glicemia")


# In[4]:


#3 Levando dados do txt (dataframe) para o MySQL
glicemias.to_sql('glic_medicoes', engine, if_exists="append", index=False)


# In[5]:


#4 - Apaga o conteúdo do arquio CSV
with open('arquivo/Glicemia.txt', "w") as file:
    pass


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:



