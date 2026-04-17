import csv                                                              #? Funzione che permette di cercare per cognome
import os
from lib.crea import PERCORSO_CSV


def ricercaCognome(percorso_file, campo, valore):
    risultati = []

    if not os.path.exists(percorso_file):
        print(f"File non trovato: {percorso_file}")
        return risultati

    try:
        with open(percorso_file, mode="r", encoding="utf-8") as file:
            lettore = csv.DictReader(file)

            if not lettore.fieldnames:
                print(f"File CSV vuoto o senza header: {percorso_file}")
                return risultati

            header_map = {h.strip().lower(): h for h in lettore.fieldnames if h}

            campo_norm = campo.strip().lower()
            # verifica che la colonna esista
            if campo_norm not in header_map:
                print("Errore: la colonna", campo, "non esiste nel CSV.")
                print("Header trovati:", lettore.fieldnames)
                return risultati

            campo_reale = header_map[campo_norm]

            for riga in lettore:
                valore_cella = (riga.get(campo_reale) or '').strip()
                if valore.lower() in valore_cella.lower():
                    risultati.append(riga)

    except Exception as e:
        print(f"Errore leggendo il file {percorso_file}: {e}")

    return risultati


def avvia_ricerca_cognome():
    valore = input("Inserisci il cognome da cercare: ")

    # usa il percorso assoluto definito in lib.crea
    risultati = ricercaCognome(PERCORSO_CSV, "cognome", valore)

    if risultati:
        print("------------------------------")
        print("Risultati Ricerca:")
        print("------------------------------")

        for r in risultati:
            # Normalizzo le chiavi (rimuovo spazi attorno agli header) prima di stampare
            normalized = {k.strip(): (v or '').strip() for k, v in r.items()}
            print(f"Nome: {normalized.get('Nome', '')}")
            print(f"Cognome: {normalized.get('Cognome', '')}")
            print(f"Numero: {normalized.get('Numero', '')}")
            # supporto sia 'Età' che 'Eta' senza accenti
            print(f"Eta: {normalized.get('Età', '') or normalized.get('Eta', '')}")
            print("------------------------------")
    else:
        print("Nessun contatto trovato.")
