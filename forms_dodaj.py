import tkinter as tk
from tkinter import messagebox
from db_uzytkowe import get_database
from bson import ObjectId

baza = get_database()

import tkinter as tk
from tkinter import messagebox
import re  # Do walidacji e-maila i daty

import tkinter as tk
from tkinter import messagebox
import re  # Do walidacji e-maila i daty


def tworzenie_formularza_pacjent(form_frame, powrot_do_menu, tytul_label):
    def dodaj_pacjenta():
        try:
            #WALIDACJA IMIENIA I NAZWISKA (isalpha)
            imie_value = imie_entry.get().strip()
            nazwisko_value = nazwisko_entry.get().strip()

            if not imie_value.isalpha():
                messagebox.showerror("Błąd", "Imię może zawierać tylko litery.")
                return

            if not nazwisko_value.isalpha():
                messagebox.showerror("Błąd", "Nazwisko może zawierać tylko litery.")
                return

            #WALIDACJA ADRESU E-MAIL
            email_input = email_entry.get().strip()
            pattern_email = r'^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$'
            if not re.match(pattern_email, email_input):
                messagebox.showerror("Błąd", "Niepoprawny adres mail!")
                return

            #WALIDACJA DATY (YYYY-MM-DD)
            data_input = data_entry.get().strip()
            pattern_data = r'^\d{4}-\d{2}-\d{2}$'
            if not re.match(pattern_data, data_input):
                messagebox.showerror(
                    "Błąd",
                    "Niepoprawny format daty! Wpisz ROK-MIESIĄC-DZIEŃ (np. 2025-01-16)."
                )
                return

            #WALIDACJA TYPÓW: wiek (int), wzrost (float)
            try:
                wiek_value = int(wiek_entry.get().strip())
            except ValueError:
                messagebox.showerror("Błąd", "Wiek musi być liczbą całkowitą.")
                return

            try:
                wzrost_value = float(wzrost_entry.get().strip())
            except ValueError:
                messagebox.showerror("Błąd", "Wzrost musi być liczbą zmiennoprzecinkową.")
                return

            #WALIDACJA CHORÓB
            choroby_input = choroby_entry.get().strip()
            if not choroby_input:
                choroby = []
            else:
                choroby_raw = choroby_input.split('|')
                choroby = []
                for choroba_str in choroby_raw:
                    nazwa, objawy_str = choroba_str.split(';')
                    objawy_list = [o.strip() for o in objawy_str.split(',')]
                    choroby.append({
                        "nazwa": nazwa.strip(),
                        "objawy": objawy_list
                    })

            # Generowanie nowego ID pacjenta
            ostatni_pacjent = baza["pacjenci"].find_one(sort=[("_id", -1)])
            if ostatni_pacjent is not None:
                nowe_id = ostatni_pacjent["_id"] + 1
            else:
                nowe_id = 1

            #Budowanie słownika pacjenta
            nowy_pacjent = {
                "_id": nowe_id,
                "imie": imie_value,
                "nazwisko": nazwisko_value,
                "wiek": wiek_value,
                "wzrost": wzrost_value,
                "ubezpieczony": ubezpieczony_var.get(),
                "choroby": choroby,
                "dane_kontaktowe": {
                    "telefon": telefon_entry.get().strip(),
                    "email": email_input
                },
                "data_rejestracji": data_input
            }

            #Zapis do bazy
            baza["pacjenci"].insert_one(nowy_pacjent)
            messagebox.showinfo("Sukces", f"Dodano pacjenta z ID = {nowe_id}!")

        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się dodać pacjenta: {e}")

    #Reszta kodu do tworzenia pól formularza jak poprzednio
    tytul_label.config(text="Kolekcja: pacjenci")

    tk.Label(form_frame, text="Dodaj pacjenta", font=("Arial", 12, "bold")).pack(anchor='nw', pady=5)

    imie_frame = tk.Frame(form_frame)
    imie_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(imie_frame, text="Imię").pack(anchor='center', padx=10)
    imie_entry = tk.Entry(imie_frame, width=30)
    imie_entry.pack(anchor='w', pady=5, padx=10)

    nazwisko_frame = tk.Frame(form_frame)
    nazwisko_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(nazwisko_frame, text="Nazwisko").pack(anchor='center', padx=10)
    nazwisko_entry = tk.Entry(nazwisko_frame, width=30)
    nazwisko_entry.pack(anchor='w', pady=5, padx=10)

    wiek_frame = tk.Frame(form_frame)
    wiek_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(wiek_frame, text="Wiek").pack(anchor='center', padx=10)
    wiek_entry = tk.Entry(wiek_frame, width=30)
    wiek_entry.pack(anchor='w', pady=5, padx=10)

    wzrost_frame = tk.Frame(form_frame)
    wzrost_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(wzrost_frame, text="Wzrost").pack(anchor='center', padx=10)
    wzrost_entry = tk.Entry(wzrost_frame, width=30)
    wzrost_entry.pack(anchor='w', pady=5, padx=10)

    ubezpieczony_var = tk.BooleanVar()
    tk.Checkbutton(form_frame, text="Ubezpieczony", variable=ubezpieczony_var).pack(anchor='w', pady=5, padx=10)

    choroby_frame = tk.Frame(form_frame)
    choroby_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(choroby_frame, text="Choroby (np. Grypa;kaszel,katar | Angina;ból gardła,gorączka)").pack(anchor='center', padx=10)
    choroby_entry = tk.Entry(choroby_frame, width=50)
    choroby_entry.pack(anchor='w', pady=5, padx=10)

    telefon_frame = tk.Frame(form_frame)
    telefon_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(telefon_frame, text="Telefon kontaktowy").pack(anchor='center', padx=10)
    telefon_entry = tk.Entry(telefon_frame, width=30)
    telefon_entry.pack(anchor='w', pady=5, padx=10)

    email_frame = tk.Frame(form_frame)
    email_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(email_frame, text="Email kontaktowy").pack(anchor='center', padx=10)
    email_entry = tk.Entry(email_frame, width=30)
    email_entry.pack(anchor='w', pady=5, padx=10)

    # Dodatkowa ramka na datę rejestracji (YYYY-MM-DD)
    data_frame = tk.Frame(form_frame)
    data_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(data_frame, text="Data rejestracji (YYYY-MM-DD)").pack(anchor='center', padx=10)
    data_entry = tk.Entry(data_frame, width=30)
    data_entry.pack(anchor='w', pady=5, padx=10)

    przyciski_frame = tk.Frame(form_frame)
    przyciski_frame.pack(anchor='s', pady=10, padx=10, fill=tk.X)

    tk.Button(
        przyciski_frame,
        text="Dodaj pacjenta",
        command=dodaj_pacjenta
    ).pack(side=tk.LEFT, pady=15, padx=5)

    tk.Button(
        przyciski_frame,
        text="Powrót do menu",
        command=powrot_do_menu
    ).pack(side=tk.LEFT, pady=15, padx=5)


