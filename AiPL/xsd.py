import tkinter as tkr
import math
import time
from tkinter import messagebox

# przykladowe rozmiary plotna
width = 1020
height = 800

# tworzenie okna, canvasu itd.
tk = tkr.Tk()
tk.state("zoomed")
tk.title("Symulator rownii pochylej")
canvas = tkr.Canvas(tk, width=width, height=height)
canvas.grid(column=0, row=1, columnspan=4)

# tworzenie i opis roznych zmiennych
xRuch = 0 # przesuniecie klocka w prawo przez 1 klatke
yRuch = 0 # przesuniecie klocka w dol przez 1 klatke

przycisk = 0 # sprawdza czy START zostal wcisniety
v = 0.0 # predkosc [m/s]
g = 9.81 # przyspieszenie ziemskie [N/kg]
t_start = 0.0 # czas rozpoczecia symulacji
t = 0.0 # uplyniete sekundy od rozpoczecia symulacji
t_klatka = 0.0 # czas narysowania ostatniej klatki
droga = 0.0 # droga do przebycia w czasie 1 klatki

# przykladowe, domyslne parametry klocka i rowni
alfa = math.radians(15.0) # w nawiasie wartosc kata w stopniach
masa = 10.0 # kg
tarcie = 0.2 # wspolczynnik tarcia, brak jednostki

# koordynaty rogow rownii, uzyte pozniej do jej rysowania
y = 0
x = 0

# sily dzialajace na klocek
silaGrawitacji = 0.0
silaZsuwajaca = 0.0
silaDociskajaca = 0.0
silaTarcia = 0.0

# przyspieszenie klocka
przyspieszenie = 0.0

# funkcja umozliwiajaca dzialanie przycisku START
def przyciskWcisniety():
    global przycisk, przyspieszenie, t_start, t_klatka, t

    if przycisk == 0: # (nie chcemy zeby przycisk START dzialal podczas symulacji)
        przycisk = 1
        if przyspieszenie == 0:
            tkr.messagebox.showinfo(title = None, message = "Klocek nie poruszy sie, za duza sila tarcia")
        t_start = time.time()
        t_klatka = time.time()
        t = 0

# tworzenie pol na wpisanie danych i ich opisow
l1 = tkr.Label(tk, text = "Kat: - (0;90)\nwartosc domyslna: 15.0 stopni")
l2 = tkr.Label(tk, text = "Masa klocka: - >0\nwartosc domyslna: 10.0kg")
l3 = tkr.Label(tk, text = "Wspolczynnik tarcia: - <0;1>\nwartosc domyslna: 0.2")
e1 = tkr.Entry(tk, width = 20)
e2 = tkr.Entry(tk, width = 20)
e3 = tkr.Entry(tk, width = 20)

l1.grid(column = 0, row = 0)
l2.grid(column = 1, row = 0)
l3.grid(column = 2, row = 0)
e1.grid(column = 0, row = 1, sticky = tkr.N)
e2.grid(column = 1, row = 1, sticky = tkr.N)
e3.grid(column = 2, row = 1, sticky = tkr.N)

