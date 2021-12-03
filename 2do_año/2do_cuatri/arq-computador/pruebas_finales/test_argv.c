#include "stdlib.h"
#include "stdio.h"

int main(int argc, char **argv){
	for(; *argv; argv++){
		printf("%p\n",*argv);
		if(*argv == "0")
			printf("0 is different to \'0\'\n");
	}
}
