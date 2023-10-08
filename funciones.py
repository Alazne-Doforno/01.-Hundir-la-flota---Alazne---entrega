import numpy as np
import variables as va
import time

# Define un tablero 10x10 con un valor específico en cada celda
def init_tablero():
    tablero = np.full((10, 10)," ")
    return tablero


# Tableros de juego
tablero_usuario = init_tablero()
tablero_maquina = init_tablero()
tablero_oculto = init_tablero()

# Define una orientación aleatoria entre horitzontal y vertical.
def orientacion():
    return np.random.choice(["horizontal", "vertical"])


# Función para comprobar que el barco entra en el tablero sin sobreponerse a otros
def espacio_tabla(tablero, tamaño, coord_x_barco, coord_y_barco, orientacion_barco):
    # Parámetros:
    # - tablero: La matriz que representa el tablero de juego.
    # - tamaño: El tamaño del barco que se quiere colocar.
    # - coord_x_barco: La coordenada x (fila) donde se intenta colocar el barco.
    # - coord_y_barco: La coordenada y (columna) donde se intenta colocar el barco.
    # - orientacion_barco: La orientación del barco, que puede ser "horizontal" o "vertical".

    # Devuelve:
    # - True si el barco puede ser colocado, False en caso contrario.

    if orientacion_barco == "horizontal":
        # Verifica si el barco entra en la tabla
        if coord_y_barco + tamaño > 10:
            return False
        # Verifica si no hay un barco en esa posición
        for eslora in range(tamaño):
            if tablero[coord_x_barco, coord_y_barco + eslora] != " ":
                return False

    else:  # Orientación vertical
        # Verifica si el barco entra en la tabla
        if coord_x_barco + tamaño > 10:
            return False
        # Verifica si no hay un barco en esa posición
        for eslora in range(tamaño):
            if tablero[coord_x_barco + eslora, coord_y_barco] != " ":
                return False

    return True


# Función para colocar un barco de manera aleatoria dentro del tablero y sin sobreponerse a otros barcos.
def colocar_barco(tablero, tamaño):
    # Parámetros:
    # - tablero: La matriz que representa el tablero de juego.
    # - tamaño: El tamaño del barco que se quiere colocar.

    # Devuelve:
    # - True si el barco se ha colocado, False si no se puedo colocar.

    while True:
        # Utiliza la función orientacón para seleccionar aleatoriamente la orientación del barco
        orientacion_barco = orientacion()
        # Genera coordenadas aleatorias para la posición del barco
        coord_x_barco = np.random.randint(0, 10)
        coord_y_barco = np.random.randint(0, 10)

        # Utiliza una función para comprobar si hay espacio para colocar el barco
        if espacio_tabla(tablero, tamaño, coord_x_barco, coord_y_barco, orientacion_barco):
            if orientacion_barco == "horizontal":
                # Coloca el barco "O" en la dirección horizontal
                for eslora in range(tamaño):
                    tablero[coord_x_barco, coord_y_barco + eslora] = "O"
            else:
                # Coloca el barco "O" en la dirección vertical
                for eslora in range(tamaño):
                    tablero[coord_x_barco + eslora, coord_y_barco] = "O"
            return True
        

# Función para jugar
def disparo(): 

    #Crea el tablero del usuario
    for tamaño in va.tamaños_de_barcos:
        colocado = False
        while not colocado:
            colocado = colocar_barco(tablero_usuario, tamaño)
    print(" Este es tu tablero:")
    time.sleep(1)
    print(tablero_usuario)
    time.sleep(1)
    print("\nEsperamos que te guste, no hay posibilidad de cambiarlo.\n")
    time.sleep(3)
    print("¡Buena suerte!\n")
    time.sleep(3)

    # Crea el tablero de la máquina
    for tamaño in va.tamaños_de_barcos:
        colocado = False
        while not colocado:
            colocado = colocar_barco(tablero_maquina, tamaño)

    while True: 

        # Turno del usuario
        coord_x = int(input('Introduce la coordenada x: \n'))
        coord_y = int(input('Introduce la coordenada y:\n'))

        # El usuario realiza un disparo exitoso, repite turno
        if tablero_maquina[coord_x, coord_y] == "O":
            tablero_maquina [coord_x, coord_y] = "X"
            tablero_oculto[coord_x, coord_y] = "X"
            time.sleep(1)
            print("\n¡Felicidades! ¡Has bombardeado el barco enemigo!")
            time.sleep(1)
            print(tablero_oculto)
            time.sleep(1)
            print("\nVuelves a disparar.\n")
            time.sleep(1)
            continue
        
        # El usuario realiza un disparo fallido.
        elif tablero_maquina[coord_x, coord_y] == " ":
            tablero_maquina[coord_x, coord_y] = "-"
            tablero_oculto[coord_x, coord_y] = "-"
            time.sleep(1)
            print("\n¡Agua! No has alcanzado ningún barco enemigo.")
            time.sleep(1)
            print(tablero_oculto)
            time.sleep(2)
            print("\nTurno de tu opositor\n")
            time.sleep(2)
            
        # El usuario realiza un disparo repetido, pierde su turno
        elif tablero_maquina[coord_x, coord_y] == "X" or tablero_maquina[coord_x, coord_y] == "-":
            time.sleep(1)
            print("\n¡Disparo previamente realizado! Pierdes una oportunidad.\n")
            time.sleep(1)
            print("\nTurno de tu rival ¡Protégete!\n")
            time.sleep(2)
            
        # El usuario gana la partida.
        if np.all(tablero_maquina != "O"):
            time.sleep(1)
            print("\n¡Felicidades! Has hundido todos los barcos.\n")
            time.sleep(1)
            print("¡Has ganado!")
            break
            
        

        #Turno de la máquina
        while True: 
            print("\nTu rival está disparando...\n")
            coord_x_aleatoria = np.random.randint(0,9)
            coord_y_aleatoria = np.random.randint(0,9)

            # El máqquina realiza un disparo exitoso, repite turno
            if tablero_usuario[coord_x_aleatoria, coord_y_aleatoria] == "O":
                tablero_usuario[coord_x_aleatoria, coord_y_aleatoria] = "X"
                time.sleep(1)
                print("¡Ouch! Tu rival ha bombardeado uno de tus barcos.")
                time.sleep(1)
                print(tablero_usuario)
                time.sleep(1)
                print("\nTu rival vuelve a disparar. ¡Cuida tus barcos!\n")
                time.sleep(2)
                continue

            # El máqquina realiza un disparo fallido
            elif tablero_usuario[coord_x_aleatoria, coord_y_aleatoria] == " ":
                tablero_usuario[coord_x_aleatoria, coord_y_aleatoria] = "-"
                time.sleep(1)
                print("¡Agua! ¡La maquina ha fallado!")
                time.sleep(1)
                print(tablero_usuario)
                time.sleep(1)
                print("\nEs tu turno.\n")
                time.sleep(2)
                break

            # La máquina realiza un disparo repetido, pierde su turno    
            elif tablero_usuario[coord_x_aleatoria, coord_y_aleatoria] == "X" or tablero_usuario[coord_x_aleatoria, coord_y_aleatoria] == "-":
                time.sleep(1)
                print("\nLa maquina ha repetido disparo y pierde su posibilidad.\n")
                time.sleep(0.5)
                print("\nEs tu turno.\n")
                time.sleep(2)
                break
            
            #La máquina gana la partida
            if np.all(tablero_usuario != "O"):
                time.sleep(1)
                print("¡Oh no! La maquina ha hundido todos tus barcos.\n")
                time.sleep(1)
                print("¡Has perdido!")
                break