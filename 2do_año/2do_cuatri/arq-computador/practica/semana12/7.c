#include <stdlib.h>
#include <stdio.h>

void sum(float *a, float *b, int len);

int main(){
    float a[3], b[3];
    for(int i=0; i<3; i++){
        a[i]=(float)i;
        b[i]=(float)i;
    }
    sum(a,b,3);
    for(int i=0; i<3; i++){
        printf("arreglo a en %d: %f\n",i,a[i]);
    }
    return 0;
}