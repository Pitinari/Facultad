;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ejercicio-plantillaA) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

(require 2htdp/image)
(require 2htdp/universe)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; estado del sistema:
(define-struct estado [color angulo rotar])
; estado es (make-estado ......).
; Interpretación: el estado es una estructura que contiene 3 datos, el color del cuadrado, su angulo de rotacion y si rota por tick

; constantes
(define ALTO 300)
(define ANCHO 300)
(define GRADOS-POR-TICK 5)
(define COLOR-FONDO "green")
(define INIT (make-estado "red" 0 "on")) ; estado inicial
;.......


; dibujar : estado -> imagen
(define (dibujar e) (place-image
                     (rotate (estado-angulo e) (square 100 "solid" (estado-color e)))
                     (/ ANCHO 2) (/ ALTO 2)
                     (rectangle ANCHO ALTO "solid" COLOR-FONDO)))

; key-handler : estado key -> estado
;
(define (key-handler e k) (cond
                            [(string=? k " ") (if (string=? "off" (estado-rotar e)) (make-estado (estado-color e) (estado-angulo e) "on") (make-estado (estado-color e) (estado-angulo e) "off"))]
                            [(string=? k "b") (make-estado "blue" (estado-angulo e) (estado-rotar e))]
                            [(string=? k "y") (make-estado "yellow" (estado-angulo e) (estado-rotar e))]
                            [(string=? k "r") (make-estado "red" (estado-angulo e) (estado-rotar e))]
                            [else e]
                            ))
; actualizar-angulo : estado -> estado
; responde al tick del reloj
(define (actualizar-angulo e) (if (string=? "on" (estado-rotar e)) (make-estado (estado-color e) (modulo (+ (estado-angulo e) GRADOS-POR-TICK) 360) (estado-rotar e)) e))


(big-bang INIT
          [on-tick actualizar-angulo]
          [on-key  key-handler]
          [to-draw dibujar])