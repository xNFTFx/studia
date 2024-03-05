##nie wiem czy jest dobrze bo w zadaniu miala byc podwojona,a tu zawsze wychodzi wieksza niz podwojona, ale zakladam ze o to jej chodzilop
x = 1000 #jakies tam poczatkowe wartosci
p = 10 #p w procentach czyli bedzie trzeba przemnozyc przez 0.01, ale na kartce nie trzeba jak sie napisze *10%
x_zmienione = x #wprowadzamy wartosc zmieniana i zaczynamy na x
lata = 0 #zmienna do liczenia lat
while x_zmienione<x*2: #petla dopoki nie nsazza wartosc bedzie mniejsza od x*2
    x_zmienione = x_zmienione* p * 0.01 + x_zmienione #wzo
    lata+=1

print(lata)