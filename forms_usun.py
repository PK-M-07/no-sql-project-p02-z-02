import tkinter as tk
from tkinter import messagebox
from bson import ObjectId
from db_uzytkowe import get_database

baza = get_database()


def wyswietl_formularz_usun_pacjent(form_frame, powrot_do_menu, tytul_label):
    tytul_label.config(text="Usuwanie z kolekcji: pacjenci")

    tk.Label(form_frame, text="Usuń pacjenta", font=("Arial", 12, "bold")).pack(anchor='nw', pady=10)

    id_frame = tk.Frame(form_frame)
    id_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(id_frame, text="ID pacjenta (liczba)").pack(anchor='w')
    pacjent_id_entry = tk.Entry(id_frame, width=30)
    pacjent_id_entry.pack(anchor='w')

    name_frame = tk.Frame(form_frame)
    name_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(name_frame, text="Imię pacjenta").pack(anchor='w')
    pacjent_imie_entry = tk.Entry(name_frame, width=30)
    pacjent_imie_entry.pack(anchor='w')

    tk.Label(name_frame, text="Nazwisko pacjenta").pack(anchor='w')
    pacjent_nazwisko_entry = tk.Entry(name_frame, width=30)
    pacjent_nazwisko_entry.pack(anchor='w')

    def usun_pacjenta():
        id_val = pacjent_id_entry.get().strip()
        imie_val = pacjent_imie_entry.get().strip()
        nazwisko_val = pacjent_nazwisko_entry.get().strip()

        # PRZYPADEK 1: ID + imię + nazwisko
        if id_val and imie_val and nazwisko_val:
            try:
                obiekt_id = int(id_val)
            except ValueError:
                messagebox.showerror("Błąd", "ID pacjenta musi być liczbą całkowitą.")
                return
            try:
                wynik = baza["pacjenci"].delete_one({
                    "_id": obiekt_id,
                    "imie": imie_val,
                    "nazwisko": nazwisko_val
                })
                if wynik.deleted_count > 0:
                    messagebox.showinfo("Sukces",
                                        f"Usunięto pacjenta (ID: {id_val}, imię: {imie_val}, nazwisko: {nazwisko_val}).")
                else:
                    messagebox.showinfo("Info",
                                        "Nie znaleziono pacjenta o podanych danych (ID, imię, nazwisko).")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się usunąć pacjenta: {e}")

        # PRZYPADEK 2: Tylko ID
        elif id_val and not (imie_val or nazwisko_val):
            try:
                obiekt_id = int(id_val)
            except ValueError:
                messagebox.showerror("Błąd", "ID pacjenta musi być liczbą całkowitą.")
                return

            try:
                wynik = baza["pacjenci"].delete_one({"_id": obiekt_id})
                if wynik.deleted_count > 0:
                    messagebox.showinfo("Sukces", f"Usunięto pacjenta o ID: {id_val}")
                else:
                    messagebox.showinfo("Info", f"Nie znaleziono pacjenta o ID: {id_val}")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się usunąć pacjenta: {e}")

        # PRZYPADEK 3: Tylko imię i nazwisko
        elif (imie_val and nazwisko_val) and not id_val:
            try:
                wynik = baza["pacjenci"].delete_many({
                    "imie": imie_val,
                    "nazwisko": nazwisko_val
                })
                if wynik.deleted_count > 0:
                    messagebox.showinfo("Sukces",
                                        f"Usunięto {wynik.deleted_count} pacjent(ów) o imieniu {imie_val} i nazwisku {nazwisko_val}.")
                else:
                    messagebox.showinfo("Info",
                                        "Nie znaleziono pacjenta o podanych danych (imię, nazwisko).")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się usunąć pacjenta: {e}")
        else:
            messagebox.showerror("Błąd",
                                 "Podaj ID pacjenta lub (imię i nazwisko), albo wszystkie trzy dane.")

    tk.Button(form_frame, text="Usuń pacjenta", command=usun_pacjenta).pack(anchor='w', pady=10, padx=10)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=10)


