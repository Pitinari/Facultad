.global main
main:
    movb $0xa0, %al
    addb $0xbb, %al
    ret

