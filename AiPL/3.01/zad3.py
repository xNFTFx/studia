wyraz = 'd u p a'
wyraz = wyraz.split()

for i in range(int(len(wyraz)//2)):
    t = wyraz[i]
    wyraz[i] = wyraz[-i - 1]
    wyraz[-i-1] = t
print(wyraz)