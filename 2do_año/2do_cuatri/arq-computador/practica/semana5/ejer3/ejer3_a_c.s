.global main
main:
    movl $-1, %eax
    movl $-256, %ebx
    andl %ebx, %eax
    ret