# funkcja od generowania rownii i klocka od nowa
def odswiezRownie():
    global y, lewybok, dolnybok, przeciwprostokatna, klocek, rownia, alfa, canvas, g, masa, tarcie, silaGrawitacji, silaZsuwajaca, silaDociskajaca, silaTarcia, przyspieszenie, width, height, canvas

    # jezeli zmienil sie rozmiar okna, zmieniamy parametry width i height
    canvas.update()
    width = (tk.winfo_width() - 4) # -4 bo boczna krawedz okna ma grubosc 2 pikseli, a tk.winfo_width() uwzgledna rowniez szerokosc ramki
    height = (tk.winfo_height() - 40) # -40 bo gorna i dolna krawedz okna maja w sumie grubosc 40 pikseli, a tk.winfo_height() uwzgledna rowniez szerokosc ramki

    # usuwanie poprzedniego klocka i rowni, jezeli juz istnieja
    if "klocek" in globals() or "klocek" in locals():
        canvas.delete(klocek)
        canvas.delete(rownia)

    # dostosowanie rozmiaru plotna do obecnego rozmiaru okna
    canvas.config(width = width, height = height)

    # siły oddziałujące na klocek
    silaGrawitacji = masa * g

    # składowe siły grawitacji
    silaZsuwajaca = silaGrawitacji * math.sin(alfa)
    silaDociskajaca = silaGrawitacji * math.cos(alfa)

    silaTarcia = tarcie * silaDociskajaca

    # sila wypadkowa zsuwajaca klocek (przyspieszenie klocka)
    if silaZsuwajaca > silaTarcia:
        przyspieszenie = (silaZsuwajaca - silaTarcia) / masa
    else:
        przyspieszenie = 0

    # wymiary rowni, zakladajac ze dolna krawedz jest stalej dlugosci
    dolnybok = width - 20  # dlugosc dolnego boku
    y = height - abs(math.floor(math.tan(alfa) * dolnybok))  # koordynat y ruchomego, lewego gornego punktu rowni
    lewybok = height - y - 10  # dlugosc lewego boku
    przeciwprostokatna = math.sqrt((lewybok**2) + (dolnybok**2))  # dlugosc przeciwprostokatnej rowni

    # rysowanie rowni
    if y >= l1.winfo_height() + e1.winfo_height(): # jezeli rownia miesci sie na ekranie, zostawiamy nasze zalozone wartosci
        rogiRowni = [10, height - 10, width - 10, height - 10, 10, y]
        rownia = canvas.create_polygon(rogiRowni, fill = "brown")
    else: # jezeli rownia sie nie miesci, ustawiamy y na maksymalny i skracamy dolny bok, zeby zachowac kat
        y = l1.winfo_height() + e1.winfo_height() # koordynat y tym razem nieruchomego, lewego gornego punktu rowni
        lewybok = height - 10 - y  # dlugosc lewego boku
        x = (lewybok/math.tan(alfa))-10 # koordynat x tym razem ruchomego, prawego dolnego punktu  rowni
        dolnybok = x - 10 # dlugosc dolnego boku
        przeciwprostokatna = math.sqrt((lewybok**2) + (dolnybok**2))  # dlugosc przeciwprostokatnej rowni
        rogiRowni = [10, height - 10,  x, height - 10,  10, y]
        rownia = canvas.create_polygon(rogiRowni, fill = "brown")

    # rysowanie klocka
    a = 200  # dlugosc klocka
    b = 100  # wysokosc klocka

    x1 = 10
    y1 = y

    x2 = x1 + math.floor(a * dolnybok / przeciwprostokatna)
    y2 = y1 + math.floor(a * lewybok / przeciwprostokatna)

    x4 = x1 + math.floor(b * lewybok / przeciwprostokatna)
    y4 = y1 - math.floor(b * dolnybok / przeciwprostokatna)

    x3 = x4 + math.floor(a * dolnybok / przeciwprostokatna)
    y3 = y4 + math.floor(a * lewybok / przeciwprostokatna)

    rogiKlocka = [x1, y1,  x2, y2,  x3, y3,  x4, y4]

    klocek = canvas.create_polygon(rogiKlocka, fill="light blue")

    canvas.update()

odswiezRownie()

# odswiezanie danych: katu nachylenia rampy, masy klocka i wspolczynnika tarcia (wywolywane po wcisnieciu przycisku ODSWIEZ ROWNIE)
def odswiezDane():
    global alfa, masa, tarcie, xRuch, yRuch, t, przycisk

    # reset danych
    przycisk = 0
    t = 0
    xRuch = 0
    yRuch = 0

    # sprawdzanie zawartosci pol do wpisywania wartosci
    if e1.get() != "":
        if float(e1.get()) < 0 or float(e1.get()) > 90:
            tkr.messagebox.showerror(title = "Error", message = "Dane nieprawidlowe")
        else:
            alfa = math.radians(float(e1.get()))
    if e2.get() != "":
        if float(e2.get()) <= 0:
            tkr.messagebox.showerror(title = "Error", message = "Dane nieprawidlowe")
        else:
            masa = float(e2.get())
    if e3.get() != "":
        if float(e3.get()) < 0 or float(e3.get()) > 1:
            tkr.messagebox.showerror(title = "Error", message = "Dane nieprawidlowe")
        else:
            tarcie = float(e3.get())

    # odswiezenie rownii z nowymi danymi
    odswiezRownie()

#tworzenie przyciskow
b1 = tkr.Button(tk, text = "START", command = przyciskWcisniety)
b2 = tkr.Button(tk, text = "ODSWIEZ\nROWNIE", command = odswiezDane)

b1.grid(column = 3, row = 0, sticky = tkr.N)
b2.grid(column = 3, row = 1, sticky = tkr.N)

# rysowanie obrazu
while True:
        if przycisk: # ruch zaczynamy dopiero po nacisnieciu START
            v = przyspieszenie * t
            droga = v * (time.time() - t_klatka) * 100
            t = time.time() - t_start
            xRuch = droga*dolnybok/przeciwprostokatna
            yRuch = droga*lewybok/przeciwprostokatna
            t_klatka = time.time()
            canvas.move(klocek, xRuch, yRuch)

            # jezeli klocek przejechal cala dlugosc rowni, resetujemy klocek i podajemy wyniki symulacji
            if canvas.coords(klocek)[1] > height:
                przycisk = 0
                odswiezRownie()
                tkr.messagebox.showinfo(title = "Wynik", message = f"Czas przebycia: ~{round(t,2)}s\nMaksymalna predkosc: ~{round(v,2)}m/s\nPrzyspieszenie wyniosło: ~{round(przyspieszenie,2)}m/s^2\nPrzebyta droga: ~{round(przeciwprostokatna/100,2)}m")

        else: # sprawdzanie czy okno zmienilo swoje rozmiary, jezeli tak to odswiezamy rownie, zeby wpasowala sie w nowe okno
            if width != (tk.winfo_width() - 4) or height != (tk.winfo_height() - 40):
                odswiezRownie()
        canvas.update()