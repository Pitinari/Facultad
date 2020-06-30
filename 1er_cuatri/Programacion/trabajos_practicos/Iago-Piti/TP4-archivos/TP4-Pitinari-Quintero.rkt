;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname TP4-Apellido1-Apellido2) (read-case-sensitive #t) (teachpacks ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "universe.rkt" "teachpack" "2htdp") (lib "image.rkt" "teachpack" "2htdp") (lib "batch-io.rkt" "teachpack" "2htdp")) #f)))
#|
Trabajo Práctico 4: Listas

Integrantes:
- [Pitinari, Tomás], comisión [4].
- [Quintero, Iago], comisión [4].
|#

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Datos ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;; Diseño de datos

; Representaremos fechas mediante strings, según el formato aaaa-mm-dd.
; Representaremos los nombres de las localidades y departamentos mediante strings.
; Representaremos la cantidad de casos (sospechosos, descartados y confirmados)
; mediante números.

(define-struct notificacion [fecha loc conf desc sosp notif])
; notificacion es (String, String, Number, Number, Number, Number)
; Interpretación: un elemento en notificacion representa el conjunto de notificaciones
; registradas en una localidad (loc) hasta un día (fecha), en donde:
; - hay conf casos confirmados de COVID-19
; - hay desc casos descartados de COVID-19
; - sosp casos estaban en estudio.
; El último elemento, notif, indica la cantidad total de notificaciones.


;;;;;;;;;;;; Preparación de los Datos

;;;;;; Datos sobre localidades santafesinas

; Datos de entrada sobre localidades
(define INPUT-LOC (read-csv-file "dataset/santa_fe_departamento_localidad.csv"))
(define DATOS-LOC (rest INPUT-LOC))

; tomar-dos : List(X) -> List(X)
; Dada una lista l de dos o más elementos, tomar-dos calcula
; la lista formada por los dos primeros elementos de l, en
; ese orden.
(check-expect (tomar-dos (list "a" "b")) (list "a" "b")) 
(check-expect (tomar-dos (list 0 1 2 3)) (list 0 1))
(define
  (tomar-dos l)
  (list (first l) (second l)))

; Lista de localidades santafecinas
(define LISTA-LOC (map second DATOS-LOC))
; Lista de localidades santafecinas, con su departamento
(define LISTA-DPTO-LOC (map tomar-dos DATOS-LOC))

;;;;;; Datos sobre notificaciones de COVID-19

; Datos de entrada sobre notificaciones
(define INPUT-NOTIF (read-csv-file "dataset/notificaciones_localidad.csv"))
(define DATOS-NOTIF (rest INPUT-NOTIF))


; [Completar, ejercicio 1]

;Voy a definir una funcion, que dada una posicion como un number, y una lista, retorne el elemento en esa posicion
;lista-indice: Number List(x) -> x
(define (lista-indice x l) (cond
                             [(empty? l) "El indice esta mal"]
                             [(= x 0) (first l)]
                             [else (lista-indice (- x 1) (rest l))]))
;Para hacer el ejercicio 1, voy a necesitar una funcion que tome una lista y la transforme en una notificacion
;list-notif: List(x) -> notificacion
(define (list-notif l) (make-notificacion
                          (lista-indice 0 l)
                          (lista-indice 1 l)
                          (string->number (lista-indice 2 l))
                          (string->number (lista-indice 3 l))
                          (string->number (lista-indice 4 l))
                          (string->number (lista-indice 5 l))
                       ))

; Lista de notificaciones
(define LISTA-NOTIF (map list-notif DATOS-NOTIF))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Consultas ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define ANTES "2020-04-02")
(define HOY "2020-06-02")
(define LIMITE-CASOS 25)

;;;;;;;;;;;; Consulta 1

; [Completar, ejercicio 2-1]

