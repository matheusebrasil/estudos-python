# People Analytics ETL Pipeline 🚀

## 📋 Sobre o Projeto
Este repositório contém um pipeline de ETL (Extract, Transform, Load) focado em **People Analytics**. O objetivo é processar dados brutos de colaboradores para gerar insights salariais, garantindo a integridade e a padronização das informações para consumo em ferramentas de BI (como Power BI).

## 🏗️ Arquitetura do Pipeline
1. **Extração:** Consumo de arquivos CSV brutos (Camada Bronze).
2. **Transformação:** - Normalização de strings (Case-folding e Strip).
   - Cálculo de métricas de negócio (Cálculo de Provisão de 13º Salário).
   - Filtragem de Data Quality (Remoção de ruídos e outliers).
3. **Carga:** Geração de arquivos curados (Camada Silver) prontos para análise.

## 🛠️ Tecnologias e Ferramentas
- **Linguagem:** Python 3.13
- **Biblioteca Principal:** Pandas (Processamento de dados vetorizado)
- **Gestão de Dependências:** Python Venv

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/matheusebrasil/estudos-python.git](https://github.com/matheusebrasil/estudos-python.git)
