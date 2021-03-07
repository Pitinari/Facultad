;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname TP5-Pitinari-Quintero) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp")) #f)))
#|
Trabajo Práctico 5: Naturales

Integrantes:
- [Pitinari, Tomas], comisión [4].
- [Quintero, Iago], comisión [4].
|#


;;;;;;;; Ejercicio 1

; [Completar]

;Definimos una funcion que tome un natural como unico parametro, en representacion de la cantidad de escalones, y devuelva la cantidad de formas posibles de subir la escalera
;subir: Natural -> Number

(check-expect (subir 4) 3)
(check-expect (subir 7) 12)

(define (subir x) (cond
                    [(> 3 x) 1]
                    [(= x 3) 2]
                    [(= x 4) 3]
                    [(= x 5) 5]
                    [else (+
                           (subir (- x 1))
                           (subir (- x 3))
                           (subir (- x 5))
                          )]
                    ))
;;;;;;;; Ejercicio 2

;;;; Ejercicio 2-1

; Costo de los recorridos válidos:
; * [21]
; * [20]
; * [12]
; * [20]
; * [21]
; * [-2]
; * [18]
; * [17]
; * [18]
; * [13]

;;;; Ejercicio 2-2
#|
                    /    tab[0][0]     si i = 0, j = 0
                    |   [(+ tab[i][j] (maximoCosto(i, (- j 1))))]    si i = 0, j != 0
maximoCosto(i, j) = <
                    |   [(+ tab[i][j] (maximoCosto((- i 1), j)))]    si i != 0, j = 0
                    \   [(max (+ tab[i][j] (maximoCosto((- i 1), j))) (+ tab[i][j] (maximoCosto(i, (- j 1)))))]    si i != 0, j != 0
|#

;;;; Ejercicio 2-3

(define TABLERO (list (list -5 10) (list 0 -2) (list 9 3)))

; [COMPLETAR]

;definimos auxiliarmente una funcion que dados dos indices, representados como numeros naturales, delvolver el elemento en su posicion en una lista de listas
;buscar-tabla: Natural Natural List(List(Number)) -> Number

(check-expect (buscar-tabla  1 2 (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) 6)
(check-expect (buscar-tabla 1 0 (list (list 1 2 3) (list 4 5 6) (list 7 8 9))) 4)

(define (buscar-tabla x y xss) (cond
                                 [(or (>= x (length xss)) (< x 0)) (error "indice fuera de rango")]
                                 [(zero? x) (cond
                                              [(or (>= y (length (first xss))) (< y 0)) (error "indice fuera de rango")]
                                              [(zero? y) (first(first xss))]
                                              [else (buscar-tabla x (sub1 y) (list (rest (first xss))))]
                                 )]
                                 [else (buscar-tabla (sub1 x) y (rest xss))]
                               ))

;Ahora vamos a definir una funcion que determine el costo mas alto de un camino en una tabla, representada por una lista de listas de eneteros
;maximo-costo: List(List(Number)) Natural Natural -> Number

(check-expect (maximo-costo TABLERO 1 2) 7)
(check-expect (maximo-costo TABLERO 1 1) 3)
(check-expect (maximo-costo (list (list 5 4 -10 15) (list 1 -2 8 2) (list -22 9 1 4)) 3 2) 21)


(define (maximo-costo tab i j) (cond
                                 [(and (zero? i) (zero? j)) (buscar-tabla j i tab)]
                                 [(zero? i) (+ (buscar-tabla j i tab) (maximo-costo tab i (sub1 j)))]
                                 [(zero? j) (+ (buscar-tabla j i tab) (maximo-costo tab (sub1 i) j))]
                                 [else (max
                                        (+ (buscar-tabla j i tab) (maximo-costo tab i (sub1 j)))
                                        (+ (buscar-tabla j i tab) (maximo-costo tab (sub1 i) j)))]
                               ))

;;;; Ejercicio 2-4

; [COMPLETAR]

;Para definir esta funcion, pedimos como parametro un tablero, de n columnas y m filas y queremos saber cual es el costo maximo de un recorrido valido en ese tablero, lo que implica llamar a la funcion anterior con el tablero n-1 y m-1 como parametros
;maximo-costo-tablero: List(List(Number)) -> Number

(check-expect (maximo-costo-tablero TABLERO) 7)
(check-expect (maximo-costo-tablero (list (list 5 4 -10 15) (list 1 -2 8 2) (list -22 9 1 4))) 21)

(define (maximo-costo-tablero tablero) (maximo-costo tablero (sub1 (length (first tablero))) (sub1 (length tablero))))