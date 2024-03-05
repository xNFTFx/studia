## zadeklarowanie wyrazu
wyraz = 'd u p a' #  normalnie bez spacji pomiedzy literami, ale tu cos nie dziala, wiec musi byc tak
wyraz = wyraz.split() # wymagane w pythonie, normalnie pomijamy ten krok

for i in range(int(len(wyraz)//2)): #petla wykonywana 1/2 rzy ile ma dlugosc wyrazu, dla nieparzystej liczby liter, wykonujemy wynik zaokraglamy w dol(w kodzie do tego uzylem dzieleia calkowitego)
    t = wyraz[i] #przypisanie wartosci elementu i do zmiennej pomocniczej t
    wyraz[i] = wyraz[len(wyraz)-i - 1] #przypisanie wartosci elementu ostatniego - i(-1 z powodu ze tablice indeksowane sa od 0) do pierwszego
    wyraz[len(wyraz)-i-1] = t #przypisanie wartosci t do ostatniego elemetnu -i

print(wyraz) # wyswietlenie wyrazu odwroconego