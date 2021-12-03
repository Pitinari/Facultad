.global main
main:
    movl $0, %eax
    movl $1, %ebx
    subl %ebx, %eax
    ret
