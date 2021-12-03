.data
format: .asciz "%ld\n"
formatHex: .asciz "%lX\n"
i: .quad 0xDEADBEEF

.text
.global main
main:
movq $format, %rdi 	# El primer argumento es el formato.
movq $1234, %rsi	# El valor a imprimir.
xorq %rax, %rax 	# Cantidad de valores de punto flotante.
call printf

#a
movq $format, %rdi
movq (%rsp), %rsi
xorq %rax, %rax
call printf

#b
movq $format, %rdi
movq $format, %rsi
xorq %rax, %rax
call printf

movq $formatHex, %rdi
movq $format, %rsi
xorq %rax, %rax
call printf

#El item d se puede saltear ya que es lo mismo que en el item a

movq $format, %rdi
movq 8(%rsp), %rsi
xorq %rax, %rax
call printf

movq $format, %rdi
movq (i), %rsi
xorq %rax, %rax
call printf

movq $format, %rdi
movq $i, %rsi
xorq %rax, %rax
call printf

xorq %rax, %rax

ret
