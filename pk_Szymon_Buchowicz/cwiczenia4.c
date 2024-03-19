#include <stdio.h>
#include <math.h>

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
int bin_to_dec(int bin){
    int dec = 0;
    int q = 1;
    while (bin> 0)
    {
        dec += bin%10 * q;
        q*=2;
        bin/=10;
    }
    return dec;
    
}
void numbersbin111(){

}


int main(){
    // printf("%d", bin_to_dec(1110));
    sqrt_of_x(15);
    return 0;
}