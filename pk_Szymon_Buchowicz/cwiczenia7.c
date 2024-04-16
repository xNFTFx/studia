#include <stdio.h>

int find_char(char* s, char c){
    int i = -1, j;
    for(j=0; s[i]!= '\0' && s[j] != c; j++)
    if(s[j] ==c ){i=j+1;}
    return 1;
}
int cyfra_w_liczbie(int x, int b){
    while (x>0)
    {
        if(x%10 == b){return 1; break;}
        x = x/10;
    }
    return 0;
}

void liczby_z_cyfra(int* a, int n, int b){
    for(int i = 0; i < n; i++){
        if(cyfra_w_liczbie(a[i], b) == 1)
        {
            printf("%d\n", a[i]);
        }
        
    }
}

void wyrazy_w_zdaniu(char* s)
{
    
}

int main(){
    int tab[] = {13, 32, 3124, 1234, 2314, 3, 35246, 312, 123, 4234, 12456, 9324};
    liczby_z_cyfra(tab, 12, 6);
    return 0;
}