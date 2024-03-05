potega() #w pythonie nie ma petli do while więc to jest ten skopiowany pseudokod pani
{ wczytaj(x,n);
y:=1; z:=x; m:=n; do{
if(m % 2 ==1)
{ y:=y*z; m:=m-1; }
z := z*z; m:=m/2; } while(m!=1)
wypisz(y*z); }

niezmiennikiem jest