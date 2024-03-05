def xd(liczba):
    warunek = 0 #zmienna prawda/falsz do zakonczenia petli
    while warunek == 0: #dopoki nasz warunek sie nie spelni wykonujemy petle
        n = liczba #przypisujemy liczbe do n, aby zapisac jej orginalna wartosc
        m= 0 #m dajemy jako 0
        while liczba >0: #dopoki liczba wieksza od 0 - w tej petli bedziemy odwracali liczbe
            m= m*10 # mnozymy dotychczasowe m razy 10 - w algorytmie bedziemy przesuwali kolejne cyfry w lewo przez mnożenie przez 10
            m+= liczba%10 #dodajemy reszte dzielenia z 10 z liczby do m - czyli dodajemy ostatnia cyfre liczby do m, w ktorej wczesniejsze cyfry przesunelismy w lewo w linijce wyzej
            liczba = liczba//10 #dzieliomy liczbe calkowicei przez 10, czyli tak jakby usuwamy z niej ostatnia cyfre
        if m ==n: #sprawdzamy czy m(liczba odwrocona) jest rowna n - liczbie orginalnej - jezeli sa takie same to sa palindromem:D
            warunek = 1 # ustawiamy ze warunek sie spelnil zeby wywalic petle
            return 1
        liczba = m+n #ustawiamy nowa liczbe na sume m i n
        if liczba > 1000000000:
            return 0
            print(liczba)
        #tego w algorytmie na zajecia nie powinno byc, ale zeby algorytm wyswietlal jakas odpowiedz to wyswietlamy sume m i n, aby sprawodzic czy git działą
f