#zadeklarowanie wszystkich wartosci potrzebnych w ciagu
a = 2 #wyraz a0
q = 4 #iloczyn ciagu
n = 3 #liczba wyrazow ktore chcemy w ciagu

ciag = [] #deklarujemy ciag

ciag.append(a) #dodajemy pierwszy wyraz do ciagu
suma = a #ustawiamy sume jako a

if n<1: #sprawdzamy czy ciag ma jakikolwiek wyraz
    print("brak ciagu") #jezeli nie to piszemy ze nie istnieje ciag
else: #no jezeli ciag istnieje
    wyraz = a #ustawiamy wyraz, ktory bedzuemy obecnie obliczali dla normalnego ciagu
    for i in range(1, n): #petla dzialajaca tyle razy ile jest dlugosc ciagu -1, bo pierwszy wyraz zadeklarowalismy wczesniej
        wyraz = wyraz *q # tworzymy kolejny wyraz ciagu
        suma +=wyraz #
        ciag.append(suma)
    print(ciag)