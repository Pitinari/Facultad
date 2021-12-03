.global main
main:
    movl $1, %eax
    shll $31, %eax
    movl $1, %ebx
    shll $15, %ebx
    xorl %ebx, %eax
    ret