def wyswietl_formularz_usun_lekarz(form_frame, powrot_do_menu, tytul_label):
    tytul_label.config(text="Usuwanie z kolekcji: lekarze")

    tk.Label(form_frame, text="Usuń lekarza", font=("Arial", 12, "bold")).pack(anchor='nw', pady=10)

    id_frame = tk.Frame(form_frame)
    id_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(id_frame, text="ID lekarza (ObjectId)").pack(anchor='w')
    lekarz_id_entry = tk.Entry(id_frame, width=30)
    lekarz_id_entry.pack(anchor='w')

    name_frame = tk.Frame(form_frame)
    name_frame.pack(anchor='w', pady=5, padx=10)
    tk.Label(name_frame, text="Imię lekarza").pack(anchor='w')
    lekarz_imie_entry = tk.Entry(name_frame, width=30)
    lekarz_imie_entry.pack(anchor='w')

    tk.Label(name_frame, text="Nazwisko lekarza").pack(anchor='w')
    lekarz_nazwisko_entry = tk.Entry(name_frame, width=30)
    lekarz_nazwisko_entry.pack(anchor='w')

    def usun_lekarza():
        id_val = lekarz_id_entry.get().strip()
        imie_val = lekarz_imie_entry.get().strip()
        nazwisko_val = lekarz_nazwisko_entry.get().strip()

        if id_val:
            try:
                obiekt_id = ObjectId(id_val)
            except Exception as e:
                messagebox.showerror("Błąd", f"ID lekarza musi być poprawnym ObjectId! Szczegóły: {e}")
                return

            try:
                wynik = baza["lekarze"].delete_one({"_id": obiekt_id})
                if wynik.deleted_count > 0:
                    messagebox.showinfo("Sukces", f"Usunięto lekarza o ID: {id_val}")
                else:
                    messagebox.showinfo("Info", f"Nie znaleziono lekarza o ID: {id_val}")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się usunąć lekarza: {e}")
        else:
            # Jeśli nie podano ID, sprawdzamy imię i nazwisko
            if imie_val and nazwisko_val:
                try:
                    wynik = baza["lekarze"].delete_many({
                        "imie": imie_val,
                        "nazwisko": nazwisko_val
                    })
                    if wynik.deleted_count > 0:
                        messagebox.showinfo("Sukces", f"Usunięto {wynik.deleted_count} lekarz(y).")
                    else:
                        messagebox.showinfo("Info", "Nie znaleziono lekarza o podanych danych.")
                except Exception as e:
                    messagebox.showerror("Błąd", f"Nie udało się usunąć lekarza: {e}")
            else:
                messagebox.showerror("Błąd", "Podaj ID lekarza lub (imię i nazwisko).")

    tk.Button(form_frame, text="Usuń lekarza", command=usun_lekarza).pack(anchor='w', pady=10, padx=10)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=10)


def wyswietl_formularz_usun_wizyta(form_frame, powrot_do_menu, tytul_label):
    tytul_label.config(text="Usuwanie z kolekcji: wizyta")

    tk.Label(form_frame, text="Usuń wizytę", font=("Arial", 12, "bold")).pack(anchor='nw', pady=10)

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

    def usun_wizyte():
        pacjent_val = wiz_pacjent_id_entry.get().strip()
        lekarz_val = wiz_lekarz_id_entry.get().strip()

        filtr = {}
        if pacjent_val:
            try:
                filtr["pacjent_id"] = int(pacjent_val)
            except ValueError:
                filtr["pacjent_id"] = pacjent_val
        if lekarz_val:
            try:
                filtr["lekarz_id"] = int(lekarz_val)
            except ValueError:
                filtr["lekarz_id"] = lekarz_val

        if not filtr:
            messagebox.showerror("Błąd", "Podaj co najmniej ID pacjenta lub ID lekarza.")
            return

        try:
            wynik = baza["wizyty"].delete_many(filtr)
            if wynik.deleted_count > 0:
                messagebox.showinfo("Sukces", f"Usunięto {wynik.deleted_count} wizyt(ę).")
            else:
                messagebox.showinfo("Info", "Nie znaleziono wizyt z podanymi kryteriami.")
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się usunąć wizyty: {e}")

    tk.Button(form_frame, text="Usuń wizytę", command=usun_wizyte).pack(anchor='w', pady=10, padx=10)
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(anchor='w', pady=10, padx=10)
