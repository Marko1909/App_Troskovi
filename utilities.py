import sqlite3
from iznimke import IznimkaPrazanTekst, IznimkaPostojeciEmail

con = sqlite3.connect("troskoviDB.db")
cur = con.cursor()


def login_provjera(email, password):
    query = """
        SELECT id, ime, prezime, email, password FROM korisnik;
    """

    data = cur.execute(query).fetchall()

    for d in data:
        if d[3] == email and d[4] == password:
            return d


def signup_provjera(ime, prezime, email, password, provjera_passworda):
    query = """
        SELECT email FROM korisnik;
    """

    data = cur.execute(query).fetchall()

    try:
        if len(ime) == 0 or len(prezime) == 0 or len(email) == 0 or len(password) == 0 or len(provjera_passworda) == 0:
            raise IznimkaPrazanTekst()

        if password != provjera_passworda:
            raise Exception(f'Neispravan password!')

        for d in data:
            if d[0] == email:
                raise IznimkaPostojeciEmail()

    except IznimkaPrazanTekst as e:
        return str(e)

    except Exception as e:
        return str(e)

    except IznimkaPostojeciEmail as e:
        return str(e)


def provjera_unosa_troskova(troskovi):
        try:
            for trosak in troskovi:
                if trosak != '':
                    realan_broj = float(trosak)

                    broj = str(realan_broj).split('.')      # Rastavljanje stringa upisanog floata, i spremanje decimala

                    if len(broj[-1]) > 2:                   # Provjera upisanih decimala
                        raise ValueError

                    if realan_broj < 0:
                        raise Exception(f'Potrebno upisati pozitivan realni broj!')

        except ValueError:
            return 'Upišite realan broj, s maksimalno dvije decimale!'

        except Exception as e:
            return str(e)

