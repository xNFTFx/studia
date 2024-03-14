#include <stdio.h> //wczytanie biblio z inputem i outputem

//Szymon Buchowicz

void cw2_zadanie1(){
    int a, b;
    printf("Podaj 2 liczby calkowite dodatnie: ");
    if(scanf("%d%d", &a, &b)<2 || a < 0 || b < 0)
    { printf("niepoprawne dane");}
    if(a==b){
        printf("pole kwadratu o bokach %d, %d wynosi %d", a, b, a*b);
    }
    else{
        printf("pole prostokata o bokach %d, %d wynosi %d", a, b, a*b);
    }
}

void cw2_zadanie2()
{
    int a, b, c;
    printf("podaj 3 liczby calkowite dodatnie\n");
    if(scanf("%d%d%d", &a, &b, &c)<3 || a < 0 || b < 0 || c<0)
    { printf("niepoprawne dane");}
    if(a+b < c || b+c < a || a+c < b){printf("nie da sie stworzyc trojkata");}
    else{printf("da sie zbudowac taki trojkat\n");}
}

void cw2_zadanie3(){
    float wzorst;
    printf("podaj swoj wzrost\n");
    scanf("%f", &wzorst);
    if(wzorst <160){printf("jestes niski %f\n", wzorst);}
    else if (wzorst <= 180){printf("jestes sredni %f\n", wzorst);}
    else {printf("jestes wysoki %f\n", wzorst);}
    
}

void cw2_zadanie4()
{
    float a,b;
    char znak;
    printf("podaj dzialanie w postaci \n'<liczba> <znak> <liczba>'\n");
    if(scanf("%f %c %f", &a, &znak, &b)<3)
    { printf("niepoprawne dane\n");}
    switch (znak)
    {
    case '+':
        printf("%f %c %f = %f", a, znak, b, a+b);
        break;
    case '-':
        printf("%f %c %f = %f", a, znak, b, a-b);
        break;
    case '*':
        printf("%f %c %f = %f", a, znak, b, a*b);
        break;
    case '/':
        printf("%f %c %f = %f", a, znak, b, a/b);
        break;
    default:
        printf("niepoprawne dane\n ");
        break;
    }
}

int cw2_zadanie5()
{
    int n;
    printf("podaj liczbe calkowita n\n");
    if(scanf("%d", &n)<1 || n<0)
    { printf("niepoprawne dane");}
    float tab[n];
    float suma = 0, min = 0, max= 0;
    if(n == 0){printf("Wybrales n = 0, wiec min, max, srednia i suma tez sa rowne 0 ;)\n");return 0;}
    printf("podawaj kolejne liczby calkowite do tablicy: \n");
    printf("podaj 1 liczbe: ");
    if(scanf("%f", &tab[0])<1){printf("podales zla dana");}
    suma += tab[0];
    min = tab[0];
    max = tab[0];
    for(int i= 1; i< n; i++){
        printf("podaj %d liczbe: ", i+1);
        if(scanf("%f", &tab[i])<1)
        { printf("podales zla dana"); break;}
        suma += tab[i];
        if(min > tab[i]){min = tab[i];}
        if(max < tab[i]){max = tab[i];}
    }
    printf("min: %f max: %f sum: %f avg: %f", min, max, suma, suma/n);

}


void cw2_zadanie6()


int main()
{
    cw2_zadanie5();
    return 0;
}