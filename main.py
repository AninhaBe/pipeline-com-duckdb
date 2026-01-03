from pipeline.bronze import salvar_bronze
from pipeline.silver import processar_silver
from pipeline.gold import gerar_gold
import time


def run_pipeline():
    DB_PATH = "projeto_eng.db"
    CSV_PATH = "data/vendas.csv"

    print("iniciando pipeline de dados...")

    try:
        start_time_bronze = time.time()
        salvar_bronze(DB_PATH, CSV_PATH)
        end_time_bronze = time.time()
        print(f"bronze executada em {end_time_bronze - start_time_bronze:.2f} segundos")

        start_time_silver = time.time()
        processar_silver(DB_PATH)
        end_time_silver = time.time()
        print(f"silver executada em {end_time_silver - start_time_silver:.2f} segundos")

        start_time_gold = time.time()
        gerar_gold(DB_PATH)
        end_time_gold = time.time()
        print(f"gold executada em {end_time_gold - start_time_gold:.2f} segundos")


        print('processamento concluído com sucesso!')
    except Exception as e:
        print("falha durante a execução", e)

if __name__ == "__main__":
    run_pipeline()