def tworzenie_formularza_lekarz(form_frame, powrot_do_menu, tytul_label):
    def dodaj_lekarza():
        try:
            #Walidacja imienia
            imie_value = imie_entry.get().strip()
            if not imie_value.isalpha():
                messagebox.showerror("Błąd", "Imię może zawierać tylko litery.")
                return

            #Walidacja nazwiska
            nazwisko_value = nazwisko_entry.get().strip()
            if not nazwisko_value.isalpha():
                messagebox.showerror("Błąd", "Nazwisko może zawierać tylko litery.")
                return

            #Walidacja specjalizacji (jeżeli chcemy tylko litery)
            specjalizacja_value = specjalizacja_entry.get().strip()
            # jeśli dopuszczamy np. spacje (np. "Chirurg dziecięcy"),
            # można użyć np. re.match(r'^[A-Za-z\s]+$', specjalizacja_value)
            if not specjalizacja_value.isalpha():
                messagebox.showerror("Błąd", "Specjalizacja może zawierać tylko litery.")
                return

            #Walidacja numeru telefonu (int)
            try:
                numer_telefonu = int(telefon_entry.get().strip())
            except ValueError:
                messagebox.showerror("Błąd", "Podano nieprawidłowy numer telefonu (musi być liczbą).")
                return

            #Walidacja adresu e-mail
            email_input = email_entry.get().strip()
            pattern_email = r'^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$'
            if not re.match(pattern_email, email_input):
                messagebox.showerror("Błąd", "Niepoprawny adres mail!")
                return

            #Walidacja lat doświadczenia (int)
            try:
                lat_doswiadczenia_value = int(lat_doswiadczenia_entry.get().strip())
            except ValueError:
                messagebox.showerror("Błąd", "Lata doświadczenia muszą być liczbą całkowitą.")
                return

            #Walidacja pensji (float)
            try:
                pensja_value = float(pensja_entry.get().strip())
            except ValueError:
                messagebox.showerror("Błąd", "Pensja musi być liczbą zmiennoprzecinkową.")
                return

            #Pobranie ostatniego lekarza i wyliczenie nowego ID (int)
            ostatni_lekarz = baza["lekarze"].find_one(sort=[("_id", -1)])
            if ostatni_lekarz is not None:
                nowe_id = ostatni_lekarz["_id"] + 1
            else:
                nowe_id = 1

            #Tworzymy słownik nowego lekarza
            nowy_lekarz = {
                "_id": nowe_id,
                "imie": imie_value,
                "nazwisko": nazwisko_value,
                "specjalizacja": specjalizacja_value,
                "numer_telefonu": numer_telefonu,
                "email": email_input,  # już zwalidowany
                "lat_doswiadczenia": lat_doswiadczenia_value,
                "pensja": pensja_value,
                "dostepnosc": dostepnosc_var.get(),
            }

            #Zapisujemy do bazy
            baza["lekarze"].insert_one(nowy_lekarz)
            messagebox.showinfo("Sukces", f"Dodano lekarza z ID = {nowe_id}!")

        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się dodać lekarza: {e}")

    #UI (jak wcześniej)
    tytul_label.config(text="Kolekcja: lekarze")

    tk.Label(form_frame, text="Dodaj lekarza", font=("Arial", 12, "bold")).pack(anchor='nw', pady=5)

    imie_frame = tk.Frame(form_frame)
    imie_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(imie_frame, text="Imię").pack(anchor='center', padx=10)
    imie_entry = tk.Entry(imie_frame, width=30)
    imie_entry.pack(anchor='w', pady=5, padx=10)

    nazwisko_frame = tk.Frame(form_frame)
    nazwisko_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(nazwisko_frame, text="Nazwisko").pack(anchor='center', padx=10)
    nazwisko_entry = tk.Entry(nazwisko_frame, width=30)
    nazwisko_entry.pack(anchor='w', pady=5, padx=10)

    specjalizacja_frame = tk.Frame(form_frame)
    specjalizacja_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(specjalizacja_frame, text="Specjalizacja").pack(anchor='center', padx=10)
    specjalizacja_entry = tk.Entry(specjalizacja_frame, width=30)
    specjalizacja_entry.pack(anchor='w', pady=5, padx=10)

    telefon_frame = tk.Frame(form_frame)
    telefon_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(telefon_frame, text="Numer telefonu").pack(anchor='center', padx=10)
    telefon_entry = tk.Entry(telefon_frame, width=30)
    telefon_entry.pack(anchor='w', pady=5, padx=10)

    email_frame = tk.Frame(form_frame)
    email_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(email_frame, text="Email").pack(anchor='center', padx=10)
    email_entry = tk.Entry(email_frame, width=30)
    email_entry.pack(anchor='w', pady=5, padx=10)

    lat_doswiadczenia_frame = tk.Frame(form_frame)
    lat_doswiadczenia_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(lat_doswiadczenia_frame, text="Lata doświadczenia").pack(anchor='center', padx=10)
    lat_doswiadczenia_entry = tk.Entry(lat_doswiadczenia_frame, width=30)
    lat_doswiadczenia_entry.pack(anchor='w', pady=5, padx=10)

    pensja_frame = tk.Frame(form_frame)
    pensja_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(pensja_frame, text="Pensja").pack(anchor='center', padx=10)
    pensja_entry = tk.Entry(pensja_frame, width=30)
    pensja_entry.pack(anchor='w', pady=5, padx=10)

    dostepnosc_var = tk.BooleanVar()
    tk.Checkbutton(form_frame, text="Dostępny", variable=dostepnosc_var).pack(anchor='w', pady=5, padx=10)

    tk.Button(form_frame, text="Dodaj lekarza", command=dodaj_lekarza).pack(anchor='w', pady=10, padx=20)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=20)


