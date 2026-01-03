import os

print("------ Iniciando Pipeline ------")
os.system("python pipeline/bronze.py")
os.system("python pipeline/silver.py")
os.system("python pipeline/gold.py")
print("------ Pipeline finalizada com sucesso! ------")