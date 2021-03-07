;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname practica1) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
;1(define (anchura x) (if (< (image-width x) (image-height x)) "flaca" "gorda"))
;(anchura (rectangle 30 20 "solid" "red"))

;2(define (anchura x) (if (= (image-width x) (image-height x)) "cuadrada" (if (< (image-width x) (image-height x)) "flaca" "gorda")))
;(anchura (rectangle 30 30 "solid" "red"))

;3(define (triangulos x y z) (if (= x y z) "equilatero" (if (or (= x y) (= y z) (= z x)) "isosceles" "escaleno")))
;(triangulos 60 50 40)

;4(define (triangulos x y z) (if (= (+ x y z) 180)(if (= x y z) "equilatero" (if (or (= x y) (= y z) (= z x)) "isosceles" "escaleno")) "error"))
;(triangulos 60 70 50)

;(define PC 60)
;(define PL 8)
;5(define (promos c l) (+ (if (<= 5 l) (* l PL 0.85) (* l PL)) (if (<= 4 c) (* c PC 0.9) (* c PC)) ))
;(promos 3 4)

;6(define (promoMayor c l) (if (>= (+ c l) 10) (if (>= (* 0.82 (+ (* c PC) (* l PL))) (promos c l)) (* 0.82 (+ (* c PC) (* l PL))) (promos c l)) (promos c l)))
;(promoMayor 5 5)

;7(define (pitagorica2? a b c) (if (= (sqr a) (+ (sqr b) (sqr c))) #t (if (= (sqr b) (+ (sqr a) (sqr c))) #t (if (= (sqr c) (+ (sqr b) (sqr a))) #t #f))))
;(pitagorica2? 5 4 5)

(define
  (pitagorica3? a b c)
  (if
   (= (sqr a) (+ (sqr b) (sqr c)))
   (string-append "Los números " (number->string a) ", "(number->string b)" y " (number->string c) " forman una terna pitagórica.")
   (if
    (= (sqr b) (+ (sqr a) (sqr c)))
    (string-append "Los números " (number->string a) ", "(number->string b)" y " (number->string c) " forman una terna pitagórica.")
    (if
     (= (sqr c) (+ (sqr b) (sqr a)))
     (string-append "Los números " (number->string a) ", "(number->string b)" y " (number->string c) " forman una terna pitagórica.")
     (string-append "Los números " (number->string a) ", "(number->string b)" y " (number->string c) " no forman una terna pitagórica.")))))
(pitagorica3? 3 4 5)

(number->string 1 17)

;9(define (collatz x) (if (= 0 (modulo x 2)) (/ x 2) (+ (* 3 x) 1)))
;(collatz 7)