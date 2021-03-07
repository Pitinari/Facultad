#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <assert.h>

/*
Tomas Pitinari
COSAS A SABER: 
-El programa para cuando toma BASTA como palabra, por ejemplo, que las palabras basta y bastA pueden ser ingresadas.
-Los comentarios del paso a paso de las funciones estan en la declaracion de proposito
-Los tests estan incluidos en el main 
-Hice que el programa use mayusculas siempre por un tema de comodidad al leer, pero se puede cambiar a minusculas tranquilamente
*/

//Se define una estructura como una lista enlazada, donde se van a guardar las palabras como string y su direccion como un entero
struct palabra{
  char* p;
  int dir;
  struct palabra *sig;
};

//Resepresente una funcion que toma un string y lo modifica
//mayuscula: String -> Nada
//La funcion toma un string y transforma todos sus caracteres, en sus respectivos caracteres mayusculas
//entrada: "hola" salida: "HOLA"
//entrada: "chAu" salida: "CHAU"
void mayuscula (char* input){
  int i=0;
  while(*(input+i) != '\0'){
    *(input+i) = toupper(*(input + i));
    i++;}
}

//No pide parametros y va registrando el buffer dinamicamente
//ingresar_palabra: Nada -> *char
//La funcion inicializa un array de largo 0, y lee caracter a caracter, si es distinto de '\n' agranda el array y guarda el caracter
char *ingresar_palabra(){
  int c,i; 
  char* string = malloc(sizeof(char));
  string[0]='\0';
  for(i=0;(c=getchar())!='\n'; i++)
    {
        string = realloc(string, (i+2)*sizeof(char));
        string[i] = (char) c;
        string[i+1] = '\0';
    }

    return string;
}

//Toma la entrada de datos para la dimension como un numero entero
//ingresar_dimension: Nada -> Int
//La funcion solicita la entrada de la dimension para el tablero y vuelve a pedir el numero si el entero es un numero negativo
int ingresar_dimension (){
  int dimension;
  printf("Ingrese un numero n, tal que la dimension de la sopa de letras sera nxn: ");
  while(1){
    scanf("%d", &dimension);
    getchar(); //utilizo un getchar para limpiar el \n de buffer ya que fflush(stdin) no me estaba funcionando
    if(dimension>0)
      break;
    printf("Ingrese una dimension valida: ");
  }
  return dimension;
}

//Toma la entrada de datos para la direccion de una palabra como un numero entero
//ingresar_direccion: Nada -> Int
//La funcion solicita la entrada de la direccion de la ultima palabra ingresada y la vuelve a pedir si el numero ingresado no esta dentro de las direcciones posibles
int ingresar_direccion(){
  int i;
  printf("Ingrese direccion [0-5]: ");
  while(1){
    scanf("%d", &i);
    getchar(); //utilizo un getchar para limpiar el \n de buffer ya que fflush(stdin) no me estaba funcionando
    if(i>=0 && i<=5)
      break;
    printf("Direccion invalida, vuelva a ingresar: ");
  }
  return i;
}

//Represente la lista de palabras ya ingresdas como una lista enlazada y la palabra que quiero corroborar que no este como un string
//ya_contiene: struct palabra String -> Int(cumpliendo la funcion de un booleano)
//La funcion pasa por todos los elementos de la lista enlazada y revisa si la palabra es igual a la ingresada, en caso de serlo la funcion devuelve 1, como
//True si fuese booleano, al terminar de revisar todas las palabras devuelve 0, como False si fuera booleano, ya que ninguna palabra de la lista es igual
//Entrada: {"HOLA",0}->{"CHAU",3} "HOLA" salida: 1
//Entrada: {"HOLA",0}->{"CHAU",3} "CASA" salida: 0
int ya_contiene(struct palabra inicio, char temp[]){
  struct palabra *pos = &inicio;
  while(pos != NULL){
    if(!strcmp(pos->p,temp))
      return 1;
    pos = pos->sig;
  }
  return 0;
}

//liberar_memoria_ll: struct palabra -> Nada
//La funcion toma la lista enlazada y libera uno a uno los nodos
void liberar_memoria_ll (struct palabra *pos){
  if(pos != NULL){
    free(pos->p);
    liberar_memoria_ll(pos->sig);
    }
  free(pos);
}


