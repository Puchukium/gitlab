import random

def juego_adivina_numero():
    print("¡Bienvenido al juego de adivinar el número!")
    
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    while True:
        # Pedir al usuario que ingrese un número
        try:
            guess = int(input("Ingresa tu suposición: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        # Incrementar el contador de intentos
        intentos += 1
        
        # Verificar si el número ingresado es igual al número secreto
        if guess == numero_secreto:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break
        elif guess < numero_secreto:
            print("El número es mayor. ¡Intenta nuevamente!")
        else:
            print("El número es menor. ¡Intenta nuevamente!")

if __name__ == "__main__":
    juego_adivina_numero()
