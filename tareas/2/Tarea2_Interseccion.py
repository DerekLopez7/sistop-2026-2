import threading
import time
import random

# Un solo carril disponible: solo un auto puede cruzar a la vez
sem_interseccion = threading.Semaphore(1)

# Direcciones posibles
direcciones = ["NORTE", "SUR", "ESTE", "OESTE"]

def carro(id_carro, direccion):
    while True:
        # El carro llega a la intersección
        print(f"Carro {id_carro} llega desde {direccion}.")
        time.sleep(random.uniform(0.2, 0.5))

        # Intenta entrar
        sem_interseccion.acquire()
        print(f"Carro {id_carro} entra a la intersección desde {direccion}.")

        # Tiempo cruzando
        time.sleep(random.uniform(0.4, 1.0))

        # Sale
        print(f"Carro {id_carro} sale de la intersección desde {direccion}.")
        sem_interseccion.release()

        # Vuelve a llegar después de un tiempo
        time.sleep(random.uniform(0.5, 1.3))


def generar_carros():
    id_contador = 1
    while True:
        direccion = random.choice(direcciones)
        threading.Thread(target=carro, args=(id_contador, direccion)).start()
        id_contador += 1
        time.sleep(random.uniform(0.4, 1.2))


def main():
    print("Simulación de intersección iniciada...")
    generador = threading.Thread(target=generar_carros)
    generador.start()


if __name__ == "__main__":
    main()
