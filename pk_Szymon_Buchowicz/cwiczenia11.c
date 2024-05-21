#include <stdio.h>
#include <ctype.h>
#include "cwiczenia11.h"

char *decipher(char *s, int p, int n){
    int zmiana = (26+p) %26;
    
    for(int i = 0; i < n; i++){
        if(islower(s[i]))
        {
            if(s[i] + zmiana > 122){s[i] = s[i] + zmiana - 26;}
            else{s[i] = s[i] + zmiana;}
        }
        else {if(isupper(s[i]))
        {
            if(s[i] + zmiana > 90){s[i] = s[i] + zmiana - 26;}
            else{s[i] = s[i] + zmiana;}
        }
        else{s[i] = s[i];}}
    }
    return s;
}

Employee* readmployes(char* fname){
    FILE *file;
    int n;
    int m;
    file = fopen(fname, "r");

    if(file == NULL){
        perror("Error: \n");
    }

    if(feof(file)){
        printf("file is empty\n");
        return NULL;
    }

    fscanf(file, "%d %d", &n, &m);
    printf("n = %d  m = %d\n\n", n, m);

    Employee tab[n];

    for(int i = 0; i<n; i++){
        fscanf(file, "%s %s %s %f", decipher(tab[i].f_name, -m, 30), tab[i].l_name, tab[i].b_date, &tab[i].salary);
        printf("%s, %s, %s, %f\n", tab[i].f_name, decipher(tab[i].l_name, -m, 50), tab[i].b_date, tab[i].salary);
    }

    fclose(file);

    return tab;
}

int main(){
    readmployes("Dane2024.txt");
    return 0;
}