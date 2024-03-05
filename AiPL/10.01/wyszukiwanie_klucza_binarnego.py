tablica = [0,1,0,0,0,1,1,1,0,0,1,0,1,0,0]
klucz = [1, 0, 1]

for i in range(len(tablica)): #for(int i = 0; i<le; i++
    if tablica[i] == klucz[0]:
        nie = 0
        for j in   range(1, len(klucz)):
            if klucz[j] != tablica[i+j]:
                nie = 1
                break
        if nie == 0:
            print(i)

# int - liczby naturalne
# float - liczba zmiennoprzecinkowa
# bool - prawda/fałsz
#
