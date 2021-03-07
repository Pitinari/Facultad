;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname final) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp")) #f)))
;divisores: Number -> (Number Number -> List(Number))
;La funcion pasada en el enunciado toma un numero y devuelve una lista de numeros llamando a divisores_aux, que son los divisores de el numero del parametro.
(define (divisores n) (divisores_aux n 1))

;divisores_aux: Number Number -> List(Number)
(define (divisores_aux n m) (cond [(= n m) '()]

                                  [else (if (= (modulo n m) 0) (cons m (divisores_aux n (+ m 1))) (divisores_aux n (+ m 1)))]))


;Represente al numero n con el tipo Number y devuelvo los numeros perfectos como una lista de numbers
;perfect-nums: Number -> List(Number)
#|
La idea de lo que hace la funcion es comparar cada numero desde n hasta 6, ya que por el 
enunciado sabemos que 6 es el primer numero perfecto, para ello comparo si el numero por
donde esta la recursion es igual a la suma de sus divisores (funcion dada en el enunciado), si
es verdadero agrego ese numero a la lista, si es false paso al siguiente numero de la recursion
|#
(define (perfect-nums n) (cond
                           [(< n 6) '()]
                           [(= n 6) (list 6)]
                           [else (if (= (foldr + 0 (divisores n)) n)
                                     (cons n (perfect-nums (sub1 n))) (perfect-nums (sub1 n)))]
                             ))

(check-expect (perfect-nums 500) (list 496 28 6))
(check-expect (perfect-nums 10) (list 6))
(check-expect (perfect-nums 10000) (list 8128 496 28 6))
(check-expect (perfect-nums 1) '())