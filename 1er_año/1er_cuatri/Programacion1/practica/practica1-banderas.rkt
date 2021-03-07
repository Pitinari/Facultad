;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname practica1-banderas) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp")) #f)))
(define ANCHO 90)
(define ALTO 60)

(define peru (place-image (rectangle (/ ANCHO 3) ALTO "solid" "red") (* (/ 1 6) ANCHO) (/ ALTO 2) (place-image (rectangle (/ ANCHO 3) ALTO "solid" "red") (* (/ 5 6) ANCHO) (/ ALTO 2) (empty-scene ANCHO ALTO))))
peru

(define italia (place-image (rectangle (/ ANCHO 3) ALTO "solid" "green") (* (/ 1 6) ANCHO) (/ ALTO 2) (place-image (rectangle (/ ANCHO 3) ALTO "solid" "red") (* (/ 5 6) ANCHO) (/ ALTO 2) (empty-scene ANCHO ALTO))))
italia

(define (3verticales x y z) (place-image (rectangle (/ ANCHO 3) ALTO "solid" x) (* (/ 1 6) ANCHO) (/ ALTO 2) (place-image (rectangle (/ ANCHO 3) ALTO "solid" y) (* (/ 3 6) ANCHO) (/ ALTO 2) (place-image (rectangle (/ ANCHO 3) ALTO "solid" z) (* (/ 5 6) ANCHO) (/ ALTO 2) (empty-scene ANCHO ALTO)))))
(3verticales "green" "white" "red")

(define alemania (place-image (rectangle ANCHO (/ ALTO 3) "solid" "yellow") (/ ANCHO 2) (* (/ 5 6) ALTO) (place-image (rectangle ANCHO (/ ALTO 3) "solid" "red") (/ ANCHO 2) (* (/ 3 6) ALTO) (place-image (rectangle ANCHO (/ ALTO 3) "solid" "black") (/ ANCHO 2) (* (/ 1 6) ALTO) (empty-scene ANCHO ALTO)))))
alemania

(define holanda (place-image (rectangle ANCHO (/ ALTO 3) "solid" "blue") (/ ANCHO 2) (* (/ 5 6) ALTO) (place-image (rectangle ANCHO (/ ALTO 3) "solid" "white") (/ ANCHO 2) (* (/ 3 6) ALTO) (place-image (rectangle ANCHO (/ ALTO 3) "solid" "red") (/ ANCHO 2) (* (/ 1 6) ALTO) (empty-scene ANCHO ALTO)))))
holanda

(define (3horizontales x y z) (place-image (rectangle ANCHO (/ ALTO 3) "solid" z) (/ ANCHO 2) (* (/ 1 6) ALTO) (place-image (rectangle  ANCHO (/ ALTO 3) "solid" y) (/ ANCHO 2) (* (/ 3 6) ALTO) (place-image (rectangle  ANCHO (/ ALTO 3) "solid" x) (/ ANCHO 2) (* (/ 5 6) ALTO) (empty-scene ANCHO ALTO)))))
(3horizontales "blue" "white" "red")

(define (3colores x y z d) (if (string=? d "horizontal") (3horizontales x y z) (if (string=? d "vertical") (3verticales x y z)  (error 'variable "No es direccion"))))

(3colores  "red" "white" "blue" "vertical")

(define sudan (place-image (rotate 270 (triangle ALTO "solid" "green")) (/ (sqrt (- (sqr ALTO) (sqr (/ ALTO 2)))) 2) (/ ALTO 2) (3colores "red" "white" "black" "horizontal")))
sudan

(define argentina (place-image (circle (/ ALTO 8) "solid" "yellow") (/ ANCHO 2) (/ ALTO 2) (3colores "blue" "white" "blue" "horizontal")))
argentina

(define camerun (place-image (star (/ ALTO 6) "solid" "yellow") (/ ANCHO 2) (/ ALTO 2) (3colores "green" "red" "yellow" "vertical")))
camerun

(define brasil (place-image (circle (/ ALTO 5) "solid" "blue") (/ ANCHO 2) (/ ALTO 2) (place-image (rhombus (/ ANCHO 2) 120 "solid" "yellow") (/ ANCHO 2) (/ ALTO 2) (place-image (rectangle ANCHO ALTO "solid" "green") (/ ANCHO 2) (/ ALTO 2) (empty-scene ANCHO ALTO)))))
brasil
