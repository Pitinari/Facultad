;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname TP3-Pitinari-Quintero) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
 #|
Trabajo Práctico 3: Estructuras

Integrantes:
- [Pitinari, Tomás], comisión [4].
- [Quintero, Iago], comisión [4].
|#

;Ejercicio 1

;Circunferencia es (make-Circunferencia posn Number)
;Tomando a posn como las coordenadas en un plano (x,y)
(define-struct Circunferencia [posicion radio])

;Ejercicio 2

;tangentes-exteriores?: Circunferencia Circunferencia -> Boolean
;Dadas 2 circunferencias quiero ver si son tangentes exteriores, para eso calculo la distancia entre ambos centros de las circunferencias y veo si es igual a la suma de sus radios
(define
 (tangentes-exteriores? circ1 circ2)
 (if (and (Circunferencia? circ1) (Circunferencia? circ2)) ;pregunto si el tipo de dato es el esperado
  (= ;Si los tipos de datos son los esperados, calculo la distancia entre los dos centros y lo comparo con la suma de los radios
   (sqrt (+
          (sqr (abs (-
                     (posn-x (Circunferencia-posicion circ1))
                     (posn-x (Circunferencia-posicion circ2))
          )))
          (sqr (abs (-
                     (posn-y (Circunferencia-posicion circ1))
                     (posn-y (Circunferencia-posicion circ2))
          )))
   ))
   (+
    (Circunferencia-radio circ1)
    (Circunferencia-radio circ2)
   )
  )
  (error "tipo de argumento invalido") ;Si alguno (o ambos) de los tipos de datos del argumento, no son los esperados emitira un error
 )
)

(check-expect (tangentes-exteriores? (make-Circunferencia (make-posn 0 1) 1) (make-Circunferencia (make-posn 0 4) 2)) #true)
(check-expect (tangentes-exteriores? (make-Circunferencia (make-posn 1 2) 1) (make-Circunferencia (make-posn 1 5) 2)) #true)
(check-expect (tangentes-exteriores? (make-Circunferencia (make-posn 2 1) 1) (make-Circunferencia (make-posn 0 4) 2)) #false)
;entrada: (make-Circunferencia (make-posn 1 2) 1) 5, salida: (error "tipo de argumento invalido")



;Ejercicio 3

;crear-tangente-exterior: Circunferencia Number -> Circunferencia
;Dada una circunferencia y un numero entero, vamos a determinar otra circunferencia, tal que sean tangentes exteriores, cuyo radio es n veces el radio de la circunferencia dada y su coordenada y es la misma
(define 
  (crear-tangente-exterior circ1 n)
  (if (and (Circunferencia? circ1) (number? n))
      (let*  ;usamos let para hacer las definiciones necesarias de la circunferencia
          ([radio (* (Circunferencia-radio circ1) n)] ;definimos el radio de la nueva circunferencia como n veces el radio de la original
           [posy (posn-y (Circunferencia-posicion circ1))] ;la posicion y es la misma que la de la circunferencia original 
           [posx (+ (posn-x (Circunferencia-posicion circ1)) (Circunferencia-radio circ1) radio)]) ;para que sean tangentes la posicion x es la suma de los dos radios mas la posx de la circunferencia original
          (make-Circunferencia (make-posn posx posy) radio)) ;definimos y devolvemos la circunferencia
      (error "tipo de argumento invalido") ;Si alguno (o ambos) de los tipos de datos del argumento, no son los esperados emitira un error
  )
)

(check-expect (crear-tangente-exterior (make-Circunferencia (make-posn 5 5) 3) 3) (make-Circunferencia (make-posn 17 5) 9))
(check-expect (crear-tangente-exterior (make-Circunferencia (make-posn 2 1) 6) 5) (make-Circunferencia (make-posn 38 1) 30))