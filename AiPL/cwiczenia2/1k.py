import random #biblioteka potrzebna do losowania liczb

##losowanie totolotka
totolotek = [] #tablica zapisujaca wyniki losowania totolotka

while len(totolotek) < 6: #petla wykonywana do momentu kiedy totolotek bedzie mial 6 roznych liczb
    byl = 0 #zminna byl aby zobaczyc czy liczba sie powtarza, co losowanie zaklad
    t = random.randint(1, 49) #losowanie liczby od 1 do 49
    for i in range(len(totolotek)): #petla dzialajaca tyle razy ile obecnie ma dlugosc totolotek
        if t == totolotek[i]: #jezeli obecnie wylosowana liczba jest rowna którejkolwiek z liczb juz wylosowanych wchodzimy do tego warunku
            byl = 1 #ustawiamy ze byla ta liczba
            break #wychodzimy z petli
    if byl == 0: #sprawdzamy czy byl ten element
        totolotek.append(t) #jezeli nie bylo dodajemy element wylosowany do tablicy totolotek

totolotek.sort() #sortujemy totolotek - nie musimy tego robic, ale latwiej sie sprawdza poprawnosc algorytmu dzieki temu
print(totolotek) #tez nie powinnismy tego wyswietlac, ale zeby sie dalo sprawdzic wsyztsko to zostawiam

##tworzenie kuponu
kupon = [] #stworzenie listy zapisujacej liczby na kuponie

while len(kupon) < 6: #petla wykonywana dopoki kupon nie ma 6 liczb
    byl = 0 #analogicznie do tego w losowaniu
    t = int(input("podaj liczbe z zakresu 1-49 ")) #prosimu uzytkownika o wpisanie liczby
    if t > 49 or t < 1: #sprawdzamy czy uzytkownik jest debilem i wpisal liczbe spoza zakresu
        print("liczba spoza zakresu") #jezeli jest trzeba mu to powiedziec
        continue #continue sluzy do pominiecia wszystkich rzeczy ktorre sa dalej w tej petli, dzieki czemu skracamy dzialanie kodu - czyli tak jakny przenosimy sie znowu pod while
    for i in range(len(kupon)): #ta petla tez patrzy czy uzytkownik jest glupi, dziala na tej samej zasadzie co przy losowaniu totka
        if t == kupon[i]:
            byl = 1
            print("podana wartosc jest juz w kuponie")
            break
    if byl == 0: #to samo co przy totku
        kupon.append(t)

kupon.sort() #sortujemy kupon - tez nie wymagane, ale jest łatwiej sprawdzać
print(kupon) #wyświetlamy kupon - ten sam case co wyżej

## porownanie kuponu z totolotkiem

odgadniete = 0 #licznik tego ile liczb jest odgadniętych

for i in range(len(kupon)): #petla działająca tyle razy ile długości ma kupon - w teorii może być po prostu 6 napisane zamiast tego len
    for j in range(len(totolotek)): #to samo co w linijce wyzej
        if kupon[i] == totolotek[j]: #sprawdzamy czy od i z kuponu jest rowna po kolei każdej liczbie z totka
            odgadniete+=1 #jezeli jest to dodajemy o 1 licznik
            break #i jezeli tu już się weszło to po prostu nie sprawdzamy kolejnych liczb z totka, bo wiadomo, że się nie powtarzają


print(odgadniete)