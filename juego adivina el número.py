import random
from random import *
import time

comenzar = time.time()

intentos = 0

print("Bienvenido al juego de adivina el número")
nombre = input("¿Cómo te llamas?: ").capitalize()

# Generamos un rango de números entre 1-100
numero = randint(1,100)

print(f"Perfecto, {nombre}, voy a pensar en un número aleatorio entre 1 y 100 y tú tendrás que adiviniarlo en 8 intentos.\nReady?")

fin = time.time()

tiempo_juego = int(fin - comenzar)


# Intentos realizados

while intentos < 8:
    print(f"Intenta acertar el número")
    adivinar = input()
    adivinar = int(adivinar)
    intentos = intentos + 1
    if adivinar not in range(1,101):
        print("Tu número no se encuentra en el rango de 1 al 100")
    if adivinar > numero:
        print("El número es mayor al mío, intenta otro menor")
    elif adivinar < numero:
        print("El número es menor al mío, intenta otro mayor")
    else:
        print(f"¡Lo has conseguido {nombre}! Y tan solo has consumido {intentos} intentos y {tiempo_juego} minutos")
        break
if adivinar != numero:
    numero = str(numero)
    print(f"No lo has conseguido {nombre}, ¡que pena! mi número era {numero}")








