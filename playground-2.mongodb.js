use('szpitalDB');

db.getCollection('pacjenci').insertMany([
  { 
    'imie': 'Marta Zielińska', 
    'wiek': 29, 
    'wzrost': 168.5, 
    'ubezpieczony': true, 
    'choroby': ['nadciśnienie'], 
    'dane_kontaktowe': { 'telefon': '123456789', 'email': 'marta.z@example.com' },
    'data_rejestracji': new Date('2024-05-01T10:30:00Z'),
    'ostatnia_wizyta': new Date('2024-12-20T15:00:00Z') 
  },
  { 
    'imie': 'Jan Kowalski', 
    'wiek': 45, 
    'wzrost': 175.3, 
    'ubezpieczony': false, 
    'choroby': ['cukrzyca', 'astma'], 
    'dane_kontaktowe': { 'telefon': '987654321', 'email': 'jan.k@example.com' },
    'data_rejestracji': new Date('2024-02-14T09:00:00Z'),
    'ostatnia_wizyta': new Date('2024-11-10T11:00:00Z')
  }
]);

db.getCollection('lekarze').insertMany([
  { 
    'imie': 'Dr. Adam Kowalski', 
    'lata_doswiadczenia': 15, 
    'pensja': 15000.00, 
    'dostepny': true, 
    'specjalizacje': ['Kardiologia'], 
    'dane_kontaktowe': { 'telefon': '987654321', 'email': 'adam.k@example.com' },
    'data_zatrudnienia': new Date('2010-05-01T09:00:00Z'),
    'ostatnia_zmiana': new Date('2024-12-15T08:00:00Z')
  },
  { 
    'imie': 'Dr. Anna Nowak', 
    'lata_doswiadczenia': 8, 
    'pensja': 12000.00, 
    'dostepny': true, 
    'specjalizacje': ['Neurologia'], 
    'dane_kontaktowe': { 'telefon': '321654987', 'email': 'anna.n@example.com' },
    'data_zatrudnienia': new Date('2016-03-01T10:00:00Z'),
    'ostatnia_zmiana': new Date('2024-12-17T08:30:00Z')
  }
]);

db.getCollection('wizyta').insertMany([
  { 
    'id_pacjenta': { $oid: "507f191e810c19729de860ea" },  
    'id_lekarza': { $oid: "507f191e810c19729de860eb" },  
    'czas_trwania_minuty': 30, 
    'koszt': 200.00, 
    'czy_zakonczona': false, 
    'objawy': ['ból w klatce piersiowej', 'duszności'],
    'szczegoly': { 'diagnostyka': 'Nadciśnienie tętnicze', 'recepta': 'Leki na nadciśnienie' },
    'data_wizyty': new Date('2024-12-15T14:30:00Z'),
    'data_utworzenia': new Date('2024-12-10T09:00:00Z')
  },
  { 
    'id_pacjenta': { $oid: "507f191e810c19729de860ec" },  
    'id_lekarza': { $oid: "507f191e810c19729de860ed" },  
    'czas_trwania_minuty': 45, 
    'koszt': 250.00, 
    'czy_zakonczona': false, 
    'objawy': ['ból głowy', 'zawroty głowy'],
    'szczegoly': { 'diagnostyka': 'Migrena', 'recepta': 'Leki przeciwbólowe' },
    'data_wizyty': new Date('2024-12-18T11:00:00Z'),
    'data_utworzenia': new Date('2024-12-10T10:00:00Z')
  }
]);
