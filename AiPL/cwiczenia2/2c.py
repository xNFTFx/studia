import random #biblioteka do losowania

tab = [] #tablica w ktorej bedziemy zapisywali liczby

#liczniki do poszczegolnych przypadkow
parzyste = 0
nieparzyste = 0
ujemne = 0
dodatnie = 0

for i in range(20): #petla na 20 liczb
    tab.append(random.randint(-100, 100)) #dodanie do tabeli liczby z zakresu [-100, 100]
    if tab[i] % 2 ==0:# jezeli reszta z dzielenia liczby przez 2 jest rowna 0 => jest parzysta
        parzyste+=1 # zwiekszamy licznik parzystych o 1
    else: #jezeli wczesniejszy warunek jest nieprawdziwy to liczba jest nieparzysta
        nieparzyste+=1 #zwiekszamy licznik nieparzystych
    if tab[i] > 0: #sprawdzamy czy dodatna liczba jest wieksza od 0
        dodatnie+=1 #zwiekszamy licznik dodatnich
    elif tab[i]<0: #niestety 0 nie jest ani dodatnie, ani ujemne wiec trzeba zrobic warunek czy jest <0
        ujemne+=1 #zwiekszamy licznik ujemnych


print(tab) #wyswietlamy tablice liczb zeby sprawdzic czy program sie nie jebnal - normalnie nie wyswietlamy
print(parzyste, nieparzyste, dodatnie, ujemne) #no i pokazanie wynikow