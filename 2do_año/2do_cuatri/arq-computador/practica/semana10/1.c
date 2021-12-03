#include <stdlib.h>
#include <stdio.h>
#include <ieee754.h>

int parte_frac (float f){
  return (*(int*)&f) & 0x007FFFFF;
}

int parte_exp (float f){
    return (((*(int*)&f) & 0x7F800000) >> 23);
}

int main (){
    float f = 1.2;
    union ieee754_float fl;
    fl.f = f;
    printf("Funciones propias:\n");
    printf("Exponente: %d, Fracci\'on: %x\n", parte_exp(f), parte_frac(f));
    printf("Funciones de ieee754.h:\n");
    printf("Exponente: %d, Fracci\'on: %x\n", fl.ieee.exponent, fl.ieee.mantissa);
    return 0;
}
