## zadanie 2
def oblicznie_pierwiastkow_trojmianu_kwadratowego(a, b, c): #zadeklarowanie funkcji pobierajacej 3 zmienne, które są współczynnikami kolejnych wyrazów funkcji kwadratowej w formacie a*x^2 + b*x + c
    delta = b**2 - 4*a*c #obliczenie delty ze wzoru b^2 - 4*a*c
    if delta <0: #jeżeli delta jest mniejsza od 0
        return None #zwracamy że nie ma miejsc zerowych
    elif delta == 0: #jeżeli delta jest równa 0
        return -b/(2*a) #zwracamy jedno miejsce zerowe ze wzoru
    else: #i jeżeli żaden z powyższych warunków nie jest prawdziwy <=> delta jest większa od 0
        return (-b - delta ** 0.5)/(2*a), (-b+delta ** 0.5)/(2*a) #to zwracamy oba miejsca zerowe w formie krotki

if __name__ == "__main__": #polecenia wykonywane tylko gdy ten plik jest wykonywanym plikiem
    print(oblicznie_pierwiastkow_trojmianu_kwadratowego(1,2,1)) # = -1
    print(oblicznie_pierwiastkow_trojmianu_kwadratowego(1,3,2)) # = -2, = -1
    print(oblicznie_pierwiastkow_trojmianu_kwadratowego(10,2,1)) # = None