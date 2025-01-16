import tkinter as tk
from tkinter import messagebox
from auth import logowanie, rejestracja
from forms_dodaj import (
    tworzenie_formularza_pacjent,
    tworzenie_formularza_lekarz,
    tworzenie_formularza_wizyta
)
from forms_usun import (
    wyswietl_formularz_usun_pacjent,
    wyswietl_formularz_usun_lekarz,
    wyswietl_formularz_usun_wizyta
)
from forms_wyszukaj import (
    wyswietl_formularz_wyszukaj_pacjent,
    wyswietl_formularz_wyszukaj_lekarz,
    wyswietl_formularz_wyszukaj_wizyta
)

def dodaj_przycisk_wyjscia(okno):
    wyjscie_frame = tk.Frame(okno, bg="#f0f0f0")
    wyjscie_frame.pack(anchor='ne', padx=10, pady=5)

    przycisk_wyjscie = tk.Button(
        wyjscie_frame,
        text="Wyjście",
        command=okno.destroy,
        bg="#ff6666",
        fg="white",
        font=("Arial", 10, "bold"),
        bd=2,
        relief="groove",
        padx=10, pady=5
    )
    przycisk_wyjscie.pack()

obecna_zakladka = None
tytul_label = None
aplikacja_glowna = None
form_frame = None
zakladki = None
przyciski_zakladek = []

def pokaz_aplikacje(rola):
    global aplikacja_glowna, form_frame, zakladki, tytul_label, przyciski_zakladek

    aplikacja_glowna = tk.Tk()
    aplikacja_glowna.title(f"Przychodnia - {rola}")

    # Ustawiamy większe okno, tak aby było wystarczająco miejsca
    aplikacja_glowna.geometry('400x800')

    # Dodajemy przycisk wyjścia w prawym górnym rogu
    dodaj_przycisk_wyjscia(aplikacja_glowna)

    # Główna ramka aplikacji
    form_frame = tk.Frame(aplikacja_glowna)
    form_frame.pack(pady=20, padx=20, anchor='nw')

    # Tytuł aktualnej sekcji
    tytul_label = tk.Label(form_frame, text="Wybierz zakładkę z poniższego menu.", font=("Arial", 12, "bold"))
    tytul_label.pack(anchor='nw', pady=10)

    # Sekcja z zakładkami
    zakladki = tk.Frame(aplikacja_glowna)
    zakladki.pack(anchor='nw', padx=20, pady=10)

    # Przyciski zakładek
    przyciski_zakladek.clear()

    if rola == "admin":
        przyciski_zakladek.append(tk.Button(zakladki, text="Dodaj", width=12, command=lambda: zmien_zakladke("dodaj")))
        przyciski_zakladek.append(tk.Button(zakladki, text="Usuń", width=12, command=lambda: zmien_zakladke("usun")))
        przyciski_zakladek.append(tk.Button(zakladki, text="Wyszukaj", width=12, command=lambda: zmien_zakladke("wyszukaj")))
    elif rola == "user":
        przyciski_zakladek.append(tk.Button(zakladki, text="Wyszukaj", width=12, command=lambda: zmien_zakladke("wyszukaj")))

    # Dodanie przycisków do interfejsu
    for przycisk in przyciski_zakladek:
        przycisk.pack(side=tk.LEFT, padx=10, anchor='nw')

    aplikacja_glowna.mainloop()
def zmien_zakladke(zakladka):
    global obecna_zakladka
    obecna_zakladka = zakladka

    # Ukrycie przycisków (znikają z ekranu)
    for przycisk in przyciski_zakladek:
        przycisk.pack_forget()

    # Usuwanie wszystkich widgetów z form_frame oprócz tytul_label
    for widget in form_frame.winfo_children():
        if widget != tytul_label:
            widget.destroy()

    # Aktualizujemy tytuł i wyświetlamy odpowiednią zawartość
    if zakladka == "dodaj":
        tytul_label.config(text="Dodawanie danych")
        wyswietl_formularz_dodaj()
    elif zakladka == "usun":
        tytul_label.config(text="Usuwanie danych")
        wyswietl_formularz_usun()
    elif zakladka == "wyszukaj":
        tytul_label.config(text="Wyszukiwanie danych")
        wyswietl_formularz_wyszukaj()

