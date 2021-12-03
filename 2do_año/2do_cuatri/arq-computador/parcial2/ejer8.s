.data
fmt: .asciz "%d\n"
.text
.global main
main:
        movq $2, %rcx
        leaq (%rsi,%rcx,8), %rax
        movq (%rax), %rax
        movw (%rax), %ax
        xorq %rsi, %rsi
        movw %ax, %si
        movq $fmt, %rdi
        xorq %rax, %rax
        call printf
        ret
