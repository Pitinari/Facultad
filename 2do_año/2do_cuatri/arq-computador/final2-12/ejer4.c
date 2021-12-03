#include <stdlib.h>
#include <stdio.h>

int suma(int a, int b, int c, int d, char e, char f, long int g, long int h){
	return a+b+c+d+e+f+g+h;
}

int main( int argc, char* argv[]){
	int a=argc, b=atoi(argv[1]), c=atoi(argv[2]), d=atoi(argv[3]);
	char e=-5, f= 6;
	long int g=8, h=7;
	printf("Resultado %d\n%d  %s  %s  %s  %d  %d %d  %d\n",suma(a,b,c,d,e,f,g,h),
	a, argv[1],argv[2],argv[3], (int)e, (int)f, (int)g, (int)h);
	return 0;
}
