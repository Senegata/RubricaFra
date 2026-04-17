import re

"""
-----------------------------
LIBRERIA A CURA DI FRANCESCO A. PEPE
DIVERTITI E COPIA PURE! :D

Libreria Open-Source
                contribuite pure!
15 Marzo 2026
Se vuoi visualizzare i commenti colorati, scarica l'estensione "Better Comments"
"""
#! Come importare la libreria? Semplice!
#? Se salvi la libreria in una cartella diversa, digita "FROM libreria_pitonica_3 import *"
#? Ti raccomando di chiamare esclusivamente le funzioni che usi, il * non è raccomandato.
#* Se salvi il file nella stessa cartella del main, ti basterà importare solo la libreria. (import libreria_pitonica_3)

"""
---------------------------------
#?CONTROLLO NOT NULL                                     (not) NULL
---------------------------------
Controlla che il campo non sia vuoto.

"""
def controllo_not_null(stringa_input, nome_campo):      # CONTROLLO NULL
    if stringa_input:
        return True
    else:
        print(f"Errore: {nome_campo} obbligatorio.")
        return False

"""
------------------------------------
#*CONTROLLO ANAGRAFICO CLASSICO
-----------------------------------
Controllo generale che verifica:
- Validità Caratteri
- Lunghezza Minima
- Lunghezza Massima
- Gestione generale di errori di vario tipo

"""
def controllo_Anagrafico_Classico(minimo, massimo, stringa_input, nome_campo):
    if not stringa_input:
        print("Errore: campo obbligatorio.")
        return False
    if len(stringa_input) < minimo and not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", stringa_input):
        print(f"Errore per il {nome_campo}: minimo {minimo} caratteri e accetto solo caratteri validi.")
        return False
    if len(stringa_input) < minimo and re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", stringa_input):
        print(f"Errore: minimo {minimo} caratteri.")
        return False
    if len(stringa_input) > massimo and not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", stringa_input):
        print(f"Errore per il {nome_campo}: massimo {massimo} caratteri e accetto solo caratteri validi.")
        return False
    if len(stringa_input) > massimo and re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", stringa_input):
        print(f"Errore: Massimo {massimo} caratteri.")
        return False
        # Solo lettere, anche accentate, e apostrofo
    if re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", stringa_input):
        return True
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]+$", stringa_input):
        print("Accetto solo caratteri.")
    else:
        print(f"Errore: {nome_campo} errato.")
        return False
    
"""
-------------------------------------
#*ACCETTO CARATTERI NULL
-------------------------------------
Accetta da stringa anche i caratteri NULL, oltre i vari controlli.
"""
DIMENSIONE_MIN = 2
DIMENSIONE_MAX = 30
def controllo_Nome_Cognome_conNull(stringa_input, messaggio):
    if len(stringa_input) > DIMENSIONE_MAX and not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]*$", stringa_input):
        print(f"Errore per il {messaggio}: massimo {DIMENSIONE_MAX} caratteri e accetto solo caratteri validi.")
        return False
    if len(stringa_input) > DIMENSIONE_MAX and re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]*$", stringa_input):
        print(f"Errore: Massimo {DIMENSIONE_MAX} caratteri.")
        return False
        # Solo lettere, anche accentate, e apostrofo
    if re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]*$", stringa_input):
        return True
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]*$", stringa_input):
        print("Accetto solo caratteri.")
    else:
        print(f"Errore: {messaggio} errato.")
        return False 
""" 
--------------------------------
#*CONTROLLO CARATTERI ALFABETICI                      Abc
--------------------------------
Controlla che un campo abbia 
solo lettere dell'alfabeto.

"""

def controllo_caratteri_alfabetici(stringa_input, nome_campo):
    if (re.match(r"^[A-Za-z ]+$",stringa_input)):
        return True
    else:
        print(f"Per {nome_campo} accetto solo caratteri alfabetici.\n")
        return False