def powrot_do_menu():

    #Przywraca główny widok (zakładki + tytuł), czyli to samo, co widzimy zaraz po zalogowaniu.

    # Usuwamy wszystkie widgety poza tytul_label
    for widget in form_frame.winfo_children():
        if widget != tytul_label:
            widget.destroy()

    # Ponownie pokazujemy przyciski zakładek
    for przycisk in przyciski_zakladek:
        przycisk.pack(side=tk.LEFT, padx=10, anchor='nw')

    # Ustawiamy napis
    tytul_label.config(text="Wybierz zakładkę z poniższego menu.")

def wyswietl_formularz_dodaj():

    #Formularz wyboru kolekcji, do której dodajemy dane.

    global kolekcja_var, kolekcja_label
    kolekcja_var = tk.StringVar(value="pacjenci")

    kolekcja_label = tk.Label(form_frame, text="Wybierz z listy, gdzie chcesz dodać dane.")
    kolekcja_label.pack(anchor='nw', pady=5)

    kolekcja_menu = tk.OptionMenu(form_frame, kolekcja_var, "pacjenci", "lekarze", "wizyta",
                                  command=aktualizuj_tekst_kolekcji)
    kolekcja_menu.pack(anchor='nw', pady=5)

    tk.Button(form_frame, text="Uruchom formularz",command=lambda: zmien_kolekcje(kolekcja_var.get())).pack(pady=10, anchor='nw')
    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(pady=10, anchor='nw')

def aktualizuj_tekst_kolekcji(kolekcja):
    kolekcja_label.config(text=f"Dodajesz dane do kolekcji: {kolekcja}")

def zmien_kolekcje(kolekcja):
    # Usuwamy wszystkie istniejące widgety z form_frame poza tytul_label
    for widget in form_frame.winfo_children():
        if widget != tytul_label:
            widget.destroy()

    # W zależności od wybranej kolekcji, otwieramy odpowiedni formularz
    if kolekcja == "pacjenci":
        tworzenie_formularza_pacjent(form_frame, powrot_do_menu, tytul_label)
    elif kolekcja == "lekarze":
        tworzenie_formularza_lekarz(form_frame, powrot_do_menu, tytul_label)
    elif kolekcja == "wizyta":
        tworzenie_formularza_wizyta(form_frame, powrot_do_menu, tytul_label)

def wyswietl_formularz_usun():
    """
    Formularz wyboru kolekcji do usunięcia danych.
    """
    global usun_kolekcja_var, usun_kolekcja_label

    usun_kolekcja_var = tk.StringVar(value="pacjenci")

    usun_kolekcja_label = tk.Label(form_frame, text="Wybierz kolekcję, z której chcesz usunąć rekord.")
    usun_kolekcja_label.pack(anchor='nw', pady=5)

    usun_kolekcja_menu = tk.OptionMenu(form_frame, usun_kolekcja_var, "pacjenci", "lekarze", "wizyta",
                                       command=aktualizuj_tekst_kolekcji_usun)
    usun_kolekcja_menu.pack(anchor='nw', pady=5)

    tk.Button(form_frame, text="Otwórz formularz usuwania",
              command=lambda: zmien_kolekcje_usun(usun_kolekcja_var.get())).pack(pady=10, anchor='nw')

    tk.Button(form_frame, text="Powrót do menu", command=powrot_do_menu).pack(pady=10, anchor='nw')

def aktualizuj_tekst_kolekcji_usun(kolekcja):
    usun_kolekcja_label.config(text=f"Usuwasz dane z kolekcji: {kolekcja}")

def zmien_kolekcje_usun(kolekcja):
    for widget in form_frame.winfo_children():
        if widget != tytul_label:
            widget.destroy()

    if kolekcja == "pacjenci":
        wyswietl_formularz_usun_pacjent(form_frame, powrot_do_menu, tytul_label)
    elif kolekcja == "lekarze":
        wyswietl_formularz_usun_lekarz(form_frame, powrot_do_menu, tytul_label)
    elif kolekcja == "wizyta":
        wyswietl_formularz_usun_wizyta(form_frame, powrot_do_menu, tytul_label)

