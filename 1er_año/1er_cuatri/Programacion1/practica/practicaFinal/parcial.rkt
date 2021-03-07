;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname parcial) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp")) #f)))
#|
;necesitamos una funcion que dada una lista de numeros y un numero aparte, devuelva la cantidad de numeros que son mas grandes que este numero aparte
;cuantos-mayores-a: List(Number) Number -> Number
(define (cuantos-mayores-a l x) (cond [(null? l) 0]
                                         [(> (first l) x) (+ 1 (cuantos-mayores-a (rest l) x))]
                                         [else (cuantos-mayores-a (rest l) x)]
                                         ))
(check-expect (cuantos-mayores-a (list 1 6 8 0 8) 5) 3)
(check-expect (cuantos-mayores-a (list 0 1 2 3) 3) 0)

;Defino una funcion que dada una lista de catetos, devuelva la suma de las hipotenusas de los catetos que formen relaciones pitagoricas
;f: List(posn) -> Number
(define (f l) (foldr + 0 (map (lambda (x) (if (integer? (sqrt (+ (sqr (posn-x x)) (sqr (posn-y x))))) (sqrt (+ (sqr (posn-x x)) (sqr (posn-y x)))) 0)) l)))

(check-expect (f (list(make-posn 4 3)(make-posn 1 2)(make-posn 7 24))) 30)
(check-expect (f (list(make-posn 4 4)(make-posn 1 2)))0)

;estructura del producto
(define-struct producto [nombre precio cantidad])

;defino una funcion que calcula el monto total del producto en el stock
;monto-en-stock: producto -> Number
(define (monto-en-stock x) (* (producto-precio x) (producto-cantidad x)))

(check-expect(monto-en-stock(make-producto "leche" 24.5 6))147)
(check-expect(monto-en-stock(make-producto "jabón" 30 2))60)

;defino una funcion que dado dos productos con el miusmo nombre, devuelve un solo producto fusionado, o un cartel de error
;actualizar-stock: producto producto -> producto
(define (actualizar-stock a b) (cond
                                 [(string=? (producto-nombre a) (producto-nombre b)) (make-producto (producto-nombre a) (/ (+ (producto-precio a) (producto-precio b)) 2) (+ (producto-cantidad a) (producto-cantidad b)))]
                                 [else (error "los productos no comparten nombre")]
                                 ))

(check-expect (actualizar-stock (make-producto "leche" 20 5)(make-producto "leche" 30 2))(make-producto "leche" 25 7))
|#













