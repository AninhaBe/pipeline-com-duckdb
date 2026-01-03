import duckdb

def gerar_gold(db_path):
    with duckdb.connect(db_path) as con:
        con.execute("""
            CREATE OR REPLACE TABLE gold_vendas_por_produto AS
            SELECT
                produto,
                SUM(valor) AS faturamento_total,
                COUNT(*) as quantidade_vendida
            FROM (SELECT DISTINCT * FROM silver_vendas)
            GROUP BY produto
            ORDER BY faturamento_total DESC
        """)

        print("tabela gold criada com sucesso!")
        print(con.execute('SELECT * FROM gold_vendas_por_produto').df())

if __name__ == "__main__":
    db_path = "projeto_eng.db"
    gerar_gold(db_path)