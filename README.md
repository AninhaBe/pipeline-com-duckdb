# Pipeline de Vendas com DuckDB 🦆

Este projeto implementa uma pipeline de dados simples utilizando a arquitetura de medalhão (Bronze, Silver e Gold) para processar dados de vendas de forma local, eficiente e persistente. A intenção é fixar o conhecimento em relação a usabilidade do DuckDB.

## Arquitetura do Projeto

O projeto segue uma estrutura modular, separando a responsabilidade de cada etapa da pipeline:

- **data/**: Armazena os arquivos brutos (Landing Zone).
- **pipeline/**: Contém os scripts Python de processamento.
- **projeto_eng.db**: Banco de dados DuckDB onde os dados são persistidos.

## Camadas da Pipeline

1.  **Bronze (`bronze.py`)**: Realiza a ingestão do arquivo `vendas.csv` utilizando a função `read_csv_auto`. Nesta etapa, o DuckDB infere os tipos de dados automaticamente através de amostragem (sniffing), criando a tabela inicial `bronze_vendas`.
2.  **Silver (`silver.py`)**: Camada de limpeza e tipagem. Aqui os dados são convertidos para os tipos corretos (Integer, Double, Date), textos são padronizados em maiúsculas e valores nulos são tratados.
3.  **Gold (`gold.py`)**: Camada de negócio. Realiza a deduplicação dos dados e agregações (soma de faturamento e contagem de itens) por produto.

## Tecnologias Utilizadas

- **Python 3.x**
- **DuckDB**: Motor de processamento SQL in-process.
- **Pandas**: Utilizado apenas para visualização dos resultados no terminal.

## Como Rodar

1. Certifique-se de ter o DuckDB instalado:
   ```bash
   pip install duckdb

2. Execute a pipeline na ordem lógica:
    ```bash
    python pipeline/bronze.py
    python pipeline/silver.py
    python pipeline/gold.py