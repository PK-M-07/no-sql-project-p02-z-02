//Generator danych

const bazaDanych = 'Projekt';
const kolekcja = 'Katastrofy';

use(bazaDanych);

const wspolrzedneMiast = {
  'Warszawa': { szerokosc: 52.2298, dlugosc: 21.0118 },
  'Kraków': { szerokosc: 50.0647, dlugosc: 19.9450 },
  'Gdańsk': { szerokosc: 54.3520, dlugosc: 18.6466 },
  'Wrocław': { szerokosc: 51.1079, dlugosc: 17.0385 },
  'Poznań': { szerokosc: 52.4084, dlugosc: 16.9342 },
  'Rzeszów': { szerokosc: 50.0413, dlugosc: 21.9990 },
  'Nowy Jork': { szerokosc: 40.7128, dlugosc: -74.0060 },
  'Londyn': { szerokosc: 51.5074, dlugosc: -0.1278 },
  'Paryż': { szerokosc: 48.8566, dlugosc: 2.3522 },
  'Tokio': { szerokosc: 35.6762, dlugosc: 139.6503 },
  'Sydney': { szerokosc: -33.8688, dlugosc: 151.2093 },
  'Rio de Janeiro': { szerokosc: -22.9068, dlugosc: -43.1729 },
  'Moskwa': { szerokosc: 55.7558, dlugosc: 37.6173 },
  'Pekin': { szerokosc: 39.9042, dlugosc: 116.4074 },
  'Berlin': { szerokosc: 52.5200, dlugosc: 13.4050 },
  'Los Angeles': { szerokosc: 34.0522, dlugosc: -118.2437 },
  'Dubaj': { szerokosc: 25.276987, dlugosc: 55.296249 },
  'Kair': { szerokosc: 30.0444, dlugosc: 31.2357 },
  'Seul': { szerokosc: 37.5665, dlugosc: 126.9780 },
  'Meksyk': { szerokosc: 19.4326, dlugosc: -99.1332 },
  'Singapur': { szerokosc: 1.3521, dlugosc: 103.8198 },
  'Bombaj': { szerokosc: 19.0760, dlugosc: 72.8777 },
  'Cape Town': { szerokosc: -33.9249, dlugosc: 18.4241 },
  'Lagos': { szerokosc: 6.5244, dlugosc: 3.3792 },
  'Dżakarta': { szerokosc: -6.2088, dlugosc: 106.8456 },
  'Buenos Aires': { szerokosc: -34.6037, dlugosc: -58.3816 },
  'Hong Kong': { szerokosc: 22.3193, dlugosc: 114.1694 },
  'Stambuł': { szerokosc: 41.0082, dlugosc: 28.9784 },
  'Bangkok': { szerokosc: 13.7563, dlugosc: 100.5018 },
  'Kuala Lumpur': { szerokosc: 3.1390, dlugosc: 101.6869 },
  'São Paulo': { szerokosc: -23.5505, dlugosc: -46.6333 },
  'Lima': { szerokosc: -12.0464, dlugosc: -77.0428 },
  'Madryt': { szerokosc: 40.4168, dlugosc: -3.7038 },
  'Toronto': { szerokosc: 43.65107, dlugosc: -79.347015 },
  'Rzym': { szerokosc: 41.9028, dlugosc: 12.4964 },
  'Lima': { szerokosc: -12.0464, dlugosc: -77.0428 },
  'Karaczi': { szerokosc: 24.8607, dlugosc: 67.0011 },
  'Nairobi': { szerokosc: -1.286389, dlugosc: 36.817223 },
  'Dhaka': { szerokosc: 23.8103, dlugosc: 90.4125 }
};

function generujLosowaKatastrofe() {
  const typyKatastrof = ['Pożar', 'Powódź', 'Trzęsienie ziemi', 'Huragan', 'Osuwisko'];
  const miasta = Object.keys(wspolrzedneMiast); 

  const losowyTyp = typyKatastrof[Math.floor(Math.random() * typyKatastrof.length)];
  const losoweMiasto = miasta[Math.floor(Math.random() * miasta.length)];

  const { szerokosc, dlugosc } = wspolrzedneMiast[losoweMiasto];

  const startDate = new Date(2000, 0, 1);
  const endDate = new Date(); 
  const losowaData = new Date(startDate.getTime() + Math.random() * (endDate.getTime() - startDate.getTime()));

  return {
    nazwa: `${losowyTyp} w ${losoweMiasto}`,
    data: losowaData,
    lokalizacja: {
      szerokosc: szerokosc, 
      dlugosc: dlugosc
    },
    opis: `Katastrofa typu ${losowyTyp} miała miejsce w ${losoweMiasto}.`
  };
}

const liczbaKatastrof = 50; 

for (let i = 0; i < liczbaKatastrof; i++) {
  const katastrofa = generujLosowaKatastrofe();
  db[kolekcja].insertOne(katastrofa);
}

