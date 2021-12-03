#include <stdlib.h>
#include <stdio.h>

int a;
int f(int b, double c, int e) {
	int d = 42069;
	printf("%p\n", &c);
	return a+d+e;
}

int main(){
	f(4,1.2,5);
	return 0;
}
