import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos_restantes = 10

    print("¡Bienvenido al juego de Adivina el Número!")
    print("Tienes 10 intentos para adivinar el número secreto del 1 al 100.")

    while intentos_restantes > 0:
        print("\nIntentos restantes:", intentos_restantes)
        intento = int(input("Introduce un número: "))

        if intento == numero_secreto:
            print("¡Felicidades! ¡Has adivinado el número secreto en", 10 - intentos_restantes + 1, "intentos!")
            return
        elif intento < numero_secreto:
            print("El número secreto es mayor que", intento)
        else:
            print("El número secreto es menor que", intento)

        intentos_restantes -= 1

    print("\nLo siento, has agotado tus intentos.")
    print("El número secreto era:", numero_secreto)

adivina_el_numero()