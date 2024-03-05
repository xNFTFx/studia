def doprowadzanie_do_cyfry(tab): #zadeklarowanie funkcji przyjmujaca argument tab
    while len(tab) > 1: #petla wykonywana do momentu az dlugosc tab bedzie rowna 1
        suma = 0 #zresetowanie wartosci zmiennej suma do 0
        for i in range(len(tab)): #petla idaca po kolei po cyfrach wyrazu
            suma+= int(tab[i]) #dodajemy kolejne cyfry tab do sumy
        tab = str(suma) #przypisujemy tab wartosc sumy w wersji stringa

    return tab #zwracamy tab w momencie gdy jego dlugosc wynosi 1 - jest cyfrą


if __name__ == "__main__": #polecenia wykonywane tylko gdy ten plik jest wykonywanym plikiem
    print(doprowadzanie_do_cyfry('12345')) # = 6
    print(doprowadzanie_do_cyfry('1111')) # = 4
    print(doprowadzanie_do_cyfry('999999')) # = 9