;definimos una funcion auxiliar para determinar si la notificacion supera LIMITE-CASOS en sus casos confirmados en el dia HOY
;cumple-condicion?: notificacion -> Boolean
(check-expect (cumple-condicion? (make-notificacion  "2020-04-06" "Rosario" 12 2 4 18)) #false)
(check-expect (cumple-condicion? (make-notificacion  "2020-06-02" "Rosario" 30 2 4 36)) #true)
(define (cumple-condicion? x) (and (> (notificacion-conf x) LIMITE-CASOS) (string=? (notificacion-fecha x) HOY)))

;definimos una funcion que filtre las notificaciones que superen LIMITE-CASOS y que sean del dia HOY y luego mapee las notificaciones filtradas para obtener solo sus respectivas localidades
;localidades-limite-casos: List(notificacion) -> List(x)
(check-expect (localidades-limite-casos (list (make-notificacion  "2020-04-06" "La Capital" 12 2 4 18) (make-notificacion  "2020-06-02" "Rosario" 30 2 4 36)))  (list "Rosario"))
(check-expect (localidades-limite-casos (list (make-notificacion  "2020-03-01" "Vera" 4 1 2 7) (make-notificacion  "2020-06-02" "General Obligado" 26 1 1 27)))  (list "General Obligado"))
(define (localidades-limite-casos l) (map  notificacion-loc (filter cumple-condicion? l)))

; [Completar, ejercicio 2-2]

(define LOCALIDADES-LIMITE-CASOS (localidades-limite-casos LISTA-NOTIF))

;;;;;;;;;;;; Consulta 2

; [Completar, ejercicio 3-1]

;definimos una funcion auxiliar para determinar si un elemento ya esta en la lista
;repetido?: String List(String) -> List(String)
(define (repetido? x l) (cond
                             [(empty? l) #false]
                             [(string=? (first l) x) #true]
                             [else (repetido? x (rest l))]
                           ))

;definimos una funcion que recorra la lista y pregunte si el elemento actual esta en resto de la lista, si este elemento se repite, se quita de la lista
;sacar-repetidos: List(String) -> List(String)
(define (sacar-repetidos l) (cond
                              [(empty? l) l]
                              [(repetido? (first l) (rest l)) (sacar-repetidos (rest l))]
                              [else (cons (first l) (sacar-repetidos (rest l)))]
                              ))

;definimos una funcion auxiliar que dada una lista de listas, arme una lista con los primeros elementos de cada lista
;tomar-primeros: List(List(X)) -> List(X)
(define (tomar-primeros l) (cond
                             [(empty? l) l]
                             [else (cons (first (first l)) (tomar-primeros (rest l)))]
                           ))

(define LISTA-DPTO (sacar-repetidos(tomar-primeros LISTA-DPTO-LOC)))

; [Completar, ejercicio 3-2]
 
; definimos una funcion auxiliar que retorna el departamento de la localidad ingresada
; loc-a-dpto: String List(List(String)) -> String

(check-expect (loc-a-dpto "PUEBLO MUÑOZ" LISTA-DPTO-LOC) "Rosario")
(check-expect (loc-a-dpto "TOBA" LISTA-DPTO-LOC) "Vera")

(define (loc-a-dpto loc list-dpto-loc)
    (cond
        [(empty? list-dpto-loc) (error "la localidad no forma parte de la provincia")]
        [(string=? (second (first list-dpto-loc))  loc) (first (first list-dpto-loc))]
        [else (loc-a-dpto  loc (rest list-dpto-loc))])
)

; definimos una funcion que retorna la cantidad de casos confirmados en un departamento hasta una fecha
; confirmados-dpto-fecha: List(Notificacion) String String -> Number

(check-expect (confirmados-dpto-fecha LISTA-NOTIF "Rosario" "2020-03-25") 11)
(check-expect (confirmados-dpto-fecha LISTA-NOTIF "Rosario" "2020-05-12") 109)


(define (confirmados-dpto-fecha notif dpto fecha)
  (cond
    [(empty? notif) 0]
    [else (cond
            [(and (string=? (notificacion-fecha (first notif)) fecha) (string=? (loc-a-dpto (notificacion-loc (first notif)) LISTA-DPTO-LOC)  dpto)) (+ (notificacion-conf (first notif)) (confirmados-dpto-fecha (rest notif) dpto fecha))]
            [else (+ 0 (confirmados-dpto-fecha (rest notif) dpto fecha))])]

   )
)


; [Completar, ejercicio 3-3]

; definimos una funcion auxiliar que retorna una lista de departamentos
; devolver-lista-dptos: List(Notificacion) String List(List(String)) -> List(String)
(check-expect (devolver-lista-dptos LISTA-NOTIF "2020-04-12" (list "Rosario" "Belgrano" "Caseros")) (list (list "Rosario" "93") (list "Belgrano" "4") (list "Caseros" "3")))
(check-expect (devolver-lista-dptos LISTA-NOTIF "2020-04-12" (list "La Capital" "General Obligado")) (list (list "La Capital" "37") (list "General Obligado" "0")))
(define (devolver-lista-dptos notif fecha lista-dpto) 
  (cond
    [(empty? lista-dpto) lista-dpto]
    [else (cons (list (first lista-dpto) (number->string (confirmados-dpto-fecha notif (first lista-dpto) fecha))) (devolver-lista-dptos notif fecha (rest lista-dpto)))]
))

; Retorna una lista con la cantidad de casos confirmados en cada departamento hasta cierta fecha
; confirmados-por-dpto: List(Notificacion) String -> Number
; Ya que esta funcion solo llama a la funcion devolver-lista-dptos, para poder recursionar sobre LISTA-DPTO, el test esta implicito en el test de la funcion devolver-lista-dpto 
(define (confirmados-por-dpto notif fecha) (devolver-lista-dptos notif fecha LISTA-DPTO))


; [Completar, ejercicio 3-4]

(define CONFIRMADOS-DPTO-ANTES (confirmados-por-dpto LISTA-NOTIF ANTES))
(define CONFIRMADOS-DPTO-HOY (confirmados-por-dpto LISTA-NOTIF HOY))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Salidas ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;; Consulta 1

; [Completar, ejercicio 4 - loc-lim-casos.csv]

;Vamos a definir una funcion auxiliar que va a tomar dos strings y los va a concatenar con un "\n" entre ellos
;saltos-de-lineas string string -> string
(check-expect (saltos-de-lineas "hola" "chau") "hola\nchau")
(check-expect (saltos-de-lineas "casa" "linda") "casa\nlinda")
(define (saltos-de-lineas x y) (string-append x "\n" y))

;para formatear los datos de la lista a usar en el archivo.csv, vamos a definir una funcion que recorra cada elemento de la lista LOCALIDADES-LIMITE-CASOS y los pase por saltos-de-lineas
;crear-string-lista: List(string) -> string
(check-expect (crear-string-lista (list "hola" "chau")) "hola\nchau\n")
(check-expect (crear-string-lista (list "la" "casa" "linda")) "la\ncasa\nlinda\n")
(define (crear-string-lista contenido) (foldr saltos-de-lineas "" contenido))

(write-file "loc-lim-casos.csv" (string-append "LOCALIDADES" "\n" (crear-string-lista LOCALIDADES-LIMITE-CASOS)))

;;;;;;; Consulta 2

; [Completar, ejercicio 4 - casos-por-dpto-hoy.csv y casos-por-dpto-antes.csv]

;Vamos a definir la funcion que va a usar el foldr que tomas formateo-de-fila, va a tomar cada elemento de la fila y lo va a concatenar con el resto de la lista poniendo una coma en el medio, si detecta un "\n" no va a poner coma
;comas-y-salto-de-lineas: string string -> string
(check-expect (comas-y-salto-de-lineas "hola" "chau\n") "hola, chau\n")
(check-expect (comas-y-salto-de-lineas "la" "\n") "la\n")
(define (comas-y-salto-de-lineas x y) (cond
                                        [(string=? y "\n") (string-append x y)]
                                        [else (string-append x ", " y)]
                                        ))

;Necesitamos una funcion auxiliar para que este en el foldr de crear-string-lista y concatene los strings dados por comas-y-salto-de-lineas
;formateo-de-fila: List(string) string -> string
(check-expect (formateo-de-fila (list "hola" "chau") "la, casa, linda\n") "hola, chau\nla, casa, linda\n")
(check-expect (formateo-de-fila (list "la" "casa" "linda") "hola, chau\n") "la, casa, linda\nhola, chau\n")
(define (formateo-de-fila fila1 resto-filas) (string-append (foldr comas-y-salto-de-lineas "\n" fila1) resto-filas))

;Dada una lista de listas necesitamos definir una funcion que transforme todos los strings de la lista de listas en un formato valido para escribir en el archivo.csv
;crear-string-lista-de-listas List(List(string)) -> string
(check-expect (crear-string-lista-de-listas (list (list "hola" "chau") (list "la" "casa" "linda"))) "hola, chau\nla, casa, linda\n")
(define (crear-string-lista-de-listas contenido) (string-append (foldr formateo-de-fila "" contenido)))

(write-file "casos-por-dpto-hoy.csv" (string-append "DEPARTAMENTOS, CASOS CONFIRMADOS\n" (crear-string-lista-de-listas CONFIRMADOS-DPTO-HOY)))
(write-file "casos-por-dpto-antes.csv" (string-append "DEPARTAMENTOS, CASOS CONFIRMADOS\n" (crear-string-lista-de-listas CONFIRMADOS-DPTO-ANTES)))

