liczba = 6 #wybranie liczby

wynik = 0 #stworzenie zmiennej pomocniczej zliczajacej sume dzielnikow

for i in range(1, liczba//2+1): #petla wykonywana do polowy liczby - nie ma dzielnikow wiekszych niz pol liczby, warunek liczba//2 +1 wymuszony jest tym ze warunek w pythonie zawsze jest <, a my musimy sprawdzic <= niz polowa
    if liczba%i == 0: #sprawdzamy czy modulo z liczby i kolejnych liczb jest rowne 0 - nie ma reszty z dzielenia obu liczb
        wynik +=i # jezeli i jest dzielnikiem dodajemy je do sumy dzielnikow


if wynik == liczba: #sprawdzamy czy suma dzielnikow jest rowna liczbie
    print("liczba doskonala") # jezeli tak to klasa B)
else:
    print("liczba niedoskonala") # a jezeli nie to dupa