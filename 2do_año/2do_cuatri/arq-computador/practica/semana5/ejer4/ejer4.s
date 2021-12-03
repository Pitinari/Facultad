.globl main
main:
movl $-1,%eax # Solo para este tama~no el mov pone en 0
# la parte alta del registro.
movl $2, %ecx
imull %ecx

shlq $32, %rdx
orq %rdx, %rax

xorq %rax,%rax
movw $-1,%ax
movw $2, %cx
mulw %cx

movl $0xFFFF0000, %edx
orl %edx, %eax

ret
