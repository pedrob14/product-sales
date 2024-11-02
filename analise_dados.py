import pandas as pd 
from sqlalchemy import create_engine 

# Conectando ao banco de dados
engine = create_engine('mysql+pymysql://username:password@localhost/Vendas')

# Carregando os dados da tabela de vendas
df = pd.read_sql('SELECT * FROM Vendas', engine)

# Analisando os dados
df['Total'] = df['Quantidade'] * df['Preco']
resumo = df.groupby('Produto').agg({'Quantidade': 'sum', 'Total': 'sum'}).reset_index()

# Exportando o resumo para um arquivo CSV
resumo.to_csv('resumo_vendas.csv', index=False)

print(resumo)
