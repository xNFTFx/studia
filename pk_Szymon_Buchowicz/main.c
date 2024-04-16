#include <stdio.h>

void test_cmd(char* d[]){
    int x, y;
    if (sscanf(d[1], "%d", &x)<1 || sscanf(d[2], "%d", &y)<1){
        printf("zle dane\n"); return;
    }
    printf("%d + %d = %d", x, y, x+y);
}

int main(int argc, char* argv[]){
    if(argc == 3){
        printf("wynik dzialania programu:\n%s\n", argv[0]);
        test_cmd(argv);
    }
    return 0;
}

