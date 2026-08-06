import pandas as pd
import numpy as np

# Definindo os dados para as colunas
nomes_produtos = [f"Produto {i+1}" for i in range(50)]
categorias_produtos = np.random.choice(["Eletrônicos", "Livros", "Roupas", "Alimentos", "Brinquedos"], 50)
precos_produtos = np.random.uniform(10.0, 500.0, 50).round(2)
itens_vendidos = np.random.randint(1, 1000, 50)
avaliacoes_produtos = np.random.uniform(1.0, 5.0, 50).round(1)

import pandas as pd
import numpy as np

# Criando o DataFrame
df_produtos = pd.DataFrame({
    "Nome do produto": nomes_produtos,
    "Categoria do produto": categorias_produtos,
    "Preço do produto": precos_produtos,
    "Itens vendidos": itens_vendidos,
    "Avaliação do produto": avaliacoes_produtos
})

# Exibindo as primeiras linhas do DataFrame
# print(df_produtos.head())
print(df_produtos[(df_produtos["Categoria do produto"] == "Livros") & (df_produtos["Avaliação do produto"] > 3)])

print("\n")
print(df_produtos.iloc[15])

print("\n")
print(df_produtos.loc[15, "Preço do produto"])

eletronicos = df_produtos[df_produtos["Categoria do produto"] == "Eletrônicos"]

print(df_produtos.loc[eletronicos.index, ["Nome do produto", "Preço do produto"]])

