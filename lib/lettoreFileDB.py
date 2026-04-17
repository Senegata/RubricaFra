import os
from lib.crea import PERCORSO_CSV


def leggi():
    try:
        if not os.path.exists(PERCORSO_CSV):
            print(f"Il file non esiste ancora: {PERCORSO_CSV}")
            return

        with open(PERCORSO_CSV, "r", encoding="utf-8") as file:
            contenuto = file.read()                                     #! Funzione che stampa all'utente l'estratto
            print(contenuto)                                            #! del file mioFile.csv
    except FileNotFoundError:
        print(f"Il file non esiste ancora: {PERCORSO_CSV}")
    except Exception as e:
        print(f"Errore leggendo il file {PERCORSO_CSV}: {e}")
