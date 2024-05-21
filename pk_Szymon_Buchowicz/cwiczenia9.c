#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <float.h>
#include <string.h>
#include "cwiczenia9.h"


double f1(double x){
    return x*x;
}

double mcarloint(double (*f)(double), double a, double b, int n){
    double sum = 0;
    srand((unsigned int)time(0));
    for(int i =0; i < n; i++){
        double t = (double)rand() / RAND_MAX;
        double x = a*(1-t) + b*t;
        sum +=f(x);
    }
    return (b-a)*sum/n;
}

double trapezinit(double (*f)(double), double a, double b, int n)
{
    double h = (b-a) / n;
    double res = 0, x = a;

    for(int i = 0; i <n; i++){
        res += (f(x) + f(x+h))*h;
        x+=h;
    }
    res /=2;
    return res;

}

// double simpsonint(double (*f)(double), double a, double b, int n){
//     return 0;
// }

void test_integral(){
    int n =1000;
    printf("Wynik: %f\n", trapezinit(f1, 0, 10, n));    
    printf("Wynik: %f\n", mcarloint(f1, 0, 10, n));

}

int cmplast_names(const void *a, const void *b){
    Person p1 = *((Person*)a);
    Person p2 = *((Person*)b);
    return strcmp(p1.nazwisko, p2.nazwisko);
}
int cmpfirst_names(const void *a, const void *b){
    Person p1 = *((Person*)a);
    Person p2 = *((Person*)b);
    return strcmp(p1.imie, p2.imie);
}


void print_persons(Person p[], int n){
    for (int i =0; i < n; i++){
        printf("%s %s wzrost %d\n", p[i].imie, p[i].nazwisko, p[i].wzrost);
    }
}

void sort_persons(Person p[], int n){
    qsort(p, n, sizeof(Person), cmpfirst_names);
    print_persons(p, n);
}

void test_person(){
    Person persons[] = {{"Adam", "Nowak", niski}, {"Jan", "Kowalski", sredni}, 
    {"Barbara", "Gorska", wysoki}, {"Kacper", "Benger", wysoki}, 
    {"Marek", "Kowalski", sredni}, {"Kacper", "Benger", niski}};
    int n = sizeof(persons)/sizeof(persons[0]);
    sort_persons(persons, n);
}


int main(){
    test_person();
}