tablica = [123, 32, 4, 423, 32, 33, 42, 32, 0, 3, 33, 44, 12, 9 , 5, 1, 2] # podanie tablicy losowych liczb, ktora bedziemy sprawdzac

#aby znalezc ciag potrzebujemy tylko dlugosc i index pierwszego wyrazu wiec bedzimy to zapisywali
index_pierwszego_w_ciagu = 0
dlugosc_ciagu = 1
# jednoczesnie zapisujemy rowniez wartosci maxymalnego ciagu
max_index_pierwszego_w_ciagu = 0
max_dlugosc_ciagu = 0

for i in range(1, len(tablica)): # petla od 2. wartosci w tablicy (o indeksie 1) do konca tablicy
    if tablica[i] < tablica[i-1]: # jezeli obecny element jest wiekszy od poprzedniego
        dlugosc_ciagu +=1 #zwiekszamy dlugosc obecnego ciagu
    else: #sprawdzamy w momencie przerwania ciagu
        if dlugosc_ciagu > max_dlugosc_ciagu: #sprawdzamy czy przed chwila zakonczony ciag jest tym najwiekszym
            max_dlugosc_ciagu = dlugosc_ciagu #jezeli jest przypisujemy jego wartosci wartosciom tego maksymalnego
            max_index_pierwszego_w_ciagu = index_pierwszego_w_ciagu
        index_pierwszego_w_ciagu = i #przypisujemy wartosci nowego ciagu - startujemy od obecnego elementu
        dlugosc_ciagu = 1 # resetujemy dlugosc na najmniejsza mozliwa czyli 1

print(max_index_pierwszego_w_ciagu, max_dlugosc_ciagu ) #wyswietlamy wartosci maksymalnego ciagu