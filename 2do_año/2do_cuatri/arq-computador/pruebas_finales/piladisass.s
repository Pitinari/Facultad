.global main
main:
pushq %rbp
movq %rsp, %rbp
pushq $0x300
pushq $0x200
pushq $0x100
movq $5, %rdi
movq $10, %rsi
call suma
# xorq %rax, %rax # <- Esta dir puede denotarse RA_f
movq %rbp, %rsp
popq %rbp
retq
.global suma
suma:
pushq %rbp
movq %rsp, %rbp
addq %rdi, %rsi
addq 16(%rbp), %rsi
movq %rsi, %rax
movq %rbp, %rsp
popq %rbp
retq
