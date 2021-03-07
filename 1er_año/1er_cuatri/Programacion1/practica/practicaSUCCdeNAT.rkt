;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname practicaSUCCdeNAT) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp")) #f)))
(define (sumanat x y) (cond
                        [(zero? y) x]
                        [else (sumanat (add1 x) (sub1 y))]
                        ))

(define (multiplicar x y) (cond
                            [(or (zero? x) (zero? y)) 0]
                            [(zero? (sub1 y)) x]
                            [else (sumanat x (multiplicar x (sub1 y)))]
                            ))

