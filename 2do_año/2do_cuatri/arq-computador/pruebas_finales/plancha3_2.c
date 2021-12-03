#include <stdio.h>
#include <ieee754.h>
#include <math.h>
int getFloatExponent(float f){
return (((*(int*)&f) & 0x7F800000) >> 23);
}
int getFloatMantissa(float f){
return ((*(int*)&f) & 0x007FFFFF);
}
//a
int myIsNaN(float f) {
if (getFloatExponent(f) == 255 && getFloatMantissa(f) != 0) {
return 1;
}
return 0;
}
//b
int myIsNaN2(float f) {
return f != f;
}
int main()
{
/*union ieee754_float f = NAN;
int fraccion = f.ieee.exponent;*/
printf("%d \n", getFloatExponent(NAN));
printf("%d \n", getFloatMantissa(NAN));
printf("nan1 \n");
printf("%d \n", myIsNaN(NAN));
printf("%d \n", myIsNaN(3.4));
printf("nan2 \n");
printf("%d \n", myIsNaN2(NAN));
printf("%d \n", myIsNaN2(3.4));
//c
float f = INFINITY;
printf("inf == inf: %d\n", f == f);
printf("INFINITY == INFINITY: %d\n", INFINITY == INFINITY);
//d
printf("10 + INFINITY == INFINITY: %d\n",10+INFINITY == INFINITY);
printf("INFINITY + INFINITY == INFINITY: %d\n",INFINITY+INFINITY == INFINITY);
printf("NAN + INFINITY == NAN: %d\n",isnan(NAN+INFINITY));
return 0;
}
