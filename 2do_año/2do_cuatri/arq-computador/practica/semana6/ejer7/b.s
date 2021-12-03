.global main
main:
	movq $0xffffffffffffffff, %rax     #numero
	xorq %rbx, %rbx   #iteraciones
	xorq %rcx, %rcx   #resultado final
	jmp while
	
while:
    cmpq $64, %rbx
    jz fin
    jmp cuerpo
cuerpo:
    ror $1, %rax
    incq %rbx
    adc $0, %rcx
    jmp while
fin:
    ret
