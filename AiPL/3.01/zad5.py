tab = [5, 3, 2, 9, 9, 1, 8]

if len(tab) % 2 == 1:
    tab.append(tab[len(tab) - 1])
min = tab[0]
max = tab[0]
for i in range(0, len(tab), 2):
    if tab[i] > tab[i+1]:
        t = tab[i]
        tab[i] = tab[i+1]
        tab[i+1] = t
    if tab[i+1] > max:
        max = tab[i+1]
    if tab[i] < min:
         min = tab[i]

print(tab, min, max)