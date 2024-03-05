tab = [3, 5, 2, 9, 1, 2, 8]

max = tab [0]

for i in range(1, len(tab)):
    if max < tab[i]:
        max = tab[i]

print(max)
