def ejercicio1():
    # 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
    # range.
    multiplos_de_4 = list(range(4, 101, 4))
    # se imprime lista para verificar resultado
    print(multiplos_de_4)

def ejercicio2():
    # 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
    # penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
    # indexing con números negativos!
    vocales = ["a", "e", "i", "o", "u"]

    print(f"El penúltimo elemento es: {vocales[-2]}")

def ejercicio3():
    # 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
    # pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

    lista = []
    lista.append("Vale")
    lista.append("Bere")
    lista.append("Paty")

    print(f"La lista resultante es: {lista}")

def ejercicio4():
    # Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
    # respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
    # en los videos o bien investigar cómo funciona el indexing con números negativos!
    
    animales = ["perro", "gato", "conejo", "pez"]

    # Reemplazar el segundo valor por "loro"
    animales[1] = "loro"
    # Reemplazar el último valor por "oso"
    animales[-1] = "oso"

    print(f"La lista resultante es: {animales}")

def ejercicio5():
    # Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza:
    # Se crea la lista numeros y se inicializa con 5 elementos de tipo int
    numeros = [8, 15, 3, 22, 7]
    # Se elimina de la lista el elemento cuyo valor es el máximo, en este ejemplo es el 22
    numeros.remove(max(numeros))
    # Se muestra por pantalla la lista resultante
    print(numeros)

def ejercicio6():
    # Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
    # pantalla los dos primeros.
    numeros = list(range(10, 31, 5))
    print(f"Los dos primeros números de la lista son: {numeros[:2]}")

def ejercicio7():
    # Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
    # cualesquiera.
    autos = ["sedan", "polo", "suran", "gol"]

    # reemplazar valores centrales
    autos[1] = "bora"
    autos[2] = "voyage"
    # mostrar la lista resultante
    print(f"La lista resultante es: {autos}")

def ejercicio8():
    # Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
    # directamente. Imprimir la lista resultante por pantalla.
    dobles = []
    dobles.append(2 * 5)
    dobles.append(2 * 10)
    dobles.append(2 * 15)

    print(f"La lista resultante es: {dobles}")

def ejercicio9():
    # Dada la lista “compras”, cuyos elementos representan los productos comprados por
    # diferentes clientes:
    # compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
    # ["agua"]]
    # a) Agregar "jugo" a la lista del tercer cliente usando append.
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    # c) Eliminar "pan" de la lista del primer cliente.
    # d) Imprimir la lista resultante por pantalla

    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

    # a)
    compras[2].append("jugo")
    # b)
    indice_fideos = compras[1].index("fideos")
    compras[1][indice_fideos] = "tallarines"
    # c)
    compras[0].remove("pan")
    # d)
    print(f"La lista resultante es: {compras}")

def ejercicio10():
    # Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    # ● Posición lista_anidada[0]: 15
    # ● Posición lista_anidada[1]: True
    # ● Posición lista_anidada[2][0]: 25.5
    # ● Posición lista_anidada[2][1]: 57.9
    # ● Posición lista_anidada[2][2]: 30.6
    # ● Posición lista_anidada[3]: False
    # Imprimir la lista resultante por pantalla

    lista_anidada = [
    15, 
    True, 
    [25.5, 57.9, 30.6], 
    False
    ]
    
    print(lista_anidada)

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
    print("***EJERCICIOS TP 5.1 - LISTAS***")
    ejercicio = input("Indique el número de ejercicio desea ejecutar (1-10), 0 para salir: ")
    if ejercicio == '0':
        break

    if ejercicio in ejercicios:
        ejercicios[ejercicio]()