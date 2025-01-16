import re
import hashlib
from pymongo import MongoClient
from bson import ObjectId

def get_database():
    klient = MongoClient("mongodb://localhost:27017/")
    return klient["przychodniaDB"]

def waliduj_email(email):
    #Przykładowa walidacja e-maila przy pomocy wyrażenia regularnego.

    wzorzec = r'^[a-zA-Z]+@[a-zA-Z]+\.(pl|com|edu|org)$'
    if re.match(wzorzec, email):
        return True
    return False

def haszuj_haslo(haslo):

    #Funkcja do hashowania hasła algorytmem SHA-256.

    return hashlib.sha256(haslo.encode()).hexdigest()