import tkinter as tk
from tkinter import messagebox
from db_uzytkowe import get_database
from bson import ObjectId

baza = get_database()


def wyswietl_formularz_wyszukaj_pacjent(form_frame, powrot_do_menu, tytul_label):
    tytul_label.config(text="Wyszukiwanie w kolekcji: pacjenci")

    tk.Label(form_frame, text="Wyszukaj pacjentów", font=("Arial", 12, "bold")).pack(anchor='nw', pady=10)

    id_frame = tk.Frame(form_frame)
    id_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(id_frame, text="ID pacjenta (liczba)").pack(anchor='w')
    pacjent_id_entry = tk.Entry(id_frame, width=30)
    pacjent_id_entry.pack(anchor='w')

    imie_frame = tk.Frame(form_frame)
    imie_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(imie_frame, text="Imię pacjenta").pack(anchor='w')
    pacjent_imie_entry = tk.Entry(imie_frame, width=30)
    pacjent_imie_entry.pack(anchor='w')

    nazwisko_frame = tk.Frame(form_frame)
    nazwisko_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(nazwisko_frame, text="Nazwisko pacjenta").pack(anchor='w')
    pacjent_nazwisko_entry = tk.Entry(nazwisko_frame, width=30)
    pacjent_nazwisko_entry.pack(anchor='w')

    wyniki_text = tk.Text(form_frame, width=90, height=12)
    wyniki_text.pack(anchor='nw', padx=10, pady=10)

    def wyszukaj_pacjenta():
        query = {}
        id_val = pacjent_id_entry.get().strip()
        imie_val = pacjent_imie_entry.get().strip()
        nazwisko_val = pacjent_nazwisko_entry.get().strip()

        if id_val:
            try:
                query["_id"] = int(id_val)
            except ValueError:
                messagebox.showerror("Błąd", "ID pacjenta musi być liczbą całkowitą.")
                return
        if imie_val:
            query["imie"] = imie_val
        if nazwisko_val:
            query["nazwisko"] = nazwisko_val

        wyniki_text.delete('1.0', tk.END)

        try:
            wyniki = baza["pacjenci"].find(query)
            znaleziono_jakikolwiek = False
            for doc in wyniki:
                znaleziono_jakikolwiek = True
                pacjent_text = (
                    f"id_: {doc.get('_id')}\n"
                    f"Imię: {doc.get('imie')}\n"
                    f"Nazwisko: {doc.get('nazwisko')}\n"
                    f"Wiek: {doc.get('wiek')}\n"
                    f"Wzrost: {doc.get('wzrost')}\n"
                    f"Ubezpieczony: {doc.get('ubezpieczony')}\n"
                    f"Choroby: {doc.get('choroby')}\n"
                    f"Telefon: {doc.get('dane_kontaktowe', {}).get('telefon')}\n"
                    f"Email: {doc.get('dane_kontaktowe', {}).get('email')}\n"
                    f"Data rejestracji: {doc.get('data_rejestracji')}\n"
                    f"Ostatnia wizyta: {doc.get('ostatnia_wizyta')}\n"
                    "----------------------------------------\n"
                )
                wyniki_text.insert(tk.END, pacjent_text)

            if not znaleziono_jakikolwiek:
                wyniki_text.insert(tk.END, "Brak pasujących pacjentów.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił problem podczas wyszukiwania: {e}")

    tk.Button(form_frame, text="Szukaj", command=wyszukaj_pacjenta).pack(anchor='w', pady=10, padx=10)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=10)


