import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Projekt"]

collections = ["Zdarzenia", "Katastrofy", "SluzbyRatownicze"]

selected_collection = db[collections[0]]

def change_collection(new_collection):
    global selected_collection
    selected_collection = db[new_collection]
    create_form(new_collection)
    messagebox.showinfo("Informacja", f"Wybrano kolekcję: {new_collection}")

def create_form(collection_name):
    for widget in form_frame.winfo_children():
        widget.destroy()

    global entry_id, entry_data, entry_typZdarzenia, entry_miasto
    global entry_sluzby_name, entry_sluzby_type, entry_sluzby_contact
    global entry_sluzby_responseTime, entry_sluzby_liczbaRatownikow
    global entry_opis, entry_status, entry_nazwa, entry_lokalizacja_szerokosc
    global entry_lokalizacja_dlugosc

    entry_id = tk.Entry(form_frame, width=30)
    entry_data = tk.Entry(form_frame, width=30)
    entry_typZdarzenia = tk.Entry(form_frame, width=30)
    entry_miasto = tk.Entry(form_frame, width=30)
    entry_sluzby_name = tk.Entry(form_frame, width=30)
    entry_sluzby_type = tk.Entry(form_frame, width=30)
    entry_sluzby_contact = tk.Entry(form_frame, width=30)
    entry_sluzby_responseTime = tk.Entry(form_frame, width=30)
    entry_sluzby_liczbaRatownikow = tk.Entry(form_frame, width=30)
    entry_opis = tk.Entry(form_frame, width=30)
    entry_status = tk.Entry(form_frame, width=30)
    entry_nazwa = tk.Entry(form_frame, width=30)
    entry_lokalizacja_szerokosc = tk.Entry(form_frame, width=30)
    entry_lokalizacja_dlugosc = tk.Entry(form_frame, width=30)

    if collection_name == "Zdarzenia":
        tk.Label(form_frame, text="_id").pack()
        entry_id.pack()

        tk.Label(form_frame, text="Data").pack()
        entry_data.pack()

        tk.Label(form_frame, text="Typ Zdarzenia").pack()
        entry_typZdarzenia.pack()

        tk.Label(form_frame, text="Miasto").pack()
        entry_miasto.pack()

        tk.Label(form_frame, text="SluzbyZaangazowane").pack()
        tk.Label(form_frame, text="  Nazwa").pack()
        entry_sluzby_name.pack()

        tk.Label(form_frame, text="  Typ").pack()
        entry_sluzby_type.pack()

        tk.Label(form_frame, text="  Kontakt").pack()
        entry_sluzby_contact.pack()

        tk.Label(form_frame, text="  Czas odpowiedzi").pack()
        entry_sluzby_responseTime.pack()

        tk.Label(form_frame, text="  Liczba ratowników").pack()
        entry_sluzby_liczbaRatownikow.pack()

        tk.Label(form_frame, text="Opis").pack()
        entry_opis.pack()

        tk.Label(form_frame, text="Status").pack()
        entry_status.pack()

    elif collection_name == "Katastrofy":
        tk.Label(form_frame, text="_id").pack()
        entry_id.pack()

        tk.Label(form_frame, text="Nazwa").pack()
        entry_nazwa.pack()

        tk.Label(form_frame, text="Data").pack()
        entry_data.pack()

        tk.Label(form_frame, text="Lokalizacja").pack()
        tk.Label(form_frame, text="  Szerokość").pack()
        entry_lokalizacja_szerokosc.pack()

        tk.Label(form_frame, text="  Długość").pack()
        entry_lokalizacja_dlugosc.pack()

        tk.Label(form_frame, text="Opis").pack()
        entry_opis.pack()

    elif collection_name == "SluzbyRatownicze":
        tk.Label(form_frame, text="_id").pack()
        entry_id.pack()

        tk.Label(form_frame, text="Nazwa").pack()
        entry_sluzby_name.pack()

        tk.Label(form_frame, text="Typ").pack()
        entry_sluzby_type.pack()

        tk.Label(form_frame, text="Kontakt").pack()
        entry_sluzby_contact.pack()

        tk.Label(form_frame, text="Czas odpowiedzi").pack()
        entry_sluzby_responseTime.pack()

        tk.Label(form_frame, text="Liczba ratowników").pack()
        entry_sluzby_liczbaRatownikow.pack()

    tk.Button(form_frame, text="Dodaj", command=add_data).pack(pady=10)