def tworzenie_formularza_wizyta(form_frame, powrot_do_menu, tytul_label):
    def dodaj_wizyte():
        try:
            pacjent_id = int(pacjent_id_entry.get())
            lekarz_id = int(lekarz_id_entry.get())
            data_wizyty = data_wizyty_entry.get()
            czas_trwania = int(czas_trwania_entry.get())
            koszt = float(koszt_entry.get())
            choroba = choroba_entry.get()
            objawy = [x.strip() for x in objawy_entry.get().split(',')]

            nowa_wizyta = {
                "pacjent_id": pacjent_id,
                "lekarz_id": lekarz_id,
                "data_wizyty": data_wizyty,
                "czas_trwania": czas_trwania,
                "koszt": koszt,
                "choroba": choroba,
                "objawy": objawy
            }

            baza["wizyty"].insert_one(nowa_wizyta)
            messagebox.showinfo("Sukces", "Dodano wizytę!")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się dodać wizyty: {e}")

    tytul_label.config(text="Kolekcja: wizyta")

    tk.Label(form_frame, text="Dodaj wizytę", font=("Arial", 12, "bold")).pack(anchor='nw', pady=5)

    pacjent_id_frame = tk.Frame(form_frame)
    pacjent_id_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(pacjent_id_frame, text="ID Pacjenta (liczba)").pack(anchor='center', padx=10)
    pacjent_id_entry = tk.Entry(pacjent_id_frame, width=30)
    pacjent_id_entry.pack(anchor='w', pady=5, padx=10)

    lekarz_id_frame = tk.Frame(form_frame)
    lekarz_id_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(lekarz_id_frame, text="ID Lekarza (liczba)").pack(anchor='center', padx=10)
    lekarz_id_entry = tk.Entry(lekarz_id_frame, width=30)
    lekarz_id_entry.pack(anchor='w', pady=5, padx=10)

    data_wizyty_frame = tk.Frame(form_frame)
    data_wizyty_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(data_wizyty_frame, text="Data wizyty (format: YYYY-MM-DD)").pack(anchor='center', padx=10)
    data_wizyty_entry = tk.Entry(data_wizyty_frame, width=30)
    data_wizyty_entry.pack(anchor='w', pady=5, padx=10)

    czas_trwania_frame = tk.Frame(form_frame)
    czas_trwania_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(czas_trwania_frame, text="Czas trwania (minuty)").pack(anchor='center', padx=10)
    czas_trwania_entry = tk.Entry(czas_trwania_frame, width=30)
    czas_trwania_entry.pack(anchor='w', pady=5, padx=10)

    koszt_frame = tk.Frame(form_frame)
    koszt_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(koszt_frame, text="Koszt wizyty").pack(anchor='center', padx=10)
    koszt_entry = tk.Entry(koszt_frame, width=30)
    koszt_entry.pack(anchor='w', pady=5, padx=10)

    choroba_frame = tk.Frame(form_frame)
    choroba_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(choroba_frame, text="Choroba").pack(anchor='w', padx=10)
    choroba_entry = tk.Entry(choroba_frame, width=30)
    choroba_entry.pack(anchor='w', pady=5, padx=10)

    objawy_frame = tk.Frame(form_frame)
    objawy_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(objawy_frame, text="Objawy (rozdzielone przecinkami)").pack(anchor='w', padx=10)
    objawy_entry = tk.Entry(objawy_frame, width=40)
    objawy_entry.pack(anchor='w', pady=5, padx=10)

    tk.Button(form_frame, text="Dodaj wizytę", command=dodaj_wizyte).pack(anchor='w', pady=10, padx=20)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=20)