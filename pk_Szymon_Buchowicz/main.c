// Szymmon Buchowicz 
// cw 27.02.2024

#include <stdio.h> //wczytanie biblio z inputem i outputem
#include "cwiczenia2.h"
#include "cwiczenia3.h"

void cw1_zadanie1(){printf("Hello world\n");}

void cw1_zadanie2()
{
    unsigned int d, m, y;
    printf("podaj swoja date urodzenia (dd/MM/yyyy)");
    if(scanf("%u/%u/%u", &d, &m, &y)<3 || y<1900 || y>2024){
        printf("Nie poprawne dane\n");
        return;
    }
    printf("urodziles sie w roku %u\n", y);
}

void cw1_zadanie3(){

    char first_name[80] = "";
    printf("Podaj swoje imie i nazwisko\n");
    fgets(first_name, sizeof(first_name), stdin);
    printf("Witaj %s\n", first_name);

}

void cw1_zadanie4(){

    int a, b, c;
    printf("podaj 3 liczby, a, b, c\n");
    if(scanf("%d %d %d", &a, &b, &c) < 3){
        printf("zle dane");
        return;
    };
    int m = a;
    if(m > b){m = b;};
    if(m > c){m = c;};
    printf("%d", m);
}

void cw1_zadanie5(){
    float wzorst;
    printf("podaj swoj wzrost\n");
    scanf("%f", &wzorst);
    if(wzorst <160){printf("jestes niski %f\n", wzorst);}
    else if (wzorst <= 180){printf("jestes sredni %f\n", wzorst);}
    else {printf("jestes wysoki %f\n", wzorst);}
    
}

/*void cw1_zadanie6(){
    char imie[20] = "";
    char plec_wybor;
    int wiek = 0;
    float wzrost = 0;
    int plec_typ = 0, wzrost_typ = 0;
    char plec[3][10] = {{"kobieta"}, {"mezczyzna"}, {"niebinarny"}};
    char kat_wzrost[3][10] = {{"niski"}, {"sredni"}, {"wysoki"}};


    printf("Podaj po kolei: \n imie \n plec \n wiek \n wzrost\n\n");
    scanf("%s %c %d %f", &imie, &plec_wybor, &wiek, &wzrost);

    if(plec_wybor == 'k'){plec_typ = 0;}
    else 
    { if(plec_wybor == 'm'){plec_typ = 1;}
    else{ plec_typ = 2;}};

    if(wzrost <160){wzrost_typ = 0;}
    else if (wzrost <= 180){wzrost_typ = 1;}
    else {wzrost_typ = 2;}


    printf("mam na imie %s, jestem %s, mam %d lat, %f cm wzrostu i przez to jestem %s", imie ,plec[plec_typ], wiek, wzrost, kat_wzrost[wzrost_typ] );

}
*/

int main()
{
    suma_i_srednia_podzielnych_przez_3_lub_5();
    return 0;
}




