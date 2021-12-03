.global fact1
fact1:
    movq %rdi, %rax
    movq %rdi, %rbx
    subq $1, %rbx
    jz fin1
    jmp for
for:
    mulq %rbx
    subq $1, %rbx
    jz fin1
    jmp for
fin1:
    ret

.global fact2
fact2:
    movq $1, %rax
factAux:
    pushq %rdi
    decq %rdi
    cmpq $0, %rdi
    jz fin2
    call factAux
fin2:
    popq %rdi
    mulq %rdi
    ret
