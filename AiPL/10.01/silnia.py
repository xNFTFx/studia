liczba = 5

## iteracyjnie

def silnia_iteracyjnie(liczba):
    wynik = 1
    for i in range(1, liczba+1):
        wynik *=i
    return wynik

print(silnia_iteracyjnie(liczba))

## rekurencyjnie

def silnia_rekurencyjnie(liczba):
    if liczba<2:
        return 1
    else:
        return liczba * silnia_rekurencyjnie(liczba-1)

print(silnia_rekurencyjnie(liczba))