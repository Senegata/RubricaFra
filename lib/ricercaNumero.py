import csv                                                              #? Funzione che permette di cercare per cognome
from lib.crea import PERCORSO_CSV
                                                                        #? un determinato studente.
def ricercaNumero(percorso_file, campo, valore):
    risultati = []

    with open(percorso_file, mode="r", encoding="utf-8") as file:
        lettore = csv.DictReader(file)

        header_map = {h.strip().lower(): h for h in lettore.fieldnames}         #! Funzione integrata in avvia_ricerca()

        campo_norm = campo.strip().lower()
                                                                                #? Permette di prendere l'input cognome da cercare
        if campo_norm not in header_map:                                        #? e verificare che sia presente nel file .csv
            print("Errore: la colonna", campo, "non esiste nel CSV.")
            print("Header trovati:", lettore.fieldnames)
            return []

        campo_reale = header_map[campo_norm]

        for riga in lettore:
            if valore.lower() in riga[campo_reale].lower():
                risultati.append(riga)

    return risultati


def avvia_ricerca_numero():
    valore = input("Inserisci il numero da cercare: ")

    # usa il percorso assoluto definito in lib.crea
    risultati = ricercaNumero(PERCORSO_CSV, "numero", valore)

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
