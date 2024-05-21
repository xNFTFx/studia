#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// nosoroce białe nie są wcale białe, tylko szre
// Prawidłowo powinny być nazywane szerokopyskimi



#define FUN(x, y) (x) > (y) ? ((x)*(y)) : ((x)*(x) + (y) * (y))


void zad2(int n){
    int tablica_a[n];
    int b = rand() % 11 + 5;
    srand((unsigned int)time(0));
    for(int i = 0; i < n; i++){
        tablica_a[i] = rand() % 21;
        printf("a: %3d, b: %3d \n", tablica_a[i], b);
        if(tablica_a[i] > b){printf("%d\n", tablica_a[i]);}
        else{printf("X\n");}
    }
}

int zadanie3(int n ,int *tablica, int pozycja, int max){
    if(pozycja == n){ return max;}
    if( tablica[pozycja] > max){
        max = tablica[pozycja];
    }
    return zadanie3(n, tablica, pozycja+1, max);
}

void test_zadanie3(){
    int tab[] = {1, 4, 2, 2, 4, 6, 8, 4, 2, 5};
    printf("%d", zadanie3(10, tab, 0, tab[0]));
}

void zadanie_4(){
    int n = 9;
    int tablica[n][n];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(j == i || i == n-j-1){tablica[i][j] = 0;}
            else if(i%2 ==0){tablica[i][j] = n-j;}
            else {tablica[i][j] = j+1;}
            printf("%3d", tablica[i][j]);
        }
        printf("\n");
    }
}

void zadanie_5(int n, char slowo[n]){
    for(int i = 0; i < n; i++){
        if(isdigit(slowo[i])==1){printf("?");}
        if(isalpha(slowo[i]) == 1){printf("X");}
    }

}

void test_zadanie_5(){
    char slowo[5] = "s2afs";

    zadanie_5(5, slowo);
}

void losowe_liczby(int n){
    srand((unsigned int)time(0));

    for(int i = 0; i < n; i++){
        printf("%d\n", rand() % 101 + 20);
        
    }
}

void jd(){
    char slowo[] = "asd a dsa";

}

int main(){
    losowe_liczby(100);
    return 0;
}