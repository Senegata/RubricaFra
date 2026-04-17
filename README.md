# RubricaFra

Una semplice rubrica scritta in Python per gestire contatti locali.

## Descrizione

Questo progetto fornisce utility per creare, inserire, leggere e cercare contatti.
È pensato come esercizio didattico per imparare a organizzare moduli Python e a gestire file di dati locali.

## Caratteristiche

- Creazione di nuovi contatti
- Inserimento e salvataggio su file
- Lettura del database locale
- Ricerca per cognome e per numero di telefono

## Requisiti

- Python 3.8+ (consigliato)

## Installazione e avvio

1. Clona il repository o scarica i file nel tuo progetto.
2. Dal terminale, esegui:

```bash
python main.py
```

Questo avvierà lo script principale che usa i moduli nella cartella `lib`.

## Struttura del progetto

- `main.py` - Punto di ingresso dell'applicazione.
- `cartellaDati/` - Cartella destinata ai file di dati (rubrica).
- `lib/` - Moduli della libreria del progetto:
  - `crea.py` - Funzioni per creare strutture/oggetti contatto.
  - `funNuovoContatto.py` - Funzionalità per gestire un nuovo contatto.
  - `inserimento.py` - Logica per inserire contatti nel file.
  - `lettoreFileDB.py` - Lettura del database/archivio contatti.
  - `libreria_pitonica_4.py` - Raccolta di utility generiche.
  - `ricercaCognome.py` - Ricerca contatti per cognome.
  - `ricercaNumero.py` - Ricerca contatti per numero di telefono.

## Esempio d'uso

Eseguire `main.py` e seguire le istruzioni interattive (se presenti).

## Contribuire

Se vuoi contribuire, apri una issue o invia una pull request con miglioramenti o correzioni.

## Licenza

Licenza da definire (es. MIT). Se desideri, posso aggiungere una `LICENSE`.

---

Se vuoi, posso:
- adattare il README con più dettagli sul funzionamento delle singole funzioni,
- aggiungere un file `LICENSE` (es. MIT),
- o committare e preparare il repository per il push su GitHub.
