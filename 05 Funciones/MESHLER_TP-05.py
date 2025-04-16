from math import pi
def ejercicio1():
    # 1. Crear una función llamada imprimir_hola_mundo que imprima por
    # pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
    # programa principal.
    def imprimir_hola_mundo():
        print("Hola Mundo!")

    imprimir_hola_mundo()

def ejercicio2():
    # 2. Crear una función llamada saludar_usuario(nombre) que reciba
    # como parámetro un nombre y devuelva un saludo personalizado.
    # Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. # 
    # Llamar a esta función desde el programa
    # principal solicitando el nombre al usuario.
    def saludar_usuario(nombre):
        print(f"Hola {nombre}!")

    nombre = input("Ingrese su nombre: ")
    saludar_usuario(nombre)

def ejercicio3():
    # 3. Crear una función llamada informacion_personal(nombre, apellido,
    # edad, residencia) que reciba cuatro parámetros e imprima: “Soy
    # [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
    # Pedir los datos al usuario y llamar a esta función con los valores ingresados.
    def informacion_personal(nombre, apellido, edad, residencia):
        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    
    informacion_personal(nombre, apellido, edad, residencia)

def ejercicio4():
    # 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
    # y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como
    # parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
    # funciones para mostrar los resultados.
    def calcular_area_circulo(radio):
        area = pi * (radio ** 2)
        return area
    
    def calcular_perimetro_circulo(radio):
        perimetro = 2 * pi * radio
        return perimetro

    radio = float(input("Ingrese el radio del círculo (cm): "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    area = round(area, 2)
    perimetro = roun(perimetro, 2)

    print(f"El círculo de radio {radio} tiene un área de {area} cm2 y un perímetro de {perimetro} cm.")

def ejercicio5():
    # 5. Crear una función llamada segundos_a_horas(segundos) que reciba
    # una cantidad de segundos como parámetro y devuelva la cantidad
    # de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
    def segundos_a_horas(segundos):
        horas = segundos / 3600
        return horas
    
    segundos = int(input("Ingrese los segundos: "))
    horas = segundos_a_horas(segundos)

    print(f"{segundos} segundos equivalen a {horas} horas.")

def ejercicio6():
    # 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
    # número como parámetro y imprima la tabla de multiplicar de ese
    # número del 1 al 10. Pedir al usuario el número y llamar a la función.
    def tabla_multiplicar(numero):
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero*i}")

    numero = int(input("Ingrese el número: "))
    tabla_multiplicar(numero)

def ejercicio7():
    # 7. Crear una función llamada operaciones_basicas(a, b) que reciba
    # dos números como parámetros y devuelva una tupla con el resultado de sumarlos,
    # restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
    def operaciones_basicas(a, b):
        suma = a + b
        resta = a - b
        division = a / b
        multiplicacion = a * b
        return (suma, resta, multiplicacion, division)

    a = int(input("Ingrese un número: "))  
    b = int(input("Ingrese otro número: "))
    s, r, m, d = operaciones_basicas(a,b)

    print("Resultados:")
    print(f"{a} + {b} = {s}")
    print(f"{a} - {b} = {r}")
    print(f"{a} x {b} = {m}")
    print(f"{a} / {b} = {d}")

def ejercicio8():
    # 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
    # peso en kilogramos y la altura en metros, y devuelva el índice de
    # masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
    # para mostrar el resultado con dos decimales.
    def calcular_imc(peso, altura):
        imc = peso / (altura**2)
        imc = round(imc, 2)
        return imc

    peso = float(input("Ingrese su peso(kg): "))
    altura = float(input("Ingrese su altura(m): "))
    imc = calcular_imc(peso, altura)
    print(f"El índice de masa corporal es: {imc}")

def ejercicio9():
    # 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
    # una temperatura en grados Celsius y devuelva su equivalente en
    # Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
    # resultado usando la función.
    def celsius_a_fahrenheit(celsius):
        f = celsius * 9/5 + 32
        f = round(f, 2)
        return f

    c = float(input("Ingrese la temperatura en Celsius: "))
    f = celsius_a_fahrenheit(c)

    print(f"{c} grados Celsius equivalen a {f} grados Farenheit.")

def ejercicio10():
    # 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
    # tres números como parámetros y devuelva el promedio de ellos.
    # Solicitar los números al usuario y mostrar el resultado usando esta
    # función.
    def calcular_promedio(a, b, c):
        p = (a+b+c)/3
        return p

    a = float(input("Ingrese un número: "))
    b = float(input("Ingrese otro número: "))
    c = float(input("Ingrese el último número: "))

    p = calcular_promedio(a, b, c)

    print(f"El promedio es: {p}")

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

while True:
    print("***EJERCICIOS TP 5 - FUNCIONES***")
    ejercicio = input("Indique el número de ejercicio desea ejecutar (1-10), 0 para salir: ")
    if ejercicio == '0':
        break

    if ejercicio in ejercicios:
        ejercicios[ejercicio]()
