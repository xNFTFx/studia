#include <stdio.h>
#define PLECSTR(plec) plec == 'M' ? "mezczyzna" : plec =='K' ? "kobieta" : "???"

void zadanie1()
{
    char imie[20], nazwisko[20];
    char plec;
    scanf("%s %s %c", &imie, &nazwisko, &plec);
    printf("\n");
    // scanf("%c", &plec);

    printf("%s %s, %s", imie, nazwisko, PLECSTR(plec));


}

int podzielne_przez_3_lub_5(int liczba){
    if(liczba%3 == 0 || liczba%5 == 0){return 1;}
    else{return 0;}
}

void zadanie4(int n){
    for(int i = 0; i < n-1; i++)
    {
        for(int j = 0; j< n; j++){
            if(i * j == 0 || i == n-2 || j == n-1){printf("* ");}
            else{
                if(i < n/2){
                    if(i+j == n-1 || i==j)
                    {
                        printf("* ");
                    }
                    else{printf("  ");}
                }
                else{
                    if(i+j == n-2 || i==j-1)
                    {
                        printf("* ");
                    }
                    else{printf("  ");}
                }
                
            }
            
        }
        printf("\n");
    }
}

int main(){
    zadanie4(10);
    return 0;
}