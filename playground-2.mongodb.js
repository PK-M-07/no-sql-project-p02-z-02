  use('przychodniaDB');  // Ustawiamy bazę danych

  // Funkcja do losowego generowania imienia i nazwiska
  function losoweImie() {
    const imiona = [
      'Adam', 'Marta', 'Anna', 'Jan', 'Paweł', 'Karolina', 'Tomasz', 'Ewa', 
      'Piotr', 'Katarzyna', 'Patryk', 'Alicja', 'Damian', 'Beata', 'Grzegorz', 
      'Magdalena', 'Kamil', 'Dorota', 'Robert', 'Agnieszka', 'Łukasz', 'Natalia',
      'Joanna', 'Michał', 'Barbara', 'Maciej', 'Zofia', 'Wojciech', 'Małgorzata', 
      'Krystian'
    ];

    const nazwiska = [
      'Kowalski', 'Zielińska', 'Nowak', 'Jankowski', 'Wójcik', 'Lewandowski', 
      'Kaczmarek', 'Mazur', 'Woźniak', 'Styrczula', 'Król', 'Kubiak', 'Grabowski', 
      'Szymczak', 'Jaworski', 'Pietrzak', 'Czarnecki', 'Wieczorek', 'Głowacki', 
      'Sadowski', 'Zawadzki', 'Bąk', 'Sikora', 'Baran', 'Pawlak', 'Wróbel', 
      'Michalski', 'Dudek', 'Wiśniewski', 'Górski', 'Zieliński', 'Ostrowski', 
      'Lis', 'Domański'
    ];
    
    const imie = imiona[Math.floor(Math.random() * imiona.length)];
    const nazwisko = nazwiska[Math.floor(Math.random() * nazwiska.length)];
    return imie + ' ' + nazwisko;
  }

  // Funkcja do losowego generowania numeru telefonu
  function losowyTelefon() {
    return '5' + Math.floor(Math.random() * 1000000000).toString().padStart(9, '0');
  }

  // Funkcja do losowego generowania emaila
  function losowyEmail(imie, nazwisko) {
    const domeny = ['@gmail.com', '@yahoo.com', '@outlook.com', '@interia.pl', '@o2.pl', '@gazeta.pl'];
    return imie.toLowerCase() + '.' + nazwisko.toLowerCase() + domeny[Math.floor(Math.random() * domeny.length)];
  }

  // Funkcja do losowego generowania daty
  function losowaData(startYear, endYear) {
    const start = new Date(startYear, 0, 1);
    const end = new Date(endYear, 11, 31);
    return new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
  }

  // Funkcja do losowego wyboru choroby
  function losowaChoroba() {
    const choroby = [
      { nazwa: 'nadciśnienie', objawy: ['ból głowy', 'zmęczenie', 'zawroty głowy'] },
      { nazwa: 'cukrzyca', objawy: ['zmęczenie', 'wzmożone pragnienie', 'częste oddawanie moczu'] },
      { nazwa: 'astma', objawy: ['duszności', 'kaszel', 'wzmożona męczliwość'] },
      { nazwa: 'migrena', objawy: ['ból głowy', 'nudności', 'wymioty', 'zawroty głowy'] },
      { nazwa: 'grypa', objawy: ['gorączka', 'kaszel', 'ból gardła', 'zmęczenie'] },
      { nazwa: 'zapalenie płuc', objawy: ['duszności', 'kaszel', 'gorączka'] },
      { nazwa: 'problemy z sercem', objawy: ['kołatanie serca', 'bóle w klatce piersiowej'] },
      { nazwa: 'bóle stawów', objawy: ['ból stawów', 'sztywność'] },
      { nazwa: 'parkinson', objawy: ['drżenie rąk', 'sztywność', 'problemy z równowagą'] },
      { nazwa: 'nowotwór płuc', objawy: ['kaszel', 'duszności', 'krwioplucie'] },
      { nazwa: 'glejak', objawy: ['ból głowy', 'niedowład', 'wzmożona senność'] },
      { nazwa: 'Bolerioza', objawy: ['bóle stawów', 'wysypka', 'zmęczenie'] },
      { nazwa: 'jaskra', objawy: ['ból oczu', 'zaburzenia widzenia'] },
      { nazwa: 'obrzęk dna oka', objawy: ['ból oka', 'zaburzenia widzenia'] },
      { nazwa: 'chłoniak', objawy: ['powiększenie węzłów chłonnych', 'zmęczenie'] },
      { nazwa: 'Alzheimer', objawy: ['zaburzenia pamięci', 'dezorientacja', 'trudności w mówieniu'] },
      { nazwa: 'osteoporoza', objawy: ['bóle pleców', 'złamania kości'] },
      { nazwa: 'reumatoidalne zapalenie stawów', objawy: ['ból stawów', 'sztywność stawów'] },
      { nazwa: 'choroba wieńcowa', objawy: ['ból w klatce piersiowej', 'duszności', 'kołatanie serca'] },
      { nazwa: 'depresja', objawy: ['smutek', 'zmęczenie', 'problemy ze snem'] },
      { nazwa: 'grzybica', objawy: ['wysypka', 'swędzenie'] },
      { nazwa: 'bezsenność', objawy: ['problemy ze snem', 'zmęczenie'] },
      { nazwa: 'angina', objawy: ['ból gardła', 'trudności w przełykaniu'] },
      { nazwa: 'katar sienny', objawy: ['katar', 'kichanie', 'świąd oczu'] },
      { nazwa: 'zapalenie zatok', objawy: ['ból głowy', 'katar', 'bóle twarzy'] },
      { nazwa: 'choroba wrzodowa', objawy: ['ból brzucha', 'nudności', 'zgaga'] },
      { nazwa: 'rak skóry', objawy: ['wysypka', 'zmiany skórne'] },
      { nazwa: 'kolka nerkowa', objawy: ['ból pleców', 'bóle brzucha'] },
      { nazwa: 'kamica żółciowa', objawy: ['ból w prawym górnym kwadrancie brzucha', 'wymioty'] },
      { nazwa: 'choroba refluksowa', objawy: ['zgaga', 'kwasowy smak w ustach'] },
      { nazwa: 'grypa żołądkowa', objawy: ['biegunka', 'nudności', 'wymioty'] }
    ];

    return choroby[Math.floor(Math.random() * choroby.length)];
  }

  // Funkcja do losowego generowania czasu trwania wizyty
  function losowyCzasTrwania() {
    return Math.floor(Math.random() * 40) + 15; 
  }

  // Funkcja do losowego generowania kosztu wizyty
  function losowyKoszt() {
    return (Math.random() * (300 - 100) + 100).toFixed(2);  
  }

  // Funkcja przypisująca lekarza do wizyty na podstawie choroby
  function przypiszLekarzaDoWizyty(choroba) {
    const specjalizacjeMap = {
      'nadciśnienie': 'internista',
      'cukrzyca': 'internista',
      'astma': 'pulmonolog',
      'migrena': 'neurolog',
      'grypa': 'internista',
      'zapalenie płuc': 'pulmonolog',
      'problemy z sercem': 'kardiolog',
      'bóle stawów': 'reumatolog',
      'parkinson': 'neurolog',
      'nowotwór płuc': 'onkolog',
      'glejak': 'neurolog',
      'Bolerioza': 'internista',
      'jaskra': 'okulista',
      'obrzęk dna oka': 'okulista',
      'chłoniak': 'onkolog',
      'Alzheimer': 'neurolog',
      'osteoporoza': 'reumatolog',
      'reumatoidalne zapalenie stawów': 'reumatolog',
      'choroba wieńcowa': 'kardiolog',
      'depresja': 'psychiatra',
      'grzybica': 'dermatolog',
      'bezsenność': 'psychiatra',
      'angina': 'laryngolog',
      'katar sienny': 'alergolog',
      'zapalenie zatok': 'laryngolog',
      'choroba wrzodowa': 'gastroenterolog',
      'rak skóry': 'dermatolog',
      'kolka nerkowa': 'urolog',
      'kamica żółciowa': 'chirurg',
      'choroba refluksowa': 'gastroenterolog',
      'grypa żołądkowa': 'gastroenterolog'
    };

    const specjalizacja = specjalizacjeMap[choroba.nazwa];
    const lekarz = lekarze.find(lekarz => lekarz.specjalizacja === specjalizacja);
    
    return lekarz ? lekarz._id : null;
  }

  // Tworzymy pacjentów
  const pacjenci = [];
  for (let i = 0; i < 200; i++) {
    const imieNazwisko = losoweImie();
    const [imie, nazwisko] = imieNazwisko.split(' ');
    const choroba = losowaChoroba();
    const dataRejestracji = losowaData(2020, 2024);
    const ostatniaWizyta = losowaData(2023, 2024);
    
    // Sprawdzamy, czy data rejestracji pacjenta jest wcześniejsza niż ostatnia wizyta
    if (dataRejestracji > ostatniaWizyta) {
      continue; // Jeżeli nie, pomijamy tego pacjenta
    }

    pacjenci.push({
      '_id': i + 1, 
      'imie': imie,
      'nazwisko': nazwisko,
      'wiek': Math.floor(Math.random() * (80 - 18) + 18),  
      'wzrost': (Math.random() * (200 - 150) + 150).toFixed(1),  
      'ubezpieczony': Math.random() > 0.5,  
      'choroby': [choroba],
      'dane_kontaktowe': { 
        'telefon': losowyTelefon(), 
        'email': losowyEmail(imie, nazwisko)
      },
      'data_rejestracji': dataRejestracji,
      'ostatnia_wizyta': ostatniaWizyta
    });
  }

  // Tworzymy lekarzy
  const lekarze = [];
  const specjalizacje = [
    'internista', 'kardiolog', 'neurolog', 'ortopeda', 'chirurg', 'psychiatra', 
    'onkolog', 'dermatolog', 'endokrynolog', 'ginekolog', 'alergolog', 'pediatra',
    'okulista', 'laryngolog', 'reumatolog', 'gastroenterolog', 'pulmonolog', 'urolog'
  ];

  for (let i = 0; i < 50; i++) {
    const imieNazwisko = losoweImie();
    const [imie, nazwisko] = imieNazwisko.split(' ');
    const specjalizacja = specjalizacje[Math.floor(Math.random() * specjalizacje.length)];
    
    // Losowanie lat doświadczenia, pensji i dostępności
    const lataDoswiadczenia = Math.floor(Math.random() * 25) + 1; // Od 1 do 25 lat
    const pensja = (Math.random() * (15000 - 5000) + 5000).toFixed(2); // Pensja od 5000 do 15000
    const czyDostepny = Math.random() > 0.5; // Losowo true lub false

    lekarze.push({
      '_id': i + 1, 
      'imie': imie,
      'nazwisko': nazwisko,
      'specjalizacja': specjalizacja,
      'numer_telefonu': losowyTelefon(),
      'email': losowyEmail(imie, nazwisko),
      'lat_doswiadczenia': lataDoswiadczenia,
      'pensja': pensja,
      'dostepnosc': czyDostepny
    });
  }

  // Tworzymy wizyty
  const wizyty = [];
  for (let i = 0; i < 500; i++) {
    const pacjent = pacjenci[Math.floor(Math.random() * pacjenci.length)];
    const choroba = pacjent.choroby[Math.floor(Math.random() * pacjent.choroby.length)];
    const lekarzId = przypiszLekarzaDoWizyty(choroba);

    // Losowanie daty wizyty
    const dataWizyty = losowaData(2023, 2024);

    // Sprawdzamy, czy data wizyty jest późniejsza od ostatniej wizyty pacjenta
    if (dataWizyty < pacjent.ostatnia_wizyta) {
      continue; // Jeśli nie, pomijamy tę wizytę
    }

    wizyty.push({
      '_id': i + 1,
      'pacjent_id': pacjent._id,
      'lekarz_id': lekarzId,
      'data_wizyty': dataWizyty,
      'czas_trwania': losowyCzasTrwania(),
      'koszt': losowyKoszt(),
      'choroba': choroba.nazwa,
      'objawy': choroba.objawy
    });
  }

  db.pacjenci.insertMany(pacjenci);
  db.lekarze.insertMany(lekarze);
  db.wizyty.insertMany(wizyty);

  print('Wszystko zostało zapisane!');
