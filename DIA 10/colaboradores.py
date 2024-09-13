import pandas as pd
import numpy as np

data = {'nome': ['Alice', 'Bob', 'Carlos', 'Diana', 'Eva'],
        'departamento': ['TI', 'Marketing', 'TI', 'RH', 'TI'],
        'salario': [5000, 4500, 5500, 4000, 6000]}

df = pd.DataFrame(data)

# Filtrar funcionários do departamento "TI"
df_ti = df[df['departamento'] == 'TI']

# Calcular a média salarial usando NumPy
media_salarial_ti = np.mean(df_ti['salario'])

print(f'Média salarial do departamento de TI: {media_salarial_ti:.2f}')