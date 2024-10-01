import random

numero_secreto = random.randint(0,100)
cant_intentos = 0
cantidad_max_intentos = 10
adivinando = False
print ("Hola, sos bienvenido al juego de adivinanza, adiviná el número secreto pero en menos de 10 intentos")

while not adivinando :
    if not cant_intentos < cantidad_max_intentos:
        print ("no has podido adivinar :( lo siento pero ya superaste la cantidad máxima de intentos")
        break

    entrada = input("introduce un número del 1 al 99: ")
    numero = int (entrada)
    
    if numero == numero_secreto:
        print ("felicitaciones has adivinado el numero secreto")
        adivinando = True
    elif numero < numero_secreto:
        print ("el numero ingresado es menor, sigue probando")
        
    else:
        print ("el numero ingresado es mayor, sigue probando")
    cant_intentos += 1

