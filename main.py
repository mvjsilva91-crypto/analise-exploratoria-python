import pandas as pd
from matplotlib import pyplot as plt

print("="*50)
print("📊 CRIAÇÃO DO DATAFRAME")
print("="*50)

# Dados
dados = {
    'Nome': ['Ana', 'João', 'Maria', 'Pedro', 'Carla'],
    'Idade': [25, 30, 35, 28, 32],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Porto Alegre'],
    'Salário': [5000, 7000, 6000, 5500, 6500]
}

# DataFrame
df = pd.DataFrame(dados)

print(df)

print("\n" + "="*50)
print("📌 INFORMAÇÕES")
print("="*50)

print("Shape:", df.shape)
print("Colunas:", df.columns.tolist())
print("Tipos:\n", df.dtypes)

print("\n📌 Primeiras linhas:")
print(df.head())

print("\n📌 Últimas linhas:")
print(df.tail())

print("\n📊 Estatísticas:")
print(df.describe())

# ---------------- FILTROS ---------------- #

print("\n📌 Pessoas com mais de 30 anos:")
print(df[df['Idade'] > 30])

print("\n📌 Salário acima de 6000:")
print(df[df['Salário'] > 6000])

print("\n📌 Moram em São Paulo:")
print(df[df['Cidade'] == "São Paulo"])

# ---------------- MÉTRICAS ---------------- #

print("\n📊 Métricas de Idade:")
print("Soma:", df['Idade'].sum())
print("Média:", df['Idade'].mean())
print("Máximo:", df['Idade'].max())
print("Mínimo:", df['Idade'].min())

# ---------------- GRÁFICO ---------------- #

print("\n📈 Gerando gráfico...")

df['Idade'].plot(kind='line', figsize=(8, 4), title='Idade')
plt.gca().spines[['top', 'right']].set_visible(False)
plt.show()