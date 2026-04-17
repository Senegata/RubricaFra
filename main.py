
from lib.crea import crea
from lib.funNuovoContatto import salvocontatto
from lib.ricercaNumero import avvia_ricerca_numero
from lib.ricercaCognome import avvia_ricerca_cognome
from lib.lettoreFileDB import leggi
print(r"---"*10)                                    #* Start del programma
print("Benvenuto\a nella rubrica!")

while True:

    print(r"---"*10)                                #!  Qui abbiamo una scelta multipla,
    print("1️⃣  ➤ Crea File")
    print("2️⃣  ➤ 📄 Registra Contatto")
    print("3️⃣  ➤ 🔍 Ricerca Contatto")
    print("4️⃣  ➤  Visualizza rubrica")
    print("5️⃣  ➤ 🚪 Quit")

    print(r"---"*10)
    
    scelta = input("   Scelta: ")
    match scelta:
        case "1":
            crea()                                     #? Salvostudente è la funzione che registra lo studente nel file .csv
            continue
        case "2":
            salvocontatto()
            continue
        case "3":
            while True:
                print("Vuoi cercare per:")
                print("1. Cognome")
                print("2. Numero")
                print("3. Torna indietro...")
                scelta2 = input("      Scelta: ")
                match scelta2:
                    case "1":
                        avvia_ricerca_cognome()
                        continue
                    case "2":
                        avvia_ricerca_numero()
                        continue
                    case "3":
                        break
        case "4":
            leggi()
            continue
        case "5":
            print("allora Ciao!")
            break