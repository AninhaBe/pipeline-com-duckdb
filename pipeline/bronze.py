import duckdb

with duckdb.connect("projeto_eng.db") as con:
    con.execute("""
            CREATE TABLE IF NOT EXISTS bronze_vendas as \
            SELECT * FROM read_csv_auto('vendas.csv')
    """)

    print("tabela criada!")