;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ejercicio-plantillaB) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "2htdp") (lib "universe.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "2htdp") (lib "universe.rkt" "teachpack" "2htdp")) #f)))
(require lang/posn)
(require 2htdp/image)
(require 2htdp/universe)

; El Estado está compuesto por:
(define-struct estado [fondo radio color])


;definiciones constantes, COMPLETE si es necesario
(define ANCHO 500)
(define ALTO 500)
(define COLOR-FONDO "black")

;Estado inicial. Escena vacía del color del fondo, radio 20, color "red"
(define ESTADO-INI (make-estado (rectangle ANCHO ALTO "solid" COLOR-FONDO) 20 "red"))


;pantalla: Estado -> Image
;Pantalla: dedicado a la cláusula to-draw de la función big-bang
(define (pantalla e) (estado-fondo e))


;mouse-handler: Estado Number Number MouseEvent -> Estado
;mouse-handler es el handler dedicado a la cláusula on-mouse de la función big-bang
(define (mouse-handler e x y me) (if
                                  (string=? me "button-down")
                                  (make-estado
                                      (place-image (circle (estado-radio e) "solid" (estado-color e)) x y (estado-fondo e))
                                      (estado-radio e)
                                      (estado-color e))
                                   e))


;key-handler: Estado Key -> Estado
;key-handler es el handler dedicado a la cláusula on-key de la función big-bang
(define (key-handler e k) (cond
                            [(string=? k "b") (make-estado (estado-fondo e) (estado-radio e) "blue")]
                            [(string=? k "m") (make-estado (estado-fondo e) (estado-radio e) "magenta")]
                            [(string=? k "g") (make-estado (estado-fondo e) (estado-radio e) "green")]
                            [(string=? k "up") (make-estado (estado-fondo e) (* (estado-radio e) 2) (estado-color e))]
                            [(string=? k "down") (make-estado (estado-fondo e) (/ (estado-radio e) 2) (estado-color e))]
                            [(string=? k "r") ESTADO-INI]
                            [else e]
                            ))


; Expresión big-bang para el programa interactivo.

(big-bang ESTADO-INI
  [to-draw pantalla]
  [on-key key-handler]
  [on-mouse mouse-handler])
