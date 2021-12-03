.data
i: .quad 4

.text
.global main
main:
	movq ($i), %rax
	ret
