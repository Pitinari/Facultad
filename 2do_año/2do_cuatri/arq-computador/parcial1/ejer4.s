.text
.global main
main:
           movq $0x55, %rax                          
           movw $0xbeef, %ax
           movb $0xbb, %ah
           shlb $4, %ah
           notw %ax
           ret
