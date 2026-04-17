
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
progetto_dir = os.path.dirname(base_dir)
cartella_csv = os.path.join(progetto_dir, "cartellaDati")
os.makedirs(cartella_csv, exist_ok=True)

PERCORSO_CSV = os.path.join(cartella_csv, "fileDB.csv")

def crea():
    with open(PERCORSO_CSV, "w", encoding="utf-8") as file:
        pass
    print("File creato in:", PERCORSO_CSV)