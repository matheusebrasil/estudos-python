import pandas as pd

# EXTRAÇÃO: Lendo o arquivo bruto
df = pd.read_csv('funcionarios.csv')

# TRANSFORMAÇÃO: Limpeza e Regras de Negócio
df['Nome'] = df['Nome'].str.strip().str.title()
df['Salario_Anual'] = df['Salario_Mensal'] * 13

# LOAD: Gerando o resultado para quem ganha acima de 3000
df_final = df[df['Salario_Mensal'] > 3000]
df_final.to_csv('relatorio_final.csv', index=False)

print("Processamento concluído com sucesso!")
print(df_final)