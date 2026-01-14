import pandas as pd
import random

# Listas base para gerar combinações aleatórias
nomes = ["João", "Maria", "Ana", "Pedro", "Lucas", "Mariane", "Adriana", "Carlos", "Beatriz", "Marcos"]
sobrenomes = ["Silva", "Souza", "Rocha", "Oliveira", "Santos", "Lima", "Vera", "Cruz"]

dados = []

for i in range(50):
    nome_completo = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    # Gera salários entre 2000 e 8000 com 2 casas decimais
    salario = round(random.uniform(2000, 8000), 2)
    dados.append([nome_completo, salario])

# Cria o DataFrame e salva o CSV
df_50 = pd.DataFrame(dados, columns=['Nome', 'Salario_Mensal'])
df_50.to_csv('funcionarios.csv', index=False)

print(f"Sucesso! Arquivo 'funcionarios.csv' gerado com {len(df_50)} registros.")