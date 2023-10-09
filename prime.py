import math

def perimetro () :
    return 2 * math.pi

print(perimetro())

def inprimir_saludo (nombre:str):
    print("Hola mi causita " + nombre)

inprimir_saludo("Andy")

def raiz_cuadrada(num:int):
    print("La raiz cuadrada es: " + str(math.sqrt(num)))

raiz_cuadrada(45)

def fahrenheit_a_celsius(tempfar:float):
    X = ((tempfar-32)*5)/9
    print("La temperatura en Celsius es: " + str(X))

fahrenheit_a_celsius(45)

def cantidad_de_pizzas(comensale:int, min_cant_de_porciones:int):
    pizza = 8
    cantidad_a_comer = min_cant_de_porciones * comensale
    cantidadpizzas = cantidad_a_comer/pizza
    return print("La cantidad de pizzas es " + str(int(cantidad_a_comer)) + " y las pizzas que vas a consumir son " + str(math.ceil(cantidadpizzas)))

cantidad_de_pizzas(4,5)

def alguno_es_0(numero1:int, numero2:int):
    return numero1 == 0 or numero2 == 0

print(alguno_es_0(0,4))

def es_nombrelargo(nombre:str) -> bool:
    return print(len(nombre) > 3 and len(nombre) < 8)

es_nombrelargo("Andres")

def es_multiplo(n:int,m:int) -> bool:
    res:bool = (n %  m) == 0
    return res

print(es_multiplo(4,5))

def peso_pino(altura:int)->int:
    primerpeso:int= min(3,altura)
    segundopeso:int= max(3,altura)
    return primerpeso*300 + (segundopeso - 3)*200



def es_peso_util(peso:int) -> bool:
    return (peso > 400 and peso < 1000) or peso == 400 or peso == 1000 

def sirve_pino(peso:int)->bool:
    x = peso_pino(peso)
    y = es_peso_util(x)
    return y

print(sirve_pino(5))
    

def numerosdel1al10(n:int)->int:
        while n > 0:
            print(n)
            n-=1
        print("despegue")
    
numerosdel1al10(45)
