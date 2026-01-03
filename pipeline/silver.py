import duckdb

with duckdb.connect("projeto_eng.db") as con:
    con.execute("""
        CREATE OR REPLACE TABLE silver_vendas AS
        SELECT
            CAST(id AS INTEGER) AS id,
            UPPER(produto) AS produto,
            CAST(valor as double) AS valor,
            COALESCE(CAST(data AS DATE), '1900-01-01') AS data_venda
        FROM bronze_vendas
        WHERE id IS NOT NULL
""")
    print(con.execute('SELECT * FROM silver_vendas').df())

print("Tabela Silver criada com sucesso a partir da Bronze!")

