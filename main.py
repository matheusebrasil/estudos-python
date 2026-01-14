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
print(f"O arquivo final tem {len(df_final)} linhas.")


# Criando uma estilização básica profissional (Estilo Google Sheets)
estilo_css = """
<style>
    body { font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }
    table { border-collapse: collapse; width: 100%; background-color: white; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    th { background-color: #1a73e8; color: white; padding: 12px; text-align: left; }
    td { padding: 10px; border-bottom: 1px solid #ddd; }
    tr:hover { background-color: #f1f3f4; }
    h2 { color: #202124; }
</style>
"""

# Gerando o HTML
html_content = estilo_css + "<h2>Relatório de People Analytics - Salários acima de R$ 3.000</h2>" + df_final.to_html(index=False)

# Salvando o arquivo
with open("relatorio_estilizado.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Relatório HTML gerado! Abra o arquivo 'relatorio_estilizado.html' no seu navegador.")