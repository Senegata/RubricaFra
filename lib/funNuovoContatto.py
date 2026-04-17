from lib.libreria_pitonica_4 import *
from lib.inserimento import salvataggio

def salvocontatto():

    file = "mioFile.csv"                                                #* La funzione inizia verificando che il file .csv esista

    DIMENSIONE_MIN = 2
    DIMENSIONE_MAX = 30
    ANNO_NASCITA_MIN = 1950

    class ContattoObj:

        def __init__(self, nome, cognome, numero, eta):
            self.nome = nome
            self.cognome = cognome
            self.numero = numero
            self.eta = eta
# -------------------------
# Input Nome
# -------------------------
    contatti = []                                               #? Qui si avvia la scansione procedurale degli input per la
    while True:                                                 #? registrazione dell'utente.
        while True:
            nome = input("Inserisci Nome: ").strip()
            if not controllo_Nome_Cognome_conNull(nome, "nome"):
                continue
            break

        while True:
            cognome=input("Inserisci cognome: ").strip()
            if not controllo_not_null(cognome, "cognome"):
                continue
            if not controllo_Anagrafico_Classico(2, 20, cognome, "cognome"):
                continue
            break

        while True:
            numero = input("Inserisci numero di telefono: ")
            if not controllo_telefono(numero, "numero"):
                continue
            break

        while True:
            eta =input("Inserisci l'età del contatto: ")
            if not controllo_eta_max(120, eta):
                continue
            break


        # costruiamo l'oggetto studente una volta raccolti i dati
        contatto = ContattoObj(nome, cognome, numero, eta)

        contatti.append(contatto)


        while True:
            conferma = input("Vuoi inserire un altro contatto? (s/n)\n").lower()    #? Permettiamo all'utente di inserire un altro
            risposta = controllo_S_N(conferma)                                      #? studente senza dover tornare nel menù.
            if risposta == True:
                if conferma == "s":
                    break
                else:
                    break
        if conferma == "s":
            continue
        else:
            break

    salvataggio(contatti)
