import pandas as pd
import numpy as np

data = {
    'vendas': [150, 200, 170, 180, 220, 250, 300, 100, 120, 160]
}

df = pd.DataFrame(data)

media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Desvio padrão: {desvio_padrao}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
