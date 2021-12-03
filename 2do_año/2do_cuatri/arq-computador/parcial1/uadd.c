#include <stdlib.h>
#include <stdio.h>

int uadd_ok(unsigned x, unsigned y){
	unsigned limit = 0xffffffff;	//unsigned con 32 bits en 1 (numero mas grande)
	printf("Numero mas grande posible: %u\n",limit);
	limit -= x;
	if(limit < y){
		return 0;	//hay desbordamiento
	}
	return 1;	//cualquier otro caso no
}

int main(){
	printf("uadd_ok: %d\n",uadd_ok(4000000000,1000000000));
	return 0;
}
