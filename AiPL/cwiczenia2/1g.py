import random #wczytanie biblioteki do losowych liczb

n = 10 # ile liczb mamy losować
t = random.randint(0,100) #losowanie liczb naturalnych od 0,100
min = t #ustawienie min na 1. liczbę

for i in range(n-1): #pętla wykonywana n-1 razy ponieważ pierwszą liczbęlosujemy wcześniej
    t = random.randint(0, 100) #losujemy liczbę
    if min > t: #sprawdzamy czy wylosowana liczba jest mniejsza niż min
        min = t #jeżeli jest to zmieniaym min na t


print(min) #pokazujemy min