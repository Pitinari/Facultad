#include <stdlib.h>
#include <setjmp.h>

#define TPILA 4096
#define NPILAS 10 //hasta 10 corrutinas

static void hace_stack(jmp_buf buf, void (*pf)(), unsigned prof, char *dummy) {
	if( dummy - (char *) &prof >= prof) { //prof va a estar dentro del marco de act porque pedi la dirección //si evalua a true, llegue a la prof que queria
		if (setjmp(buf)!=0) {
			pf(); abort();
		}
	} else hace_stack(buf, pf, prof, dummy);
}

void stack(jmp_buf buf, void (*pf)()) {
	static int quedan = NPILAS;
	char dummy;
	hace_stack(buf, pf, TPILA *quedan, &dummy);
	quedan--;
}
