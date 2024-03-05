import sys  #zaimportowanie biblioteki, aby przyjmować argumenty z command line
from nwd import szukanie_nwd as nwd
from trojmian_kwadratowy import oblicznie_pierwiastkow_trojmianu_kwadratowego as optk
from doprowadzanie_do_cyfry import doprowadzanie_do_cyfry as ddc


## testy

if __name__ == '__main__': #main programu
    wybor = input("czy na poczatku chcesz przetestowac zadanie 3 dla arguentu z lini zadan?\n [wpisz 1 jezeli tak, jezeli nie podaj jakakolwiek inna wartosc]\n") #info dla użytkownika
    if wybor == 1: #jeżeli użytkownik wybral 1 - tak
        print("wynik dla zadania 3 dla argumentu z command line to: ", ddc(sys.argv[1])) #wykonujemy polecenie z zad 3 dla argumentu pobranego z command line za pomocą biblioteki sys i funkcji argv
    while True: #nieskonczona petla
        print("ktore zadanie chcesz przetestowac \n 1- wprowadz 1\n 2 - wprowadz 2\n 3 - wprowadz 3 \n k - chcesz zakonczyc program") #info dla użytkownika
        wybor = input() #danie wyboru uzytkownikowi
        match wybor: # dopasowanie odpowiedzi uzytkownika
            case '1': #jak wybral 1
                print("program sluzy do znajdywania NWD dwoch podanych liczb") #info dla uzytkownika
                a = input("podaj pierwsza liczbe ") #prosba o wpisanie liczby
                b = input("podaj druga liczbe ") #prosba o wpisanie liczby
                print("NWD tych liczb to: ", nwd(int(a), int(b)), '\n') #wyswietlenie wyniku programu i wywolanie funkcji
            case '2': # jak wybral 2
                print("program służy do wyznaczania pierwiastków trójmianu kwadratowego podanego w postaci a*x^2 + b*x + c") #info dla uzytkownika
                a = input("podaj a ") #prosba o wpisanie liczby
                b = input("podaj b ") #prosba o wpisanie liczby
                c = input("podaj c ") #prosba o wpisanie liczby
                print("Pierwiastki tego wielomianu: ", optk(int(a),int(b), int(c)), '\n') #wyswietlenie wyniku programu i wywolanie funkcji
            case '3': # jak wybral 3
                print("program sluzy do doprowadzenia dowolnej liczby całkowitej do postaci cyfry, poprzez sumowanie jej cyfr") #info dla uzytkownika
                liczba = input("podaj liczbe ") #prosba o wpisanie liczby
                print("Program doprowadził tą liczbę to cyfry: ", ddc(liczba), '\n') #wyswietlenie wyniku programu i wywolanie funkcji
            case 'k': #jak wybral k
                print("Program zakończony") #info dla uzytkownika
                break #zakonczenie nieskonczonej petli
            case _ : #jak wybral cos innego niz powyzsze
                print("Podałeś błędny argument. Spróbuj ponownie \n") #pokazanie uzytkownikowi ze zle wybral