//La lista de palabras esta representada como una lista enlazada y la dimension de la tabla como un entero
//guardar_datos: struct palabra Int -> Nada
//La funcion toma la lista de palabras y la dimension, luego abre (o en caso de no existir crea) un archivo donde se guardaran los datos
//primero guardara la dimension y despues guardara palabra a palabra junto con su direccion a medida que libera la memoria de los string que las guardaban
void guardar_datos (struct palabra inicio, int dim){
  struct palabra *pos = &inicio;
  FILE *a = fopen("datos.txt","w");

  fprintf(a, "DIMENSION\n%d\nPALABRAS\n", dim);

  while(pos != NULL){
    fprintf(a, "%s %d\n", pos->p, pos->dir);
    pos = pos->sig;
  }
  fclose(a);
  free(a);
}

int main(){

  {//tests
    {//testeo de mayuscula
      char *c;
      c = malloc(sizeof(char)*5);
      strcpy(c,"holA");
      mayuscula(c);
      assert(strcmp(c,"HOLA") == 0);
      strcpy(c,"CHAU");
      mayuscula(c);
      assert(strcmp(c,"CHAU") == 0);
      strcpy(c,"holA");
      mayuscula(c);
      assert(strcmp(c,"hola") != 0);
      free(c);
    }
    {//testeo de ya_contiene Y liberar_memoria_ll
      struct palabra *ejemplo;
      ejemplo = malloc(sizeof(struct palabra));
      ejemplo->p = malloc(sizeof(char)*5);
      strcpy(ejemplo->p,"HOLA");
      ejemplo->sig = malloc(sizeof(struct palabra));
      ejemplo->sig->p = malloc(sizeof(char)*5);
      strcpy(ejemplo->sig->p,"CHAU");
      ejemplo->sig->sig = NULL;
      assert(ya_contiene(*ejemplo,"HOLA") == 1);
      assert(ya_contiene(*ejemplo,"CHAU") == 1);
      assert(ya_contiene(*ejemplo,"CASA") == 0);
      liberar_memoria_ll(ejemplo);
    }
  }

  struct palabra *inicio, *pos;
  char *temp;
  int dim, i;

  dim = ingresar_dimension(); //Se ingresa la dimension

  printf("Ingrese la primera palabra: ");
  temp = ingresar_palabra(); //se utiliza un array dinamico para ingresar la palabra
  mayuscula(temp);

  i = ingresar_direccion(); //se ingresa la direccion de la ultima palabra

  inicio = malloc(sizeof(struct palabra)); //como el programa utiliza una lista enlazada inicializamos el nodo raiz como "inicio" y guardamos la priemra palabra con su direccion
  inicio->p = malloc(sizeof(char)*(strlen(temp)+1));
  strcpy(inicio->p,temp);
  inicio->dir = i;
  inicio->sig = NULL;

  pos = inicio; //se va a usar pos como puntero para ir moviendose por la lista enlazada

  free(temp); //se libera la memoria del string ingresado antes de volver a ingresar

  while(1){

    printf("Ingrese una palabra: ");
    temp = ingresar_palabra();  //se ingresa una palabra

    if(!strcmp(temp,"BASTA")){  //el ingreso de palabras solo finaliza con "BASTA", por lo que "basta" es una palabra valida
      printf("Se ingreso la palabra BASTA, termino el ingreso de palabras\n");
      break;
    }

    mayuscula(temp); //luego de corroborar si es distinto de "BASTA" se hace mayuscula para normalizar

    i = ingresar_direccion();

    if(ya_contiene(*inicio,temp)){  //revisa si ya se ingreso
      printf("La palabra ya esta contenida\n");
      continue;
    }
    
    pos->sig = malloc(sizeof(struct palabra));  //se guarda la palabra en el siguiente nodo y se mueve el punteo pos
    pos = pos->sig;
    pos->p = malloc(sizeof(char)*(strlen(temp)+1));
    strcpy(pos->p,temp);
    pos->dir = i;
    pos->sig = NULL;

    free(temp); //se libera el string antes de volver a ingresar
  }
  free(temp);//se libera el string ya que no se va a usar mas

  guardar_datos(*inicio,dim); //guarda los datos en un archivo "datos.txt"

  liberar_memoria_ll(inicio); //libera la memoria utilizada en la lista enlazada

  return 0;
}