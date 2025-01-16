import tkinter as tk
from tkinter import messagebox

# Zakładamy, że db_uzytkowe.py jest w tym samym folderze,
# więc importujemy funkcje z modułu
from db_uzytkowe import get_database, haszuj_haslo

baza = get_database()

def logowanie(login_entry, haslo_entry, aplikacja, pokaz_aplikacje):
    login = login_entry.get()
    haslo = haslo_entry.get()

    # Przykładowe loginy admina
    if login == "Patryk" and haszuj_haslo(haslo) == haszuj_haslo("Patryk508"):
        messagebox.showinfo("Sukces", "Zalogowano jako admin!")
        aplikacja.destroy()  # Zamykamy okno logowania
        pokaz_aplikacje("admin")
    elif login == "1" and haszuj_haslo(haslo) == haszuj_haslo("1"):
        messagebox.showinfo("Sukces", "Zalogowano jako admin!")
        aplikacja.destroy()  # Zamykamy okno logowania
        pokaz_aplikacje("admin")
    else:
        # Logowanie jako zwykły użytkownik (po sprawdzeniu w kolekcji "uzytkownicy")
        uzytkownik = baza["uzytkownicy"].find_one({
            "login": login,
            "haslo": haszuj_haslo(haslo)
        })
        if uzytkownik:
            messagebox.showinfo("Sukces", "Zalogowano jako użytkownik!")
            aplikacja.destroy()  # Zamykamy okno logowania
            pokaz_aplikacje("user")
        else:
            messagebox.showerror("Błąd", "Niepoprawny login lub hasło!")

def rejestracja(login_entry, haslo_entry, haslo2_entry):
    login = login_entry.get()
    haslo = haslo_entry.get()
    haslo2 = haslo2_entry.get()

    if haslo != haslo2:
        messagebox.showerror("Błąd", "Hasła muszą być takie same!")
        return

    if baza["uzytkownicy"].find_one({"login": login}):
        messagebox.showerror("Błąd", "Login już istnieje!")
        return

    hashed_password = haszuj_haslo(haslo)
    nowy_uzytkownik = {
        "login": login,
        "haslo": hashed_password,
    }
    baza["uzytkownicy"].insert_one(nowy_uzytkownik)

    messagebox.showinfo("Sukces", "Zarejestrowano pomyślnie!")
