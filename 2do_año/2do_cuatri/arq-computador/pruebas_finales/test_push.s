.data
a: .quad 0x1122334455667788

.text
.global main
main: 
	push a
	pop %rax
	ret
