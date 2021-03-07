;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname TP1-Pitinari-Quintero) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "htdp")) #f)))
#|
Trabajo Práctico 1: Receta para el diseño

Integrantes:
- [Pitinari, Tomas], comisión [4].
- [Quintero, Iago], comisión [4].
|#

; Ejercicio 1

(define (superficie a b c) (+ (* a b) (* 2 b c) (* 2 a c)))

(define (redondear x) (/ (round (* 100 x)) 100) )

(define
  (pintura-necesaria a b c tipo) 
  (redondear (if (= tipo 1) (/ (superficie a b c) 16) (if (= tipo 2) (/ (superficie a b c) 12) (error "tipo: No es una pintura")))))

(check-expect (pintura-necesaria 4 10 1.5 2) 6.83)

(check-expect (pintura-necesaria 30 15 2 1) 39.38)

; Ejercicio 2

(define
  (chequeo-pintura a b c tipo baldes)
  (if (> (- (pintura-necesaria a b c tipo) (* 2 baldes)) 0) ;aca chequeamos si sobra o falta pintura
      (string-append "Faltan " (number->string(ceiling (/ (- (pintura-necesaria a b c tipo) (* 2 baldes)) 2))) " baldes") ;este es el caso si falta pintura, por lo que redondeamos para arriba para saber cuantos baldes faltan
      (if (< (/ (- (* 2 baldes) (pintura-necesaria a b c tipo)) 2) 1) ;si sobra pintura, tenemos dos opciones
          "Cantidad justa" ;que la cantidad de baldes sea la justa
          (string-append "Sobran " (number->string(floor (/ (- (* 2 baldes) (pintura-necesaria a b c tipo)) 2))) " baldes")))) ;o si sobró más de 2 litros, por ende un balde o más

(check-expect (chequeo-pintura 3 7 1.3 1 4) "Sobran 2 baldes")

(check-expect (chequeo-pintura 45 13 4 2 9) "Faltan 35 baldes")

(check-expect (chequeo-pintura 4 10 1.7 1 3) "Cantidad justa")

; Ejercicio 3
#|
La función del apartado 1 resulto de utilidad para el segundo,
ya que para saber cuantos baldes se requiere para pintar una
pileta necesitamos saber cuanta pintura se necesita para pintar esta.
Si no se hubiese pedido la función del apartado uno hubiésemos tenido
que calcular los litros de pintura dentro de la función del apartado 2.
Extraerla y usarla como una función auxiliar hace al código más
prolijo además de posibilitar la reutilización de código dentro
del programa, en el caso que se tenga que volver a calcular la
cantidad de pintura de función una pileta o calcularla muchas
veces en el mismo apartado.
|#