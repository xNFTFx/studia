limit = 100 ## sztuczne ograniczenie do której liczby chcemy sprawdzać potencjalne pierwiastki, stworzone aby program się zatrzymał

liczba = 1 ##zadeklasrowanie 1. liczby naturalnej

while liczba*liczba <= limit: ## petla dzialajaca dopoki mnozenie dwoch liczb bedzie mniejsze niz narzucony limit, dla tego algorytmu może być równiej użyte while True, działające w nieskończoność
    print(liczba*liczba) ## wypisanie kolejnych pierwiastkow
    liczba +=1 ## inkrementacja wartosci liczba - zwiekszenie o 1

##alternatywna wersja kodu - działająca w nieskończoność
#
#liczba = 1
#while True:
#   print(liczba *liczba)
#   liczba+=1