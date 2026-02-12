import pandas as pd
import os

# Caminho do CSV
arquivo = r"C:\Users\d912425\Desktop\feiras_livres.csv"

# Ler CSV (normalmente é separado por vírgula)
df = pd.read_csv(arquivo)

# Ver quais valores existem na coluna SUB-PREF.
print(df["SUB-PREF."].unique())

# Filtrar apenas Campo Limpo
df_campo_limpo = df[df["SUB-PREF."].str.upper() == "CAMPO LIMPO"]

# Salvar resultado em Downloads
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
saida = os.path.join(downloads, "feiras_campo_limpo.csv")

df_campo_limpo.to_csv(saida, index=False, sep=";", encoding="utf-8-sig")

print("Arquivo salvo em:", saida)

quantidade = len(df_campo_limpo)
print("Quantidade de feiras em Campo Limpo:", quantidade)

import pandas as pd
import os

arquivo = r"C:\Users\d912425\Desktop\feiras_livres.csv"

df = pd.read_csv(arquivo)

# Filtrar Campo Limpo
df_campo_limpo = df[
    df["SUB-PREF."].str.strip().str.upper() == "CAMPO LIMPO"
]

print("Total de feiras:", len(df_campo_limpo))

# Salvar todas as linhas filtradas
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
saida = os.path.join(downloads, "feiras_campo_limpo.csv")

df_campo_limpo.to_csv(saida, index=False, sep=";", encoding="utf-8-sig")

print("Arquivo salvo em:", saida)
