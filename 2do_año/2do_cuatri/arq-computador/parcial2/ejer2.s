.global cond
cond:
    cmpq (%rsi), %rdi
    jz fin
    js sumar
fin:
    ret
sumar:
    movq %rdi, (%rsi)
    jmp fin