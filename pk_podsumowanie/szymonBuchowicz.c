// Szymon Buchowicz
// 421827
// 23.04.2024

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <time.h>

#define M 10

#define FUN(x,y) (x > y) ? (x * y) : 1/((x)*(x) + (y)*(y))

void zadanie1();
void zadanie01();
void zadanie2();
int zadanie3(int a);
void zadanie4(int n);


int main(){
    printf("%f", FUN(8, 2));
    return 0;
}

void zadanie01(){
    float a[] = {1, 2, 3, 4, 8,6, 7, 8, 9};
    int n = sizeof(a) / sizeof(a[0]);
    for(int i = 0; i<n-1; i++){
        printf("f(%f, %f) = %f\n", a[i], a[i+1], FUN(a[i], a[i+1]));
    }
}

void zadanie1(){
    int n;
    printf("Podaj n: ");
    if(scanf("d", &n) <1){ printf("niepoprawne dane"); return;}
    for(int i = 0l; i < n; i++){
        int a;
        printf("%d: ", i+1);
        fseek(stdin, 0, SEEK_END);
        if(scanf("%d", &a) < 1){
            i--; continue;
        }
        if(a % 10 == 9){printf("Liczba z cyfra 9: %d\n", a);}
        
    }
}

void zadanie2(){
    char s[100] = "";
    int d, m, r;
    printf("podaj swoje imie i nazwisko: ");
    fgets(s, sizeof(s), stdin);
    // printf("%s", s);
    // printf("podaj swoja date urodzenia 'DD/MM/YYYY'\n");
    // if(scanf("%d/%d/%d", d, m, r) != 3){
    //     printf("niepoprawne dane");
    //     return;
    // }
    srand((unsigned int)time(0));
    int  a[M][M];
    for (int i =0; i<M; i++){
        for (int j = 0; j<M ; j++){
            a[i][j] = rand() % 63 - 31;
            printf("%4d ", a[i][j]);
        }
        printf("\n");
    }
    printf("procent: = %d %%");

}

int zadanie3(int a){
    if(a ==0){
        return 0;
    }
    return a%10 + zadanie3(a/10);
}

void zadanie4(int n){
    for(int i = 0; i<(n+1)/2; i++){
        for(int j = 0; j < i; j++){printf("  ");}
        for(int j = 0; j< n- 2*i; j++){printf("* ");}
        printf("\n");
    }
}

void zadanie5(char s[]){
    for(int i = 0; s[i] != '\0';  i++){
        if(islower(s[i])){
            s[i] = toupper(s[i]);
        }
        else{
            s[i] = tolower(s[i]);
        }
    }
}

int maxel(int a[], int n, int i, int m){
    if(i  == n){return m;}
    if(a[i] > m){m= a[i];}
    return maxel(a, n, i+1, m);
}