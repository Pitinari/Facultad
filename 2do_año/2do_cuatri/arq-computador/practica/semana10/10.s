.global setjmp2
setjmp2:   # jmp_buf en rdi
    pop	%rcx
	movq %rcx, (%rdi)
	movq %rsp, 8(%rdi)
	movq %rbp, 16(%rdi)
	movq %rbx, 24(%rdi)
	movq %r12, 32(%rdi)
	movq %r13, 40(%rdi)
	movq %r14, 48(%rdi)
	movq %r15, 56(%rdi)
	xorq %rax, %rax	
	jmpq *%rcx

.global longjmp2
longjmp2:   # jmp_buf en rdi
    movq (%rdi), %rcx
	movq 8(%rdi), %rsp
	movq 16(%rdi), %rbp
	movq 24(%rdi), %rbx
	movq 32(%rdi), %r12
	movq 40(%rdi), %r13
	movq 48(%rdi), %r14
	movq 56(%rdi), %r15

    movq	%rsi, %rax	# valor de retorno en rsi
	testq	%rax, %rax	# no debe retornar 0
	jnz	cero
	incq	%rax		# retornar 1
cero:
	jmpq	*%rcx
