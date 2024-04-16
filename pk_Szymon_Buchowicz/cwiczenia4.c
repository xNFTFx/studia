#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>


#define EPS = 1.0e-5

double pieviete(int n){
    long double pi = 2;
    long double q = sqrt(2)/2;
    int i =0;
    while (i<n) //chciałem zrobić z tym epsilonem, a pozniej nie chcialem wracac do fora ;)
    {
        pi = pi/q;
        q = sqrt(2+ q*2)/2;
        i++;
    }
    return pi;
}

double sqrt_of_x(double x){
    double s = 1;
    while (s*s < x)
    {
        s = (s+x)/s;
        printf("%f, %f", s, x);
    }
    return s;
}

int sumofdigits(unsigned int number){
    int sum = 0;
    while(number > 0){
        sum += number%10;
        number = number/10;
    }
    return sum;
}

void zad3a(){
   int tab[] = {78, 34, 123, 678, 34, 567, 1023, 5869, 5, 435, 546, 666, 999};
   int length = sizeof(tab)/sizeof(*tab);
   for(int i = 0; i< length; i++){
        printf("Suma cyfr liczby %d to %d\n", tab[i], sumofdigits(tab[i]));
   }
}


void numbersbin111(){
    int n = 1; 
    while (n <= 5000) {
        if ((n & (n + 1)) == 0) {
            printf("%d \n", n);
        }
        n++;
    }
}

unsigned int digitsqrt(unsigned int a) {
    while(a > 0){
        if(a <10){return a; break;}
        a = sumofdigits(a);
    }
    return 0;
}


int zdanie(char* s) {
    int count = 0;
    while (*s) {
        if (isupper(*s)) {
            count++;
        }
        s++;
    }
    return count;
}

void test_zdanie() {
    char sentence[100];
    printf("Wpisz zdanie: ");
    fgets(sentence, sizeof(sentence), stdin); // mozliwe ze z powodu pracy na vs code nie dzialala mi funkcja gets_s, ale z tego co szukałem w internecie najlepiej jest wtedy uzcyc fgets

    if (sentence[sizeof(sentence) - 1] == '\n') {
        sentence[sizeof(sentence) - 1] = '\0';
    }

    int result = zdanie(sentence);
    printf("Liczba duzych liter w zdaniu: %d\n", result);
}

int main(){
    test_zdanie();
    return 0;
}