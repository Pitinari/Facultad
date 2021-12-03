.global main
main:
	movq $1, %rax
	movq 8(%rax), %rax
	ret
