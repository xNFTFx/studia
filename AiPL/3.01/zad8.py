def liczba_rozklad(liczba):
    tablica = []
    dzielnik = 10
    while liczba > 0:
        tablica.append(int((liczba %dzielnik)*10/dzielnik))
        liczba -= liczba %dzielnik
        dzielnik *=10
    return tablica

def mnożenie_czynnikow(tab):
    suma = 0
    for i in range(len(tab)):
        suma += tab[i]*tab[i]
    return suma

def zawiera(tab, liczba):
    for i in range(len(tab)):
        if liczba == tab[i]:
            return True
    return False



tablica = []
liczba = 4

while True:
    print(liczba)
    print(tablica)
    if mnożenie_czynnikow(liczba_rozklad(liczba)) ==1:
        print("liczba wesoła")
        break
    liczba = mnożenie_czynnikow(liczba_rozklad(liczba))
    if zawiera(tablica, liczba) == True:
        print("nie jest wesola")
        break
    tablica.append(liczba)