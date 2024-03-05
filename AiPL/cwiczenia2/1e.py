## dziwne zadanie
## dzielenie z resztą v. algorytm

# zadeklarowanie wartosci dzielnika i dzielnej
dzielna = 23
dzielnik = 4
wynik = 0 #zmienna pomocnicza wynik
reszta = 0 #zmienna pomocnicza reszta

if dzielnik == 0: #sprawdzenie czy dzielnik = 0
    print("nie da sie mnozyc przez 0") #wyswietlenie ze jest blad dla dzielnik = 0
else: # co robimy dla dzielnika roznego od 0
    while dzielna > dzielnik: #petla dopoki dzielna > dzielnik, dzielna bedzie zmniejszana
        dzielna = dzielna - dzielnik # odejmujemy dzielnik od dzielnej jezeli dzielna jest wieksza od dzielnika
        wynik +=1   # zwiekszamy wynik
    reszta = dzielna # wartosc ktora bedzie mniejsza niz dzielnik wsadzamy jako reszta

print(wynik, reszta) #wyswietlamy wynik i reszte

## dzielenie normalne v. algorytm
# doslownie to samo co wczesniej tylko zamiast reszty koncowke dzielimy i dostajemy ulamek i dodajemy do wyniku
dzielna = 23
dzielnik = 4
wynik = 0

if dzielnik == 0:
    print("nie da sie mnozyc przez 0")
else:
    while dzielna > dzielnik:
        dzielna = dzielna - dzielnik
        wynik +=1

wynik += dzielna/dzielnik

print(wynik)

## jak to sie normalnie robi
# po prostu dzielenie
dzielna = 23
dzielnik = 4
wynik = 0
reszta = 0

wynik = dzielna/dzielnik
print(wynik)

## z resztą typowo

wynik = dzielna // dzielnik #dzielnie calkowite
reszta = dzielna % dzielnik #modulo - zwracanie reszty z dzialania

print(wynik, reszta)