"""
-----------------------------------
#?CONTROLLO STRINGA LUNGHEZZA MINIMA              Minimo < Aa 
-----------------------------------
Controlla che una stringa superi
un numero minimo di caratteri

"""
def controllo_stringa_lunghezza_minima(minimo, stringa_input, nome_campo):
    if len(stringa_input) >= minimo:
        return True
    elif len(stringa_input) < minimo:
        print(f"Per {nome_campo} deve avere più di {minimo} caratteri.")
        return False
    
    
"""
-----------------------------------
#?CONTROLLO STRINGA LUNGHEZZA MASSIMA              Aa < Massimo
-----------------------------------
Controlla che una stringa superi
un numero massimo di caratteri

"""
def controllo_stringa_lunghezza_massima(massimo, stringa_input, nome_campo):
    if len(stringa_input) <= massimo:
        return True
    elif len(stringa_input) > massimo:
        print(f"Per {nome_campo} deve avere meno di {massimo} caratteri.")
        return False
    
    

"""
-------------------------------------
#?CONTROLLO LUNGHEZZA MIN - MAX
-------------------------------------
Controlla che la stringa sia tra un MIN e un MAX caratteri.
"""

def controllo_stringa_lunghezza_MinMax(minimo, massimo, stringa_input, nome_campo):
    if len(stringa_input) >= minimo and len(stringa_input) <= massimo:
        return True
    else:
        print(f"In {nome_campo} valore minimo {minimo} e massimo {massimo} non rispettato.")
        return False
"""
-----------------------------------
#?CONTROLLO DATI NUMERICI                               123456789
------------------------------------
Controlla che un campo abbia solo numeri 
(interi, negativi, decimali)

"""

def controllo_dati_numerici(stringa_input, nome_campo):
    try:
        float(stringa_input)  # Accetta interi, negativi e decimali
        return True
    except ValueError:
        print(f"Per {nome_campo} accetto solo numeri.\n")
        return False

"""
------------------------------------
#*CONTROLLO FORMATO EMAIL VALIDA                      francesco@gmail.com
------------------------------------
Controllo validità formato mail.
es: nome@dominio.com

"""
def controllo_email(stringa_input, nome_campo):
    if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", stringa_input):
        return True
    else:
        print(f"Per {nome_campo} inserisci un'email valida (es: nome@dominio.com).\n")
        return False
    

"""
-------------------------------------------
#?CONTROLLO NUMERO TELEFONO ITALIANO VALIDO               3515584786 (10 cifre)
-------------------------------------------
Controllo validità numero di telefono

"""

def controllo_telefono(stringa_input, nome_campo):
    if re.match(r"^\d{10}$", stringa_input):
        return True
    else:
        print(f"Per {nome_campo} accetto solo 10 cifre.\n")
        return False
    
"""
-----------------------------------------
#!CONTROLLO S / N                                            vuoi confermare? s / n
----------------------------------------
"""
def controllo_S_N(string_input):
    if string_input in ["s", "n"]:
        return True
    else:
        print("Valore non valido")
        return False
    

"""
---------------------------------------------------
#! CONTROLLO ETA' min - max
---------------------------------------------------
"""

def controllo_eta_MinMax(min, max, eta_input):
    # accetta solo numeri interi (anche più cifre) e controlla il range
    if re.match(r"^\d+$", str(eta_input)):
        valore = int(eta_input)
        if min <= valore <= max:
            return True
    print(f"Età non valida. Assicurarsi di aver inserito un numero valido. Attenzione: il range è da {min} a {max} anni.")
    return False

"""
---------------------------------------------------
#! CONTROLLO ETA' - max
---------------------------------------------------
"""

def controllo_eta_max(max, eta_input):
    # accetta solo numeri interi e verifica che siano <= max
    if re.match(r"^\d+$", str(eta_input)):
        valore = int(eta_input)
        if valore <= max:
            return True
    print(f"Età non valida. Assicurarsi di aver inserito un numero valido. Attenzione: si accettano solo massimo {max} anni.")
    return False
