;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname TP2-Pitinari-Quintero) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp")) #f)))
#|
Trabajo Práctico 2: Programas Interactivos

Integrantes:
- [Pitinari, Tomás], comisión [4].
- [Quintero, Iago], comisión [4].
|#

;[Completar con el diseño del programa interactivo pedido]
(require 2htdp/universe)
(require 2htdp/image)


(define FUENTE 20) ;tamaño de la fuente de las letras

(define ESTADO-INICIAL 50) ;estado inicial del big-bang

(define TIEMPO-TICK 2) ;tiempo de tick, en este caso fijado cada 2 segundos

(define MIN 0) ;El numero mas chico

(define MAX 100) ;El numero mas grande

(define CANT-NUM (+ (- MAX MIN) 1)) ;cantidad de puntos que vamos a representar en el eje x

(define ANCHO (* 3 (- CANT-NUM 1))) ;ancho de la escena, buscamos que tenga la forma de k*100 siendo k un natural, para que al buscar la proporcion de la distancia entre dos puntos, sea un numero entero, ya que la cantidad de segmentos que se forman al dividir el eje en CANT-NUM puntos, es CANT-NUM - 1 segmentos

(define ALTO 80) ;alto de la escena

(define COLORPAR "blue") ;constante de color para los pares

(define COLORIMP "red") ;constante de color para los impares


;paridad: Number -> String
;Devolvemos un String dependiendo de la paridad del numero ingrersado
(define (paridad n)
  (if (= (modulo n 2) 0)
      COLORPAR
      COLORIMP))
(check-expect (paridad 2) COLORPAR);entrada: 2, salida: "blue"
(check-expect (paridad 7) COLORIMP);entrada: 7, salida: "red"

;coordenadax: Number Number Number -> Number
;Calculamos la posicion horizontal de el numero respecto al ancho del plano y la cantidad de partes (numeros distintos posibles) de este
(define (coordenadax n ancho partes)
  (* (/ ancho partes) n))
(check-expect (coordenadax 5 200 100) 10);entrada: (5 200 100), salida: 10
(check-expect (coordenadax 24 300 50) 144);entrada: (24 300 50), salida: 144

;Representaremos el Estado como Number y lo transformaremos en un Image
;pantalla: Estado -> Image
;Recibe un Estado, que es un Number, y lo ubicaremos en un plano x y, siendo x el valor calculado en coordenadax, con un margen agregado para que no se corte por el plano en caso de ser muy pequeño, e y el valor que es igual a la mitad del alto del plano (el medio).
(define (pantalla n)
  (place-image
    (text (number->string n) FUENTE (paridad n)) ;Se transforma el Estado a un string y del string a una imagen de fuente constante y color dependiente de su paridad
    (+ (coordenadax (- n MIN) ANCHO (- CANT-NUM 1)) (/ (image-width(text (number->string MIN) FUENTE "black")) 2)) ;la imagen antes generada se ubicara en la coordenada x correspondiente al resultado de la funcion coordenadax mas la mitad del ancho de la imagen (text "0" Fuente colorIndiferente), para que no se salgan de la escena los numeros que estan mas a la izquierda. Notar en los parametros de coordenadax le restamos al estado el numero minimo, para que si se cambian los valores de los extremos de los ejes la funcion no genere errores.
    (/ ALTO 2) ;Una coordenada y igual a la mitad del alto del plano vacio
  (empty-scene
   (+ ANCHO ;al ancho que fije para la escena, le sumo los valores dados abajo, para que, las imagenes de "0","1","2","98","99" o "100" no queden afuera de la escena, por lo que vimos arriba desplazo un poco los puntos para que todo quede dentro
      (/ (image-width(text (number->string MAX) FUENTE "black")) 2)
      (/ (image-width(text (number->string MIN) FUENTE "black")) 2))
   ALTO)))

;Representamos el Estado como un Number
;cambiar-numero: Estado -> Estado
;Hay que modificar el Estado cada tiempo-tick segundos, por lo que generamos un numero aleatorio natural entre MIN y MAX.
(define (cambiar-numero n) (+ (random CANT-NUM) MIN)) ;luego de generar el numero random, le sumo el numero minimo para que quede dentro del rango.+
(check-random (cambiar-numero 45) (+ (random CANT-NUM) MIN))
(check-random (cambiar-numero 69) (+ (random CANT-NUM) MIN))
;Cualquier numero dentro del rango usado puede devolver cualquier numero dentro del mismo rango


;Representaremos el Estado en Number y las teclas en String
;flechas: Estado String -> Estado
;Cada tecla tiene un String especifico asociado, apretamos la flecha derecha reemplazaremos el estado por la suma de, un numero aleatorio entre 0 y 49, y 51, lo cual es igual a un numero aleatorio entre 51 y 100. Por otro lado al apretar la flecha izquierda cambiamos el estado por un numero aleatorio entre 0 y 49. Si la tecla tiene cualquier otro valor el estado se mantiene.
;El problema con esta funcion es que no la puede generalizar con las constantes ya que eran consignas bastante especificas.
(define (flechas n k)
  (cond
  [(string=? k "right") (+ (random 50) 51)] ;caso de que la tecla presionada sea la flecha derecha
  [(string=? k "left") (random 50)] ;caso de que la tecla presionada sea la flecha izquierda
  [else n])) ;caso en que la tecla presionada sea cualquier otra
(check-random (flechas 2 "right") (+ (random 50) 51));entrada: 2 "right", salida: random entre 51 y 100
(check-random (flechas 84 "left") (random 50));entrada: 84 "left", salida: random entre 0 y 49
(check-expect (flechas 50 "up") 50);entrada: 50 "up", salida: 50



;Representamos el Estado como un Number
;multiplo8: Estado -> Boolean
;Para determinar el final del big-bang, el estado tiene que ser multiplo de 8, lo que es equivalente a que el resto de la division entre el estado y 8 sea 0
;No utilizamos una constante para la funcion multiplo8, ya que tampoco tendria sentido testearla
(define (multiplo8 n) (= (modulo n 8) 0)) ;Si el resto de la division entre el estado y 8 es igual a 0, entonces la funcion devuelve #true, por lo que finaliza big-bang, en todos los demas casos devuelve #false y no hace nada.
(check-expect (multiplo8 25) #false);entrada: 25, salida: #false
(check-expect (multiplo8 80) #true);entrada: 80, salida: #true


(big-bang ESTADO-INICIAL ;estado-inicial constante definida en 50 
[to-draw pantalla] ;pantalla "dibuja" en un plano vacio insertando una imagen del Estado
[on-tick cambiar-numero TIEMPO-TICK] ;Llamara a cambiar-numero cada tiempo-tick segundos, siendo tiempo-tick una constante definida en 2
[on-key flechas] ;al presionar cualquier tecla se llamara a la funcion
[stop-when multiplo8] ;antes de llamar a la funcion que "dibuja", verifica si big-bang debe finalizar
)