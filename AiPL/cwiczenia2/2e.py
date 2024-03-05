wyraz = 'k a j a k' #podanie wyrazu - normalnie bez spacji, ale inaczej nie chce dzialac - problem z danymi w pythonie
wyraz.split() #pythonowe naprawienie bledow - nie patrzcie

palindrom = 1 #zmienna pomocnicza prawda/falsz - czy wyraz jest palindromem - myslimy pozytywnie ze jest ;)
for i in range(len(wyraz)//2): #petla do polowy dlugosci wyrazu
    if wyraz[i] != wyraz[len(wyraz)-i-1]: # jezeli sprawdzany element i symetryczny do niego sa od siebie rozne
        print("nie jest palindromem") # to wyswuetlamy ze nie jest
        palindrom = 0 #ustawiamy wartosc false
        break # i wywalamy petle
if palindrom ==1: # no i tu sprawdzamy czy nasze zalozenie ze jest palindromem przetrwalo petle
    print("palindrom") # jezeli przetrwalo to wyswietlamy ze git