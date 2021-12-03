#include <stdio.h>
#include "guindows.h"

task t1, t2, taskmain;

void ft1(){
	double d;
	for(d=-1;;d+=0.001) {
		printf("d=%f\n", d);
		TRANSFER(t1,t2);
	}
}

void ft2(){
	int i;
	for(i=0;i<10000;i++) {
		printf("i=%d\n", i);
		TRANSFER(t2,t1);
	}
	TRANSFER(t2, taskmain);
}

main(){
	stack(t1,ft1);
	stack(t2,ft2);
	TRANSFER(taskmain,t1);
	return 0;
}
