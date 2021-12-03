#include <stdio.h>
#include <setjmp.h>

jmp_buf BufferA= {0, 0, 0};

int setjmp2(jmp_buf env);
void longjmp2(jmp_buf env, int val);

int main(){
    int r = setjmp2(BufferA);
    printf("%d",r);
    if( r==0 )  {longjmp2(BufferA,1);}
    return 0;
}