def add_data():
    collection_name = selected_collection.name
    document = {}

    try:
        if collection_name == "Zdarzenia":
            document = {
                "_id": entry_id.get(),
                "data": entry_data.get(),
                "typZdarzenia": entry_typZdarzenia.get(),
                "Miasto": entry_miasto.get(),
                "SluzbyZaangazowane": {
                    "name": entry_sluzby_name.get(),
                    "type": entry_sluzby_type.get(),
                    "contact": entry_sluzby_contact.get(),
                    "responseTime": int(entry_sluzby_responseTime.get()),
                    "liczbaRatownikow": int(entry_sluzby_liczbaRatownikow.get()),
                },
                "opis": entry_opis.get(),
                "status": entry_status.get(),
            }
        elif collection_name == "Katastrofy":
            document = {
                "_id": entry_id.get(),
                "nazwa": entry_nazwa.get(),
                "data": entry_data.get(),
                "lokalizacja": {
                    "szerokosc": float(entry_lokalizacja_szerokosc.get()),
                    "dlugosc": float(entry_lokalizacja_dlugosc.get()),
                },
                "opis": entry_opis.get(),
            }
        elif collection_name == "SluzbyRatownicze":
            document = {
                "_id": entry_id.get(),
                "name": entry_sluzby_name.get(),
                "type": entry_sluzby_type.get(),
                "contact": entry_sluzby_contact.get(),
                "responseTime": int(entry_sluzby_responseTime.get()),
                "liczbaRatownikow": int(entry_sluzby_liczbaRatownikow.get()),
            }

        selected_collection.insert_one(document)
        messagebox.showinfo("Sukces", "Dane zostały dodane!")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {e}")

def exit_app():
    app.quit()

app = tk.Tk()
app.title("MongoDB GUI")
app.geometry("600x600")

tk.Label(app, text="Wybierz kolekcję").pack(pady=10)
selected_collection_var = tk.StringVar(app)
selected_collection_var.set(collections[0])  # Domyślnie pierwsza kolekcja

collection_menu = tk.OptionMenu(app, selected_collection_var, *collections, command=change_collection)
collection_menu.pack()

form_frame = tk.Frame(app)
form_frame.pack(pady=20)

entry_id = tk.Entry(form_frame, width=30)
entry_data = tk.Entry(form_frame, width=30)
entry_typZdarzenia = tk.Entry(form_frame, width=30)
entry_miasto = tk.Entry(form_frame, width=30)
entry_sluzby_name = tk.Entry(form_frame, width=30)
entry_sluzby_type = tk.Entry(form_frame, width=30)
entry_sluzby_contact = tk.Entry(form_frame, width=30)
entry_sluzby_responseTime = tk.Entry(form_frame, width=30)
entry_sluzby_liczbaRatownikow = tk.Entry(form_frame, width=30)
entry_opis = tk.Entry(form_frame, width=30)
entry_status = tk.Entry(form_frame, width=30)
entry_nazwa = tk.Entry(form_frame, width=30)
entry_lokalizacja_szerokosc = tk.Entry(form_frame, width=30)
entry_lokalizacja_dlugosc = tk.Entry(form_frame, width=30)

create_form(collections[0])

exit_button = tk.Button(app, text="Wyjście", command=exit_app, bg="red", fg="white", font=("Arial", 12))
exit_button.place(x=550, y=10)

app.mainloop()