def wyswietl_formularz_wyszukaj_lekarz(form_frame, powrot_do_menu, tytul_label):
    tytul_label.config(text="Wyszukiwanie w kolekcji: lekarze")

    tk.Label(form_frame, text="Wyszukaj lekarzy", font=("Arial", 12, "bold")).pack(anchor='nw', pady=10)

    id_frame = tk.Frame(form_frame)
    id_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(id_frame, text="ID lekarza (ObjectId)").pack(anchor='w')
    lekarz_id_entry = tk.Entry(id_frame, width=30)
    lekarz_id_entry.pack(anchor='w')

    imie_frame = tk.Frame(form_frame)
    imie_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(imie_frame, text="Imię lekarza").pack(anchor='w')
    lekarz_imie_entry = tk.Entry(imie_frame, width=30)
    lekarz_imie_entry.pack(anchor='w')

    nazwisko_frame = tk.Frame(form_frame)
    nazwisko_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(nazwisko_frame, text="Nazwisko lekarza").pack(anchor='w')
    lekarz_nazwisko_entry = tk.Entry(nazwisko_frame, width=30)
    lekarz_nazwisko_entry.pack(anchor='w')

    wyniki_text = tk.Text(form_frame, width=90, height=12)
    wyniki_text.pack(anchor='nw', padx=10, pady=10)

    def wyszukaj_lekarza():
        query = {}
        id_val = lekarz_id_entry.get().strip()
        imie_val = lekarz_imie_entry.get().strip()
        nazwisko_val = lekarz_nazwisko_entry.get().strip()

        if id_val:
            # Proba konwersji na ObjectId
            try:
                query["_id"] = ObjectId(id_val)
            except Exception:
                messagebox.showerror("Błąd", "Niepoprawne ID (ObjectId).")
                return
        if imie_val:
            query["imie"] = imie_val
        if nazwisko_val:
            query["nazwisko"] = nazwisko_val

        wyniki_text.delete('1.0', tk.END)

        try:
            wyniki = baza["lekarze"].find(query)
            znaleziono_jakikolwiek = False
            for doc in wyniki:
                znaleziono_jakikolwiek = True
                lekarz_text = (
                    f"id_: {doc.get('_id')}\n"
                    f"Imię: {doc.get('imie')}\n"
                    f"Nazwisko: {doc.get('nazwisko')}\n"
                    f"Specjalizacja: {doc.get('specjalizacja')}\n"
                    f"Numer telefonu: {doc.get('numer_telefonu')}\n"
                    f"Email: {doc.get('email')}\n"
                    f"Lata doświadczenia: {doc.get('lat_doswiadczenia')}\n"
                    f"Pensja: {doc.get('pensja')}\n"
                    f"Dostępny: {doc.get('dostepnosc')}\n"
                    "----------------------------------------\n"
                )
                wyniki_text.insert(tk.END, lekarz_text)

            if not znaleziono_jakikolwiek:
                wyniki_text.insert(tk.END, "Brak pasujących lekarzy.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił problem podczas wyszukiwania: {e}")

    tk.Button(form_frame, text="Szukaj", command=wyszukaj_lekarza).pack(anchor='w', pady=10, padx=10)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=10)


def wyswietl_formularz_wyszukaj_wizyta(form_frame, powrot_do_menu, tytul_label):
    tytul_label.config(text="Wyszukiwanie w kolekcji: wizyta")

    tk.Label(form_frame, text="Wyszukaj wizyty", font=("Arial", 12, "bold")).pack(anchor='nw', pady=10)

    wiz_pacjent_frame = tk.Frame(form_frame)
    wiz_pacjent_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(wiz_pacjent_frame, text="ID pacjenta").pack(anchor='w')
    wiz_pacjent_id_entry = tk.Entry(wiz_pacjent_frame, width=30)
    wiz_pacjent_id_entry.pack(anchor='w')

    wiz_lekarz_frame = tk.Frame(form_frame)
    wiz_lekarz_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(wiz_lekarz_frame, text="ID lekarza").pack(anchor='w')
    wiz_lekarz_id_entry = tk.Entry(wiz_lekarz_frame, width=30)
    wiz_lekarz_id_entry.pack(anchor='w')

    choroba_frame = tk.Frame(form_frame)
    choroba_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(choroba_frame, text="Choroba").pack(anchor='w')
    choroba_entry = tk.Entry(choroba_frame, width=30)
    choroba_entry.pack(anchor='w')

    wyniki_text = tk.Text(form_frame, width=90, height=12)
    wyniki_text.pack(anchor='nw', padx=10, pady=10)

    def wyszukaj_wizyte():
        query = {}
        pacjent_val = wiz_pacjent_id_entry.get().strip()
        lekarz_val = wiz_lekarz_id_entry.get().strip()
        choroba_val = choroba_entry.get().strip()

        if pacjent_val:
            try:
                query["pacjent_id"] = int(pacjent_val)
            except ValueError:
                query["pacjent_id"] = pacjent_val
        if lekarz_val:
            try:
                query["lekarz_id"] = int(lekarz_val)
            except ValueError:
                query["lekarz_id"] = lekarz_val
        if choroba_val:
            query["choroba"] = choroba_val

        wyniki_text.delete('1.0', tk.END)

        try:
            wyniki = baza["wizyty"].find(query)
            znaleziono_jakikolwiek = False
            for doc in wyniki:
                znaleziono_jakikolwiek = True
                wizyta_text = (
                    f"id_: {doc.get('_id')}\n"
                    f"pacjent_id: {doc.get('pacjent_id')}\n"
                    f"lekarz_id: {doc.get('lekarz_id')}\n"
                    f"data_wizyty: {doc.get('data_wizyty')}\n"
                    f"czas_trwania: {doc.get('czas_trwania')}\n"
                    f"koszt: {doc.get('koszt')}\n"
                    f"choroba: {doc.get('choroba')}\n"
                    f"objawy: {doc.get('objawy')}\n"
                    "----------------------------------------\n"
                )
                wyniki_text.insert(tk.END, wizyta_text)

            if not znaleziono_jakikolwiek:
                wyniki_text.insert(tk.END, "Brak pasujących wizyt.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił problem podczas wyszukiwania: {e}")

    tk.Button(form_frame, text="Szukaj", command=wyszukaj_wizyte).pack(anchor='w', pady=10, padx=10)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=10)
