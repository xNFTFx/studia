import random #import biblioteki potrzebnej do losowania liczb

zetony = 5 #ustawienie zetonow na 5

while zetony <10 and zetony >0: #petla dopki zetony sa w zakresie (0,10)
    zgadywana = random.randint(1,3) #wylosowanie liczby z zakresu 1-3
    odp = 1 #poproszenie uzytkownika od liczbe z zakresu 1-3, w teorii pownno sie jeszcze zrobid warunek jezeli uzytkownik da liczbe spoza zakresu ale mi sie nie chce
    if odp == zgadywana: #jezeli zgadl
        print("zgadles") #powiedzenie uzytkownikowi ze zgadl
        zetony +=2 #dodanie 2 do zetonow
    else:   #zezeli nie zgadl
        zetony-=1 #odjecie zetonu
        print("nie zgadles") #pokazanie uzytkownikowi ze nie zgadl
    print("masz ", zetony, " zetonow") #pokazanie uzytkownikowi ile ma zetonow

if zetony == 0: #juz poza petla jezeli zetony = 0
    print("przegrales") #pokazujesz ze uztkownik przegral
else: # no i jezeli ma wiecej zetonow niz 0, czyli ma tez wiecej od 10 bo inaczej petla nie wylaczy sie
    print("wygrales") #pokazanie uzytkownikowi ze wygral giere