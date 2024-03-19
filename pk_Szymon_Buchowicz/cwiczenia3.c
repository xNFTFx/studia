#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>


int podzielna_przez_3_lub_5(int liczba){
    if(liczba%3 == 0 || liczba%5 == 0){
        return 1;
        }
    else{
        return 0;
    }
}

void suma_i_srednia_podzielnych_przez_3_lub_5(){
    int n, suma = 0, licznik = 0;
    printf("podaj n:");
    if (scanf("%d", &n) < 1 || n<1){printf("niepoprawne dane");}

    srand((unsigned)time(0));
    for(int i = 0; i<n; i++)
    {
        int x = rand() % (1000  - 9+1);
        if (podzielna_przez_3_lub_5(x) == 1){
            printf("[%d] \n", x);
            suma +=x, licznik++;
        }
        else{
            printf("(%d) \n", x);
        }
    }
    printf("suma = %d\n srednia = %f\n", suma, (float)suma/licznik);
}

int potega_2(unsigned int liczba)
{
    int i = 1, y;

    while (liczba > i)
    {
        i =i<<1;
        if (liczba == i){
            return 1;
        }

    }
    
}

int test_potega_2(){

    for(int i = 0; i < 5000; i++){
        if (potega_2(i)==1){
            printf("%d\n", i);
        }
    }
}

int montecarlo(int dokladnosc){
    srand((unsigned)time(0));
    int promien = 1000000;
    int w_kole = 0;
    for( int i = 0; i < dokladnosc; i++){
            double x = rand() % (promien);
            double y = rand() % (promien);
            if(sqrt(x*x + y*y) <= promien){w_kole+=1;}
    }
    printf("%f", (double)w_kole*4/dokladnosc);
}

void zadanie_5(){
    int n;
    printf("podaj liczbe calkowita n\n");
    if(scanf("%d", &n)<1 || n<0)
    { printf("niepoprawne dane");}
    float tab[n];
    srand((unsigned)time(0));
    if(n == 0){printf("Wybrales n = 0, wiec min, max, srednia i suma tez sa rowne 0 ;)\n");}
    float suma = 0;
    float min = 50;
    float max = 0;
    int licznik = 0;
    for(int i= 0; i< n; i++){
        tab[i] = (rand() % (100+1)) -50;
        if(tab[i] > 0){       
            suma += tab[i];
            licznik+=1;
            if(min > tab[i]){min = tab[i];}
            if(max < tab[i]){max = tab[i];}
        }
    }
    printf("min: %f max: %f sum: %f avg: %f", min, max, suma, suma/licznik);
}

int main()
{
montecarlo(500000000); // u mnie na kompie w miare szybko leci ale radze uwazac ;)
}