## zadeklarowanie tablicy wartości/ może być w formie prosby o wpisanie - input
x = [2, 43, 212, 32, 123, 3, 999, 134, 1, 0, 432]

max = x[0] ## stworzenie zmiennej pomocniczej max i przypisanie jej wartosci pierwszego elementu tablicy(w pythonie indeksy elementów w tablicy liczymy od 0)

for i in range(1, len(x)): ##petla chodzaca od elementu o indeksie 1(dla tablicy zadeklarowanej 43),aż i osiągnie wartość o 1 mniejszą niż długość tablicy
    if x[i] > max: ## porownanie obecnie sprawdzanego elementu tablicy z wartoscia max
        max = x[i] ## jezeli max jest mniejesze od sprawdzanego elementu, przypisujemy max wartpsc elementu

print(max) ##wyswietlamy max