## zadanie 1
def szukanie_nwd(a,b): #definiuję funkcję do szukania NWD. KOd bazuje na zoptymalizowanym algorytmie Euklidesa
    while(b!=0): #pętla wykonywana dopóki b będzie się różniło od 0
        t = b #tworzymy zmienną pomocniczą, służącą do zamiany liczb
        b = a%b #przypisujemy nową wartość zmiennej b równą a modulo b (reszta z dzielenia)
        a = t #przypisanie wartości zmiennej t do zmiennej a
    return a #zwracamy wartość zmiennej a w momencie gdy zmienna b osiągnie wartość 0

if __name__ == '__main__':
    print(szukanie_nwd(1, 1000)) #  = 1
    print(szukanie_nwd(24, 28)) # = 4
    print(szukanie_nwd(999, 111)) # = 111