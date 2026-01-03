import duckdb

with duckdb.connect("projeto_eng.db") as con:
    con.execute("""
        CREATE OR REPLACE TABLE gold_vendas_por_produto AS
        SELECT
            produto,
            SUM(valor) AS faturamento_total,
            COUNT(*) as quantidade_vendida,
        FROM (SELECT DISTINCT * FROM silver_vendas)
            group by produto
            order by faturamento_total DESC
""")
    print('tabela Gold gerada com sucesso!')
    print(con.execute('SELECT * FROM gold_vendas_por_produto').df())