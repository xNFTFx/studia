liczba = -0.27

mantysa = []

potega = 1
przesuniecie_wykladnika = 0
bit_znaku = 0

if liczba < 0:
    bit_znaku = 1

liczba = abs(liczba)

while True:
    while True:
        potega *=2
        przesuniecie_wykladnika +=1
        if potega > liczba:
            potega/=2
            przesuniecie_wykladnika-=1
            break
    print(potega, przesuniecie_wykladnika)
    if potega < liczba:
        mantysa.append(1)
        liczba-=potega
    else:
        mantysa.append(0)
    potega/=2
    if mantysa[0] == 0:
        przesuniecie_wykladnika -=1
        mantysa.pop(0)
    print(mantysa, liczba)
    if len(mantysa) == 24:
        break

mantysa.pop(0)

wykladnik_dziesietny = 127 + przesuniecie_wykladnika
wykladnik_binarny = []

potega = 128
print(wykladnik_dziesietny)
while potega >=1:
    print(potega)

    if wykladnik_dziesietny >= potega:
        wykladnik_dziesietny-=potega
        wykladnik_binarny.append(1)
    else:
        wykladnik_binarny.append(0)
    potega/=2

print(bit_znaku, wykladnik_binarny, mantysa)

