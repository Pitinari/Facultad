.global main
main:
	movb $0xaa, %al
	salb $1, %al # al=0x54
	ret
