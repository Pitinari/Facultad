# int solve(float a, float b, float c, float d, float e, float f, float *x, float *y);
# que resuelva el sistema de ecuaciones:
# ax + by = c
# dx + ey = f

.global solve
solve: # xmm 0 = a, 1 = b, 2 = c, 3 = d, 4 = e, 5 = f
  xorps %xmm6, %xmm6
  comiss %xmm0, %xmm6
  jz invalido
  mulss %xmm0, %xmm5 # xmm5=af
  movss %xmm3, %xmm6 # xmm6=d
  mulss %xmm2, %xmm3 # xmm3=dc
  subss %xmm3, %xmm5 # xmm5=af-dc
  mulss %xmm0, %xmm4 # xmm4=ea
  mulss %xmm1, %xmm6 # xmm6=bd
  subss %xmm6, %xmm4 # xmm4=ea-bd
  xorps %xmm7, %xmm7
  comiss %xmm4, %xmm7
  jz invalido
  divss %xmm4, %xmm5 # xmm5=(af-dc)/(ea-bd)
  mulss %xmm5, %xmm1 # xmm1=by
  subss %xmm1, %xmm2 # xmm2=c-by
  divss %xmm0, %xmm2 # xmm2=(c-by)/a
  movss %xmm2, (%rsi)
  movss %xmm5, (%rdi)
  xorq %rax, %rax
  ret

invalido:
  movq $-1, %rax
  ret
