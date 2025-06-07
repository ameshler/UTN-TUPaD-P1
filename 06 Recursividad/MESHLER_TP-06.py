def ejercicio1():
    # Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
    # función para calcular y mostrar en pantalla el factorial de todos los números enteros 
    # entre 1 y el número que indique el usuario
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        return num * factorial(num - 1)
    
    n = int(input("Ingrese el número al que le quiere calcular el factorial: "))
    print(f"El factorial de {n} es {factorial(n)}")

def ejercicio2():
    # Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
    # indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
    # especifique.
    def fibonacci(pos):
        if pos == 0:
            return 0
        elif pos == 1:
            return 1
        else:
            return fibonacci(pos-1) + fibonacci(pos-2)
        
    p = int(input("Ingrese la posición de la serie de Fibonacci que quiere obtener: "))

    if p >= 0:
        print(f"En la posicion {p} de la serie de Fibonacci se encuentra el valor {fibonacci(p)}")
    else:
        print("La posicion debe ser un número entero positivo. Vuelva a intentar.")

def ejercicio3():
    # Crea una función recursiva que calcule la potencia de un número base elevado a un 
    # exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
    # logaritmo general
    def potencia(base, exponente):
        if exponente == 0:
            return 1 
        return base * potencia(base, exponente - 1)
    
    b = int(input("Ingrese la base de la potencia a calcular: "))
    e = int(input("Ingrese el exponente de la potencia a calcular: "))

    print(f"{b}^{e} = {potencia(b,e)}")

def ejercicio4():
    # Crear una función recursiva en Python que reciba un número entero positivo en base 
    # decimal y devuelva su representación en binario como una cadena de texto.
    # Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y 
    # unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este 
    # procedimiento:
    #     1. Dividir el número por 2.
    #     2. Guardar el resto (0 o 1).
    #     3. Repetir el proceso con el cociente hasta que llegue a 0.
    #     4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
    # Convertir el número 10 a binario:
    #     10 ÷ 2 = 5 resto: 0 
    #     5 ÷ 2 = 2 resto: 1 
    #     2 ÷ 2 = 1 resto: 0 
    #     1 ÷ 2 = 0 resto: 1 
    # Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
    def decimal_a_binario(n):
        if n == 0:
            return "0"
        elif n == 1:
            return "1"
        else:
            return decimal_a_binario(n // 2) + str(n % 2)
    
    num = int(input("Ingrese el número decimal que desea pasar a binario: "))
    print(f"{num} decimal es igual a {decimal_a_binario(num)} en binario.")

def ejercicio5():
    # Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
    # cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
    # lo es.
    # Requisitos:
    # La solución debe ser recursiva.
    # No se debe usar [::-1] ni la función reversed().
    def es_palindromo(palabra):
        if len(palabra) <= 1:
            return True
        if palabra[0] != palabra[-1]:
            return False
        return es_palindromo(palabra[1:-1])
    
    p = input("Ingrese una palabra, se determinará si es o no un palíndromo: ")
    print(f"{p} es un palíndromo") if es_palindromo(p) else print(f"{p} no es un palíndromo")

def ejercicio6():
    # Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
    # número entero positivo y devuelva la suma de todos sus dígitos.
    # Restricciones:
    #     No se puede convertir el número a string.
    #     Usá operaciones matemáticas (%, //) y recursión.
    # Ejemplos:
    #     suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
    #     suma_digitos(9) → 9
    #     suma_digitos(305) → 8 (3 + 0 + 5)
    def suma_digitos(n):
        if n < 10:
            return n
        else:
            return n%10 + suma_digitos(n//10)
    
    num = int(input("Ingrese un número entero: "))
    print(f"La suma de los dígitos de {num} es {suma_digitos(num)}")

def ejercicio7():
    # Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
    # bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
    # último nivel con un solo bloque.
    # Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
    # nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
    # pirámide.
    # Ejemplos:
    # contar_bloques(1) → 1 (1)
    # contar_bloques(2) → 3 (2 + 1)
    # contar_bloques(4) → 10 (4 + 3 + 2 + 1)
    def contar_bloques(n):
        if n == 1:
            return 1
        else:
            return n + contar_bloques(n - 1)

    bloques_base = int(input("Ingrese la cantidad de bloques de la base de la pirámide: "))
    print(f"Con {bloques_base} en la base se necesitarán {contar_bloques(bloques_base)} para completar la pirámide.")

def ejercicio8():
    # Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
    # número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
    # aparece ese dígito dentro del número.
    # Ejemplos:
    # contar_digito(12233421, 2) → 3 
    # contar_digito(5555, 5) → 4
    # contar_digito(123456, 7) → 0 
    def contar_digito(numero, digito):
        if numero == 0:
            return 0
        if numero%10 == digito:
            return 1 + contar_digito(numero//10, digito) 
        else:
            return 0 + contar_digito(numero//10, digito)

    n = int(input("Ingrese un número entero positivo: "))
    d = int(input("Ingrese el dígito que desea buscar: "))
    print(f"El dígito {d} apacece {contar_digito(n, d)} veces en {n}")

ejercicios = {
    '1': ejercicio1,
    '2': ejercicio2,
    '3': ejercicio3,
    '4': ejercicio4,
    '5': ejercicio5,
    '6': ejercicio6,
    '7': ejercicio7,
    '8': ejercicio8
}

while True:
    print("***EJERCICIOS TP 6 - RECURSIVIDAD***")
    ejercicio = input("Indique el número de ejercicio desea ejecutar (1-8), 0 para salir: ")
    if ejercicio == '0':
        break

    if ejercicio in ejercicios:
        ejercicios[ejercicio]()