print(`${liczbaKatastrof} losowych katastrof zostało dodanych do kolekcji '${kolekcja}'.`);


//Generator danych 2

const bazaDanych = 'Projekt';
const kolekcja = 'SluzbyRatownicze';

use(bazaDanych);

const miasta = [
  'Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Rzeszów', 'Nowy Jork', 'Londyn', 'Paryż', 'Tokio', 
  'Sydney', 'Rio de Janeiro', 'Moskwa', 'Pekin', 'Berlin', 'Los Angeles', 'Dubaj', 'Kair', 'Seul', 'Meksyk',
  'Singapur', 'Bombaj', 'Cape Town', 'Lagos', 'Dżakarta', 'Buenos Aires', 'Hong Kong', 'Stambuł', 'Bangkok',
  'Kuala Lumpur', 'São Paulo', 'Lima', 'Madryt', 'Toronto', 'Rzym', 'Karaczi', 'Nairobi', 'Dhaka'
];

const typySluzb = ['Straż Pożarna', 'Policja', 'Pogotowie Ratunkowe', 'Centrum Zarządzania Kryzysowego'];

function generujNumerKontaktowy() {
  return (
    Math.floor(100 + Math.random() * 900) + '-' +
    Math.floor(100 + Math.random() * 900) + '-' +
    Math.floor(100 + Math.random() * 900)
  );
}

function generujCzasReakcji() {
  const czasy = ['5 minut', '10 minut', '15 minut', '20 minut', '30 minut'];
  return czasy[Math.floor(Math.random() * czasy.length)];
}

function generujLiczbeRatownikow() {
  return Math.floor(Math.random() * 101);
}

function generujLosowaSluzbaRatownicza() {
  const miasto = miasta[Math.floor(Math.random() * miasta.length)];
  const typ = typySluzb[Math.floor(Math.random() * typySluzb.length)];

  return {
    name: `${typ} ${miasto}`,
    type: typ,
    contact: generujNumerKontaktowy(),
    responseTime: generujCzasReakcji(),
    liczbaRatownikow: generujLiczbeRatownikow()
  };
}

const liczbaSluzb = 50; 

for (let i = 0; i < liczbaSluzb; i++) {
  const sluzba = generujLosowaSluzbaRatownicza();
  db[kolekcja].insertOne(sluzba);
}

print(`${liczbaSluzb} losowych służb ratowniczych zostało dodanych do kolekcji '${kolekcja}'.`);
 
//Generator danych 3

const bazaDanych = 'Projekt';
const kolekcja = 'Aktualnosci';

use(bazaDanych);

const typyAlertow = ['Ostrzeżenie o powodzi', 'Ostrzeżenie o huraganie', 'Ostrzeżenie o trzęsieniu ziemi', 'Ostrzeżenie o pożarze', 'Alert o wypadku drogowym'];

const miasta = [
  'Warszawa', 'Kraków', 'Gdańsk', 'Wrocław', 'Poznań', 'Rzeszów', 'Nowy Jork', 'Londyn', 'Paryż', 'Tokio',
  'Sydney', 'Rio de Janeiro', 'Moskwa', 'Pekin', 'Berlin', 'Los Angeles', 'Dubaj', 'Kair', 'Seul', 'Meksyk',
  'Singapur', 'Bombaj', 'Cape Town', 'Lagos', 'Dżakarta', 'Buenos Aires', 'Hong Kong', 'Stambuł', 'Bangkok',
  'Kuala Lumpur', 'São Paulo', 'Lima', 'Madryt', 'Toronto', 'Rzym', 'Karaczi', 'Nairobi', 'Dhaka'
];

function generujDate() {
  const data = new Date();
  const rok = data.getFullYear();
  const miesiac = Math.floor(Math.random() * 12);
  const dzien = Math.floor(Math.random() * 28) + 1;
  const godzina = Math.floor(Math.random() * 24);
  const minuta = Math.floor(Math.random() * 60);

  return new Date(rok, miesiac, dzien, godzina, minuta);
}

function generujAlert() {
  const typAlertu = typyAlertow[Math.floor(Math.random() * typyAlertow.length)];
  const miasto = miasta[Math.floor(Math.random() * miasta.length)];

  return {
    data: generujDate(),
    typAlertu: typAlertu,
    lokalizacja: miasto,
    status: Math.random() > 0.5 ? 'Aktywny' : 'Zakończony',
    opis: `Alert dotyczący ${typAlertu.toLowerCase()} w mieście ${miasto}. Szczegóły: wkrótce.`,
  };
}

const liczbaAlertow = 50;

for (let i = 0; i < liczbaAlertow; i++) {
  const alert = generujAlert();
  db[kolekcja].insertOne(alert);
}

print(`${liczbaAlertow} losowych alertów zostało dodanych do kolekcji '${kolekcja}'.`);