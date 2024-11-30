import random

class JuegoAdivinanza:
    def __init__(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def validar_numero(self, numero):
        if numero < self.numero_secreto:
            print("El número es mayor.")
        elif numero > self.numero_secreto:
            print("El número es menor.")
        else:
            print("¡Correcto!")
            return True
        return False

    def registrar_intento(self):
        self.intentos += 1

    def reiniciar(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def registrar_partida(self, intentos, gano):
        self.historial.append({"intentos": intentos, "gano": gano})

    def mostrar_estadisticas(self):
        partidas_jugadas = len(self.historial)
        partidas_ganadas = sum(1 for partida in self.historial if partida["gano"])
        porcentaje_aciertos = (partidas_ganadas / partidas_jugadas * 100) if partidas_jugadas > 0 else 0

        print(f"Nombre: {self.nombre}")
        print(f"Partidas jugadas: {partidas_jugadas}")
        print(f"Partidas ganadas: {partidas_ganadas}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")

def guardar_estadisticas(jugador):
    with open("estadisticas.txt", "w") as archivo:
        for partida in jugador.historial:
            archivo.write(f"{partida['intentos']}, {partida['gano']}\n")

def cargar_estadisticas(jugador):
    try:
        with open("estadisticas.txt", "r") as archivo:
            for linea in archivo:
                intentos, gano = linea.strip().split(", ")
                jugador.historial.append({"intentos": int(intentos), "gano": gano == "True"})
    except FileNotFoundError:
        pass

def menu():
    nombre_jugador = input("Ingrese su nombre: ")
    jugador = Jugador(nombre_jugador)
    cargar_estadisticas(jugador)
    juego = JuegoAdivinanza()

    while True:
        print("\nMenú:")
        print("1. Comenzar una nueva partida")
        print("2. Ver las estadísticas del jugador")
        print("3. Salir del juego")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            juego.reiniciar()
            print("Nueva partida iniciada. ¡Adivina el número!")

            while True:
                numero = int(input("Ingrese un número: "))
                juego.registrar_intento()
                if juego.validar_numero(numero):
                    jugador.registrar_partida(juego.intentos, True)
                    break

        elif opcion == "2":
            jugador.mostrar_estadisticas()

        elif opcion == "3":
            guardar_estadisticas(jugador)
            print("Estadísticas guardadas. ¡Hasta luego!")
            break

        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()
