## zadeklarowanie wartości wspolczynnikow ze wzoru a*x^2 + b*x + c
a = 1
b = -3
c = 2

delta = b ** 2 - 4 * a * c #obliczenie delty - ** to w pythonie potegowanie

if delta < 0: # sprawdzamy wartosc delty
    print("brak rozwiazan") #chyba wiadomow czm :P
elif delta == 0: # elif to formalnie else pod ktorym jest kolejny warunek czyli if, akurat w pythonie tak można, wszedzie indziej trzeba poprostu zrobic if w else
    print( (-1)*b/(2*a)) #pokazanie wyniku dla delty = 0
else: # jezeli zadnen z powyzszych warunkow nie zostal spelniony
    print(((-1)*b + delta**(1/2))/(2*a), ((-1)*b - delta**(1/2))/(2*a)) #pokazanie wynikow dla delty > 0, zapis dleta **(1/2) to pierwiastek, tylko w pythonie zeby to lepiej zapisac trzeba miec bibliteke dodatkowo pobrana. Ale na aipl można to wszytko zapisac noramlnie a nie po informatycznemu :P
