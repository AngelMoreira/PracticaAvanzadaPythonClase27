import random

# Variables globales para el rango y los intentos máximos
rango_min = 1
rango_max = 100
intentos_max = 5
numero_secreto = random.randint(rango_min, rango_max)

# Función para pedir una adivinanza
def pedir_adivinanza():
    try:
        return int(input(f"Adivina el número (entre {rango_min} y {rango_max}): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return pedir_adivinanza()

# Función para pedir el rango y los intentos máximos
def configurar_juego():
    global rango_min, rango_max, intentos_max, numero_secreto
    try:
        rango_min = int(input("Ingresa el valor mínimo del rango: "))
        rango_max = int(input("Ingresa el valor máximo del rango: "))
        intentos_max = int(input("Ingresa el número máximo de intentos: "))
        if rango_min >= rango_max or intentos_max <= 0:
            print("Valores inválidos. Inténtalo de nuevo.")
            configurar_juego()
        else:
            numero_secreto = random.randint(rango_min, rango_max)
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")
        configurar_juego()

# Función principal del juego
def juego_adivinanza():
    intentos = 0
    while intentos < intentos_max:  # Bucle while
        adivinanza = pedir_adivinanza()
        intentos += 1
        
        if adivinanza < numero_secreto:  # Bifurcación doble
            print("Demasiado bajo.")
        elif adivinanza > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
            break
    else:
        print(f"Lo siento, no adivinaste el número. El número era {numero_secreto}.")

# Función principal para iniciar el juego
def main():
    configurar_juego()
    juego_adivinanza()

# Llamamos a la función principal
main()
