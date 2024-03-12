#include <stdio.h>
#include <stdlib.h>
#include <time.h>


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

int montecarlo(dokladnosc){
    srand((unsigned)time(0));
    for( int i = 0, i < dokladnosc; i++){
            float x = rand() % (1);
            float y = rand() % (1);
            printf("%f %f \n", x, y);
    }
}


int main()
{
montecarlo(10) ;
}