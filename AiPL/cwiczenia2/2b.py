liczba = int(input()) #wpisujemy pierwsza liczbe poza warunkiem
if liczba == 0: #sprawdzamy czy pierwsza liczba byla rowna 0
    print("koniec") #jezeli byla konczymy program
else: #jezeli byla rozna od 0...
    licznik = 0 # ustawiamy licznik liczb ktore wpiszemy na 0 - w petli na poczatku zwiekszamy wartosci a pozniej prosimy o nowa, wiec wartosc wpisana wczesniej tez bedzie uwzgledniona
    suma = 0    # ustawiamy sume na 0
    min = liczba # ustawiamy min i max na pierwzsa liczbe
    max = liczba
    while liczba != 0: #dopoki nie wpiszemy 0
        licznik+=1 # dodajemy 1 do licznika
        suma +=liczba #dodajemy ostatnia liczbe do sumy
        if liczba < min: #sprawdzamy czy obecna liczba jest mniejsza od dotychczasowej najmniejszej
            min = liczba #jezeli tak to zmieniamy najmniejsza
        if liczba > max: #to samo tylko z najwieksza
            max = liczba
        liczba = int(input()) #prosimy uzytkownika o nowa liczbe
    print(min, max, suma/licznik) # juz poza petla ;) pokazujemy wszystki wartosci wymagane w zadaniu
