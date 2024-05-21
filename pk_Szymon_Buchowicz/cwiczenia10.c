#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int liczba_znakow(FILE *fp)
{
    int counter = 0;
    char c;
    while(!feof(fp)){
        if (fscanf(fp, "%c", &c, sizeof(c))){
            counter++;
        }
    }
    return counter;
}

void tests(char *fnames[], int n) {
    FILE *file;
    for (int i = 0; i < n; i++) {
        file = fopen(fnames[i], "r");
        if (file == NULL) {
            printf("%s : Cannot open file\n", fnames[i]);
        } else {
            printf("%s : %d\n", fnames[i], liczba_znakow(file));
            fclose(file);
        }
    }
}

char* szyfruj(char* s, int p, int n)
{
    char zaszyfrowane[n];
    int zmiana = p%26;

    
    for(int i = 0; i < n; i++){
        if(islower(s[i]))
        {
            if(s[i] + zmiana > 122){zaszyfrowane[i] = s[i] + zmiana - 26;}
            else{zaszyfrowane[i] = s[i] + zmiana;}
        }
        else {if(isupper(s[i]))
        {
            if(s[i] + zmiana > 90){zaszyfrowane[i] = s[i] + zmiana - 26;}
            else{zaszyfrowane[i] = s[i] + zmiana;}
        }
        else{zaszyfrowane[i] = s[i];}}
    }
    printf("%s\n", zaszyfrowane);
    return zaszyfrowane;
}

int main(int argc, char* argv[]){
    // int n = argc - 1;
    // if(n>0){
    //     char **fnames = (char **)malloc(n* sizeof(char*));
    //     if(fnames == NULL){return EXIT_FAILURE;}
    //     for(int i = 0; i<n; i++){
    //         fnames[i] = argv [i+1];
    //     }
    //     tests(fnames, n);
    // }
    
    // return EXIT_SUCCESS;
    
    char slowo[] = "Ola ma kota zzz...";
    int n = sizeof(slowo)/sizeof(slowo[0]);

    szyfruj(slowo, 27, n);
}