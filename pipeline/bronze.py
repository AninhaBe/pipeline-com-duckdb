import duckdb

def salvar_bronze(db_path, csv_path):
    with duckdb.connect(db_path) as con:
        con.execute(f"""
                CREATE TABLE IF NOT EXISTS bronze_vendas as \
                SELECT * FROM read_csv_auto('{csv_path}')
        """)

        print("tabela bronze criada com sucesso!")
        print(con.execute('SELECT * FROM bronze_vendas').df())


if __name__ == "__main__":
    db_path = "projeto_eng.db"
    csv_path = "data/vendas.csv"
    salvar_bronze(db_path, csv_path)