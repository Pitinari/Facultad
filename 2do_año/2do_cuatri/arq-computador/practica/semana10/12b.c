#include "guindows.h"
#include <stdio.h>

static task t1, t2, t3, taskmain;

static void ft1(void){
    int var1;
    printf("direccion de var1: %p\n", &var1);
    for (double d = -1; ; d += 0.001) {
        printf("t1: d=%f\n", d);
        TRANSFER(t1, t2);
    }
}

static void ft2(void){
    int var2;
    printf("direccion de var2: %p\n", &var2);
    for (unsigned i = 0; i < 10000; i++) {
        printf("t2: i=%u\n", i);
        TRANSFER(t2, t3);
    }
    TRANSFER(t2, taskmain);
}

void ft3(void){
    int var3;
    printf("direccion de var3: %p\n", &var3);
    for (unsigned i = 0; i < 50; i++) {
    printf("t3: i=%u\n", i);
    TRANSFER(t3, t1);
    }
    TRANSFER(t3, taskmain);
}

int main(void)
{
    stack(t1, ft1);
    stack(t2, ft2);
    stack(t3, ft3);
    TRANSFER(taskmain, t1);
    return 0;
}
