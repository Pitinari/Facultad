.global sum
sum:
  movq %rdx, %rcx  # len
etiqueta:
  decq %rdx        # i 
  movss (%rdi, %rdx, 4), %xmm0  # a[i]
  movss (%rsi, %rdx, 4), %xmm1  # b[i]
  addss %xmm0, %xmm1            # a[i] + b[i]
  movss %xmm1, (%rdi, %rdx, 4)  # a[i] + b[i]
  loop etiqueta
  ret
  