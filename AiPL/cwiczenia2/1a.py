## deklaracja wartości/mogą być też prośba o wczytanie - input
a = 3
b = 9
c = 4

max = 0 ## deklaracja pomocniczej zmiennej do zapisywania najwiekszej wartości

if a > b: ## porównanie a i b
    if a > c: ## porównanie a i c jeżeli a >b
        max = a ##ustawienie max na a
    else: ## jeżeli c jest większe
        max = c ## ustawienie max na c
else: ## jeżeli b >a
    if b > c: ##porownanie b i c jezeli b>a
        max = b ## ustawienie max na b
    else: ## jezeli  c>b
        max = c ## ustawienie max na c

print(max) ##wypisanie wartosci zmiennej max