#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ZNAK(x, y) (x) * (y) >0 ? 1: ((x)+(y))%2 == 0 ? (x) : (y)

int main(){
    printf("%d", ZNAK(-3, 8));
    srand((unsigned int)time(0));
    int x = rand() %100;
    printf("\n%d", x);
    return 0;
}