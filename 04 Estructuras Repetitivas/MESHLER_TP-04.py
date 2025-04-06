import random
# Funciones ejercicios
def ejercicio1():
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
    for i in range(101):
        print(i)

def ejercicio2():
# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene
    numero = int(input("Ingrese un número entero: "))
    aux = numero
    cant_digitos = 0

    while aux > 0:
        aux = aux // 10
        cant_digitos += 1
    
    print(f"{numero} tiene {cant_digitos} dígitos.")

def ejercicio3():
# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.
    print("Se sumarán todos los enteros comprendidos entre dos numeros, excluyendo los valores ingresados.")
    min = int(input("Ingrese el número menor: "))
    max = int(input("Ingrese el número mayor: "))
    suma = 0

    if min >= max:
        print("Datos incorrectos, vuelva a intentar.")
    else:
        for i in range(min+1, max):
            suma += i

        print(f"La suma de los enteros entre {min} y {max} es {suma}.")

def ejercicio4():
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.
    num = int(input("Ingrese un número entero para iniciar la suma, 0 para terminar: "))
    suma = 0

    while num != 0:
        suma += num
        num = int(input("Ingrese el número siguiente, 0 para terminar: "))

    print(f"La suma de los números ingresadis es: {suma}")

def ejercicio5():
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
    aleatorio = random.randint(0, 9)
    cant_intentos = 1

    print("Se generó aleatoriamente un número entre 0 y 9..")
    numero = int(input("Cuál es el numero?: "))
    while numero != aleatorio:
        cant_intentos += 1
        numero = int(input("Incorrecto. Cuál es el numero?: "))

    print(f"Correcto! El número es {numero}, lo adivinó en {cant_intentos} intentos.")

def ejercicio6():
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.
    for i in range(98, 0, -2):
        print(i)

def ejercicio7():
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.
    num =int(input("Se sunmarán todos los enteros comprendidos entre 0 y el número que ingrese a continuación: "))

    if num <= 0:
        print("Incorrecto. Debe ingresar un entero positivo. Vuelva a intentar.")
    else:
        aux = num - 1
        suma = 0
        while aux > 0:
            suma += aux
            aux -= 1
        
        print(f"La suma de los enteros comprendidos entre 0 y {num} es {suma}")

def ejercicio8():
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
    cant_numeros = 100
    cant_pares = 0
    cant_impares = 0
    cant_positivos = 0
    cant_negativos = 0

    for i in range(cant_numeros):
        num = int(input("Ingrese un número entero: "))
        if num % 2 == 0:
            cant_pares += 1
        else:
            cant_impares += 1
        if num > 0:
            cant_positivos += 1
        else:
            cant_negativos += 1
            
    print(f"Usted ingresó {cant_numeros} numeros:")
    print(f"La cantidad de pares es: {cant_pares}")
    print(f"La cantidad de impares es: {cant_impares}")
    print(f"La cantidad de positivos es: {cant_positivos}")
    print(f"La cantidad de negativos es: {cant_negativos}")

def ejercicio9():
# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).
    cant_numeros = 100
    suma = 0
    for i in range(cant_numeros):
        num = int(input("Ingrese un número entero: "))
        suma += num

    media = suma/cant_numeros

    print(f"La media de los {cant_numeros} números ingresados es: {media}.")

def ejercicio10():
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
    numero = int(input("Ingrese un número entero de más de un dígito: "))
    aux = numero # Uso una variable aux para mantener el valor del número ingresado por el usuario
    numero_invertido = 0

    while aux > 0:
        digito = aux % 10 # para obtener el primer digito del número guardado en aux
        numero_invertido = numero_invertido * 10 + digito # para ir armando el num invertido
        aux //= 10 # división entera para eliminar el dígito ya procesado

    print(f"Usted ingresó el número {numero}, invertido queda {numero_invertido}")

# Diccionario ejercicios
ejercicios = {
    '1': ejercicio1,
    '2': ejercicio2,
    '3': ejercicio3,
    '4': ejercicio4,
    '5': ejercicio5,
    '6': ejercicio6,
    '7': ejercicio7,
    '8': ejercicio8,
    '9': ejercicio9,
    '10': ejercicio10
}

# Selector de ejercicios a ejecutar
while True:
    print("***EJERCICIOS TP 4 - ESTRUCTURAS REPETITIVAS***")
    ejercicio = input("Indique el número de ejercicio desea ejecutar (1-10), 0 para salir: ")
    if ejercicio == '0':
        break

    if ejercicio in ejercicios:
        ejercicios[ejercicio]()
