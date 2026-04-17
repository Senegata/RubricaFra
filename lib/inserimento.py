import csv
import os
import errno

from lib.crea import PERCORSO_CSV

def salvataggio(contatti):
    file = PERCORSO_CSV
    try:
        file_vuoto = not os.path.exists(file) or os.path.getsize(file) == 0

        with open(file, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if file_vuoto:
                writer.writerow(["Nome", " Cognome", " Numero", " Età"])

            # Scrivo i record
            for s in contatti:
                writer.writerow([s.nome, s.cognome, s.numero, s.eta])


    except PermissionError as e:
        print(f"❌ Errore 403 - Non hai il permesso per accedere al file.")
        print(f"   Dettagli: {e}")

    except FileNotFoundError as e:
        print(f"❌ Errore 404 - File o directory non trovata")
        print(f"   Dettagli: {e}")

    except IsADirectoryError:
        print(f"❌ Errore - Tentavi di aprire una directory come file")

    except NotADirectoryError:
        print(f"❌ Errore - Il percorso contiene un file dove servirebbe una directory")

    except OSError as errore:
        if errore.errno == errno.ENOENT:
            print(f"❌ Errore {errore.errno} - File o directory non trovata")
        elif errore.errno == errno.EACCES:
            print(f"❌ Errore {errore.errno} - Permesso negato")
        elif errore.errno == errno.ENOSPC:
            print(f"❌ Errore {errore.errno} - Spazio su disco insufficiente")
        elif errore.errno == errno.ENODEV:
            print(f"❌ Errore {errore.errno} - Disco non trovato")
        elif errore.errno == errno.EROFS:
            print(f"❌ Errore {errore.errno} - File system in sola lettura")
        elif errore.errno == errno.EBUSY:
            print(f"❌ Errore {errore.errno} - File occupato da un altro processo")
        elif errore.errno == errno.EEXIST:
            print(f"❌ Errore {errore.errno} - Il file esiste già")
        else:
            print(f"❌ Errore OSError generico: {errore}")
        print(f"   Dettagli: {errore}")

    except UnicodeEncodeError:
        print(f"❌ Errore di encoding - Caratteri non scrivibili")

    except UnicodeDecodeError:
        print(f"❌ Errore di decoding - Encoding file non compatibile")

    except IOError as e:
        print(f"❌ Errore I/O generico: {e}")

    except Exception as e:
        print(f"❌ Errore inaspettato: {type(e).__name__}")
        print(f"   Dettagli: {e}")

    else:
        print("✅ File creato e scritto con successo!")

    finally:
        print("🔚 Operazione completata!")
