tablica = [0,1,2,3,4,5,6,7,8,9, 10]

szukana = 3
l = 1
p = 1
suma = 0

while szukana != suma:
    if p >= len(tablica):
        print("nie ma takiego podciągu")
        break
    if suma < szukana:
        suma += tablica[p]
        p+=1

    else:
        suma -=tablica[l]
        l+=1

print(l, p-1)