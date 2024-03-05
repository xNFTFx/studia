liczba = 745

def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba = int(liczba/10)
    return suma

def pierwiastek_cyfrowy(liczba):
    if liczba % 10 == liczba:
        return liczba
    else:
        return pierwiastek_cyfrowy(suma_cyfr(liczba))

pierwiastek_cyfrowy(liczba)