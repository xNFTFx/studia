#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

#define MAX 10

inline void println(){
    printf("/n");
}

void swap(int* x, int *y){
    *x = *x ^ *y;
    *y = *x ^ *y;
    *x = *x ^ *y;
}

void test_swap(){
    int x = 10, y = 20;
    printf("x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("x = %d, y = %d\n", x, y);
}

void bubble_sort(int a[], int n){
    for (int i = 0; i<n-1; i++){
        for(int j = 0; j<n-1-i; j++){
            if(a[j] > a[j+1]){
                swap(&a[j], &a[j+1]);
            }
        }
    }
}

void test_bubble_sort(){
    int tab[MAX];
    srand((unsigned)time(0));
    for(int i = 0; i<MAX; i++){
        tab[i]  = rand() % (80+1)+10;
        printf("%d\n", tab[i]);
    }

    bubble_sort(tab, MAX);
    printf("\njuz posortowane \n\n");

    for(int i = 0; i<MAX; i++){
        printf("%d\n", tab[i]);
    }

}

int imie_na_litere(char name[], char letter){
    if(letter == name[0]){
        return 1;
    }
    return 0;
}

void test_imie_na_litere(){
    char* imiona[] = {"Szymon", "Amelia", "Piotr", "Kornelia", "Jaroslaw", "Pawel", "Kacper"};
    int ilosc_imion = 5;
    char litera;

    printf("Podaj litere, na ktora maja zaczynac sie imiona: ");
    scanf(" %c", &litera);

    printf("Imiona rozpoczynajace sie na litere '%c':\n", litera);
    for (int i = 0; i < ilosc_imion; i++) {
        if (tolower(imiona[i][0]) == tolower(litera)) {
            printf("%s\n", imiona[i]);
        }
    }
}

int partition(int array[], int low, int high) {
    int pivot = array[low];
    int left = low;
    int right = high;

    while (left <= right) {
        while (array[left] < pivot) {
            left++;
        }

        while (array[right] > pivot) {
            right--;
        }

        if (left <= right) {
            swap(&array[left], &array[right]);
            left++;
            right--;
        }
    }

    return left;
}

void quicksort(int array[], int low, int high) {
    if (low < high) {
        int pi = partition(array, low, high);
        quicksort(array, low, pi - 1);
        quicksort(array, pi, high);
    }
}

int main(){
    test_imie_na_litere();
    return 0;
}