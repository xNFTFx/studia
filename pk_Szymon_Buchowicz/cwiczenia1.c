// Szymmon Buchowicz 
// cw 27.02.2024

#include <stdio.h> //wczytanie biblio z inputem i outputem
#include <math.h>


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

void cw1_zadanie6(){
    char imie[20];
    char plec_wybor;
    int wiek = 0;
    float wzrost = 0;
    int plec_typ = 0, wzrost_typ = 0;
    char plec[3][10] = {{"kobieta"}, {"mezczyzna"}, {"niebinarny"}};
    char kat_wzrost[3][10] = {{"niski"}, {"sredni"}, {"wysoki"}};


    printf("Podaj imie: ");
    scanf("%s", imie);
    printf("Podaj plec (m - mezczyzna, k - kobieta): ");
    scanf("%c", &plec_wybor);
    printf("Podaj wiek: ");
    scanf("%d", &wiek);
    printf("Podaj wzrost (w centymetrach): ");
    scanf("%f", &wzrost);

    if(plec_wybor == 'k'){plec_typ = 0;}
    else 
    { if(plec_wybor == 'm'){plec_typ = 1;}
    else{ plec_typ = 2;}};

    if(wzrost <160){wzrost_typ = 0;}
    else if (wzrost <= 180){wzrost_typ = 1;}
    else {wzrost_typ = 2;}


    printf("mam na imie %s, jestem %s, mam %d lat, %f cm wzrostu i przez to jestem %s", imie ,plec[plec_typ], wiek, wzrost, kat_wzrost[wzrost_typ] );

}

void pd1(){
    int d1, m1, y1, d2, m2, y2;

    printf("Podaj pierwsza date (dd/MM/yyyy): ");
    scanf("%d/%d/%d", &d1, &m1, &y1);
    
    printf("Podaj druga date (dd/MM/yyyy): ");
    scanf("%d/%d/%d", &d2, &m2, &y2);

    if (y1 < y2 || (y1 == y2 && m1 < m2) || (y1 == y2 && m1 == m2 && d1 < d2)) {
        printf("Data %02d/%02d/%04d jest wczesniejsza niz data %02d/%02d/%04d\n", d1, m1, y1, d2, m2, y2);
    } else if (y1 == y2 && m1 == m2 && d1 == d2) {
        printf("Podane daty sa rowne: %02d/%02d/%04d\n", d1, m1, y1);
    } else {
        printf("Data %02d/%02d/%04d jest wczesniejsza niz data %02d/%02d/%04d\n", d2, m2, y2, d1, m1, y1);
    }
}

void pd2(){
    float a, b, c;
    float delta, x1, x2, czesc_rzeczywista, czesc_urojona;

    printf("Podaj wspolczynniki rownania kwadratowego (a, b, c): ");
    scanf("%f %f %f", &a, &b, &c);

    delta = b * b - 4 * a * c;

    if (delta > 0) {
        x1 = (-b + sqrtf(delta)) / (2 * a);
        x2 = (-b - sqrtf(delta)) / (2 * a);
        printf("Pierwiastki rownania: %.2f i %.2f\n", x1, x2);
    } else if (delta == 0) {
        x1 = -b / (2 * a);
        printf("Pierwiastek rownania: %.2f\n", x1);
    } else {
        czesc_rzeczywista = -b / (2 * a);
        czesc_urojona = sqrtf(-delta) / (2 * a);
        printf("Pierwiastki zespolone: %.2f + %.2fi i %.2f - %.2fi\n", czesc_rzeczywista, czesc_urojona, czesc_rzeczywista, czesc_urojona);
    }
}


int main()
{
    return 0;

}




