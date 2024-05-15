def imprimirholamundo ():
    print ("hola mundo")

def imprimirunverso ():
    print ("Quick quick \ntell me something awful \nlike you are a poet\ntrapped inside the body of a finance guy")

import math

def raizDe2 ():
    return round (math.sqrt(2), 4) 

def factorial_de_dos ():
    return "2"

def perimetro ():
    return math.pi * 2

def imprimir_saludo (nombre:str):
    return "Hola " + nombre

def raiz_cuadrada_de (x:int):
    return math.sqrt(x)

def fahrenheit_a_celsius (temp_far:float):
    return (temp_far-32) * 5/9

def imprimir_dos_veces (estribillo):
    return 2 * estribillo

def es_multiplo_de (x:int,y:int) -> bool:
    if (x % y) == 0 :
        return True
    else:
        return False
#OTRA FORMA

def es_Multiplo_de (x:int,y:int) -> bool:
    resultado:bool = None
    if (x % y) == 0 :
        resultado = True
    else:
        resultado = False
    
    return resultado
    
def es_par (x:int) -> bool:
    return es_multiplo_de (x,2)

def cantidad_de_pizzas (comensales:int, min_cant_de_porciones:int) -> int:
    return math.ceil (comensales * min_cant_de_porciones / 8)

def alguno_es_0 (numero1:float,numero2:float) -> bool:
    