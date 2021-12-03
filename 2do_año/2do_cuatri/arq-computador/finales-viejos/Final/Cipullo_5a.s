# Codigo en C
# int main(int argc, char **argv){
#        printf("%d %p\n", argc, argv);
#        return argc;
# }

    .data
formato: .asciz "%d %p\n"


    .text
    .global main
main:
    movq %rsi, %rdx # rdx guarda argv (puntero), 3er argumento
    movq %rdi, %rsi # rsi guarda argc, 2do argumento
    pushq %rsi # guarda el valor de argc en la pila
    movq $formato, %rdi # rdi guarda el formato, 1er argumento
    xorq %rax, %rax
    call printf

    popq %rax # guardo argc en rax para retornarlo
    ret