def wyswietl_formularz_wyszukaj():
    """
    Główny formularz wyboru kolekcji do wyszukiwania.
    """
    global wyszukaj_kolekcja_var, wyszukaj_kolekcja_label

    wyszukaj_kolekcja_var = tk.StringVar(value="pacjenci")

    wyszukaj_kolekcja_label = tk.Label(form_frame, text="Wybierz kolekcję, w której chcesz wyszukać dane.")
    wyszukaj_kolekcja_label.pack(anchor='nw', pady=5)

    wyszukaj_kolekcja_menu = tk.OptionMenu(
        form_frame,
        wyszukaj_kolekcja_var,
        "pacjenci", "lekarze", "wizyta",
        command=aktualizuj_tekst_kolekcji_wyszukaj
    )
    wyszukaj_kolekcja_menu.pack(anchor='nw', pady=5)

    tk.Button(form_frame,text="Otwórz formularz wyszukiwania",command=lambda: zmien_kolekcje_wyszukaj(wyszukaj_kolekcja_var.get())).pack(pady=10, anchor='nw')

    tk.Button(form_frame,text="Powrót do menu",command=powrot_do_menu).pack(pady=10, anchor='nw')

def aktualizuj_tekst_kolekcji_wyszukaj(kolekcja):
    wyszukaj_kolekcja_label.config(text=f"Wyszukujesz w kolekcji: {kolekcja}")

def zmien_kolekcje_wyszukaj(kolekcja):
    for widget in form_frame.winfo_children():
        if widget != tytul_label:
            widget.destroy()

    if kolekcja == "pacjenci":
        wyswietl_formularz_wyszukaj_pacjent(form_frame, powrot_do_menu, tytul_label)
    elif kolekcja == "lekarze":
        wyswietl_formularz_wyszukaj_lekarz(form_frame, powrot_do_menu, tytul_label)
    elif kolekcja == "wizyta":
        wyswietl_formularz_wyszukaj_wizyta(form_frame, powrot_do_menu, tytul_label)

if __name__ == "__main__":
    aplikacja = tk.Tk()
    aplikacja.title("Logowanie - Przychodnia")

    # Zwiększamy rozmiar okna logowania
    aplikacja.geometry('400x350')

    # Dodajemy przycisk wyjścia w prawym górnym rogu
    dodaj_przycisk_wyjscia(aplikacja)

    # Ramka logowania
    logowanie_frame = tk.Frame(aplikacja)
    logowanie_frame.pack(pady=20)

    tk.Label(logowanie_frame, text="Login", font=("Arial", 10, "bold")).pack()
    login_entry = tk.Entry(logowanie_frame, width=25)
    login_entry.pack(pady=5)

    tk.Label(logowanie_frame, text="Hasło", font=("Arial", 10, "bold")).pack()
    haslo_entry = tk.Entry(logowanie_frame, show="*", width=25)
    haslo_entry.pack(pady=5)

    # przekazujemy parametry do funkcji logowanie
    tk.Button(logowanie_frame,text="Zaloguj się",width=20,command=lambda: logowanie(login_entry, haslo_entry, aplikacja, pokaz_aplikacje)).pack(pady=10)

    # przejście do rejestracji
    def przejdz_do_rejestracji():
        logowanie_frame.pack_forget()
        rejestracja_frame.pack(pady=20)

    tk.Button(logowanie_frame,text="Zarejestruj się",width=20,command=przejdz_do_rejestracji).pack(pady=5)

    # Ramka rejestracji
    rejestracja_frame = tk.Frame(aplikacja)

    tk.Label(rejestracja_frame, text="Login", font=("Arial", 10, "bold")).pack()
    login_rejestracja_entry = tk.Entry(rejestracja_frame, width=25)
    login_rejestracja_entry.pack(pady=5)

    tk.Label(rejestracja_frame, text="Hasło", font=("Arial", 10, "bold")).pack()
    haslo_rejestracja_entry = tk.Entry(rejestracja_frame, show="*", width=25)
    haslo_rejestracja_entry.pack(pady=5)

    tk.Label(rejestracja_frame, text="Powtórz hasło", font=("Arial", 10, "bold")).pack()
    haslo2_rejestracja_entry = tk.Entry(rejestracja_frame, show="*", width=25)
    haslo2_rejestracja_entry.pack(pady=5)

    def zarejestruj_i_powrot():
        rejestracja(login_rejestracja_entry, haslo_rejestracja_entry, haslo2_rejestracja_entry)
        przejdz_do_logowania()

    tk.Button(rejestracja_frame,text="Zarejestruj",width=20,command=zarejestruj_i_powrot).pack(pady=10)

    def przejdz_do_logowania():
        rejestracja_frame.pack_forget()
        logowanie_frame.pack(pady=20)

    tk.Button(rejestracja_frame,text="Powrót",width=20,command=przejdz_do_logowania).pack(pady=5)

    aplikacja.mainloop()