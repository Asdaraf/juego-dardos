# Input que ingresa a los jugadores
jugadores = input("Ingrese los nombres de los jugadores: ")
jugadores = jugadores.upper()
jugadores = jugadores.split(" ")

jugador1 = jugadores[0][0:3]
jugador2 = jugadores[1][0:3]
if jugador1 == jugador2:
    jugador2 = f"{jugador2}2"

puntaje_jugador1 = 501
puntaje_jugador2 = 501

print(f"\033[1m{jugador1} {puntaje_jugador1}\033[0m")
print(f"\033[1m{jugador2} {puntaje_jugador2}\033[0m")

#Funcion para cada lanzamiento y verifica si cumple
def lanzamiento():
    global x
    x = input()
    x = x.upper()
    if x == "SIMPLE BULL":
        x = 25
        return x
    elif x == "DOUBLE BULL":
        x = 50
        return x
    elif x == "NULL":
        x = 0
        return x
    else:
        x = x.split(" ")
        if len(x) == 2:
            if x[0].isnumeric() and x[1].isnumeric():
                y = int(x[0])
                z = int(x[1])

                if y > 3 or z > 20:
                    print("Error. Debes ingresar un numero entre 1 y 3, y entre 1 y 20")
                    quit()
                else:
                    x = y * z
                    return x
            else:
                print("Error al ingresar la jugada.")
                quit()
        else:
            print("Error al ingresar la jugada.")
            quit()

# 6 lanzamientos e imprime resultado. Si llega a 0 gana.
while True:
    for i in range(6):
        lanzamiento()
        if i < 3:
            puntaje_jugador1 = abs(puntaje_jugador1 - x)
            if puntaje_jugador1 == 0:
                break
        elif i < 6:
            puntaje_jugador2 = abs(puntaje_jugador2 - x)
            if puntaje_jugador2 == 0:
                break

    print(f"\033[1m{jugador1} {puntaje_jugador1}\033[0m")
    print(f"\033[1m{jugador2} {puntaje_jugador2}\033[0m")

    if puntaje_jugador1 == 0:
        print(f"\033[1mGana {jugador1}. Felicidades!\033[0m")
        break
    elif puntaje_jugador2 == 0:
        print(f"\033[1mGana {jugador2}. Felicidades!\033[0m")
        break
    else:
        continue