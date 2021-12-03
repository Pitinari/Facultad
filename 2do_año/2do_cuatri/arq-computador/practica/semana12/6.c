#include <stdlib.h>
#include <stdio.h>

int solve(float a, float b, float c, float d, float e, float f, float *x, float *y);

int main(){
    float a=0, b=1, c=1, d=2, e=1, f=2, x, y;
    if(solve(a,b,c,d,e,f,&x,&y) == 0){
        printf("Las incognitas de la ecuacion son: X=%f \t Y=%f\n",x,y);
    }
    else{
        printf("La ecuacion no una unica solucion, o no la tiene\n");
    }
    return 0;
}