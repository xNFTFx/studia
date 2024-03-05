liczba = 134134 #deklarujemy losowa liczbe

while liczba > 0: #petla dopoki liczba jest >0 - bedziemy zminiali wartosc liczby
    if liczba % 10 ==2: #sprawdzamy czy reszta z dzielenia liczby przez 10 to 2
        print("zawiera 2") #jezeli tak piszemy ze zawiera 2
        break #i przerywamy program
    #jezeli nie wchodzimy do tamtego warunku to idziemy dalej - nie ma else
    liczba = liczba//10 # dzielimy calkowicie liczbe prze 10 (tak jakby usuwamy ostatnia cyfre z liczby)