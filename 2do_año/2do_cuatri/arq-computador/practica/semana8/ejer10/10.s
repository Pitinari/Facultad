.data

.text
# setJump espera recibir una direccion de memoria apuntando a 2 palabras, en la primera
# almacenamos la direccion de la instruccion que llamo a setJump y en la segunda
# se almacenara el valor de retorno
.global setjmp2
setjmp2:
	popq %rbx
	movq %rbx, %rdi
	movq 8(%rdi), %rax
	jmp *%rbx

# longJump espera recibir la misma direccion de memoria apuntando a 2 palabras, guarda
# en la segunda palabra el valor de retorno y salta a la direccion
# especificada en la 1er palabra
.global longjmp2
longjmp2:
	popq %rbx
	movq %rsi, 8(%rdi)
	jmp *%rdi
