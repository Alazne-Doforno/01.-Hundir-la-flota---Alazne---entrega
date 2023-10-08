import numpy as np
import funciones as fu
import variables as va
import time

nombre = input("\n ¿Cómo te llamas?: \n")
time.sleep(1)

print(f"\n ¡Hola {nombre}! Bienvenida al juego de Hundir la flota.\n")
time.sleep(2)

print(" El objetivo del juego es hundir todos los barcos de tu oponente.\n")
time.sleep(3)
print(" Tendrás un tablero con 10 barcos de diferentes tamaños aleatoriamente colocados:\n \
      - 'O' representa la eslora de un barco.\n \
      - 'X' disparo acertado.\n \
      - '-' disparo fallido.\n")

time.sleep(10)
print(" Los jugadores os iréis turnan los disparos.\n \
Para realizar un disparo, simplemente tienes que indicar las coordenadas en el tablero.\n \
Si aciertas, tendrás otro disparo disponible; en caso contrario, le tocará a tu rival.\n")
time.sleep(10)
print(" Vamos a colocar todos los barcos de forma aleatoria...")
time.sleep(3)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("\n¡Comienza el juego!\n")
time.sleep(3)

fu.disparo()