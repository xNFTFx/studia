#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef long long int llong;

void swap(int* x, int *y){
    *x = *x ^ *y;
    *y = *x ^ *y;
    *x = *x ^ *y;
}

void simple_sort(int a[], int n) 
{
	for (int i = 0; i < n - 1; ++i) {
		int k = i;
		for (int j = i + 1; j < n; ++j) {
			if (a[j] < a[k]) {
				k = j;
			}

		}
		if (i != k) {
			swap(&a[i], &a[k]);
		}
	}
}


int factorial_rec(int num){
    if(num == 1){
        return num;
    }
    else{ return num* factorial_rec(num-1);}
}

int nwd(int a, int b) 
{

	return b == 0 ? a : nwd(b, a % b);
}

int znajdz_pierwsza_cyfre(char *napis, int index) {
    if (napis[index] == '\0')
        return -1; // Jeśli nie znaleziono żadnej cyfry w napisie, zwracamy -1
    
    if (napis[index] >= '0' && napis[index] <= '9') {
        printf("Znaleziono cyfre '%c'", napis[index]);
        return index; // Zwracamy indeks, jeśli znaleziono cyfrę
    }
    
    return znajdz_pierwsza_cyfre(napis, index + 1); // Rekurencyjnie szukamy dalej
}


void szachownica()
{
	int tablica[10][10];

	
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			if ((i + j) % 2 == 0) {
				tablica[i][j] = 1;
			}
			else {
				tablica[i][j] = 0;
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			printf("%d ", tablica[i][j]);
		}
		printf("\n");
	}
}


int main(){
    znajdz_pierwsza_cyfre("dupabiskupa4",0);
    return 0;
}
