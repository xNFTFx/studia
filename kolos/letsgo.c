#include <stdio.h>
#include <ctype.h>

void zadanie1(){
    int n, liczba;
    printf("podaj n: ");
    if( scanf("%d", &n) != 1){return ;}
    for(int i = 0; i<n; i++){
        scanf("%d", &liczba);
        if(liczba%10 == 9){printf("%d\n", liczba);}
    }
}



int zadanie3(int a){
    if(a == 0){return a;}
    return a%10 + zadanie3(a/10);
}

void zadanie4(int n){
    for(int i = 0; i < (n+1)/2; i++){
        for(int j =0; j<i; j++){
            printf("  ");
        }
        for(int j = 0; j< n -2*i; j++){
            printf(" *");
        }
        printf("\n");
    }
}

void zadanie5(char *s){
    for(int i = 0; s[i] != '\0'; i++){
        if(islower(s[i])==1){s[i] = toupper(s[i]);}
        else if(isupper(s[i])==1){s[i] = tolower(s[i]);}
        printf("%c", s[i]);
    }
}

int main(){
    char slowo[9] = "sadSADasd";
    zadanie5(slowo);
}