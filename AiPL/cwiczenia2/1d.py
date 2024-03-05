##zadeklarowanie wartości x i n/ mogą być wprowadzone inputem
x = 2
n = 5
wynik = 1 ##zmienna wynik - ustawienie jej początkowo na 0 pomaga w przypadku gdy n = 0

for i in range(n): ## petla wykonywana n razy
    wynik *=x ## mnozenie wyniku i x

print(wynik) ##pokazanie wartosci wyniku
