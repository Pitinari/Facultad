.data
.text
.global main
main:
	movq $0xA0A0A0A0E0E0E0E0 ,%rax
	ror $32, %rax
	ret
