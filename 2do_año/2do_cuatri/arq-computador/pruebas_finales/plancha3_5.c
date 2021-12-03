#include <stdio.h>
#include <stdlib.h>

int main(){
	void *a = malloc(sizeof(float));
	void *b = malloc(sizeof(float));
	*a = 0b00011000010100000000000000000000;
	*b = 0b00011000011000000000000000000000;
	printf("%f\n",(float*)*a + (float*)*b);
	return 0;
}
