def ejercicio1():
    # Dado el diccionario precios_frutas
    # precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
    # 1450}
    # Añadir las siguientes frutas con sus respectivos precios:
    #     ● Naranja = 1200
    #     ● Manzana = 1500
    #     ● Pera = 2300
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

    precios_frutas["Naranja"] = 1200
    precios_frutas["Manzana"] = 1500
    precios_frutas["Pera"] = 2300

    print(precios_frutas)

def ejercicio2():
    # Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
    # desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
    #     ● Banana = 1330
    #     ● Manzana = 1700
    #     ● Melón = 2800
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

    precios_frutas["Banana"] = 1330
    precios_frutas["Manzana"] = 1700
    precios_frutas["Melón"] = 2800

    print(precios_frutas)

def ejercicio3():
    # Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
    # desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
    # precios.
    precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

    frutas = list(precios_frutas.keys())

    print(frutas)

def ejercicio4():
    # Escribí un programa que permita almacenar y consultar números telefónicos.
    #     • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
    #     • Luego, pedí un nombre y mostrale el número asociado, si existe.
    contactos = {}
    #Permitir cargar 5 contactos
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        telefono = input(f"Ingrese el número de teléfono de {nombre}: ")
        contactos[nombre] = telefono

    # Búsqueda de contactos:
    while True:
        nombre_buscar = input("Ingrese el nombre de contacto que quiere buscar: ")
        telefono_encontrado = contactos.get(nombre_buscar)
        if telefono_encontrado != None:
            print(telefono_encontrado)
            break
        else:
            print("El contacto no existe, vuelva a intentar...")
        
def ejercicio5():
    # Solicita al usuario una frase e imprime:
    #     • Las palabras únicas (usando un set).
    #     • Un diccionario con la cantidad de veces que aparece cada palabra.
    # Pedir frase al usuario
    frase = input("Ingrese una frase: ")
    # Separar palabras
    palabras = frase.split()
    # Obtener palabras únicas
    palabras_unicas = set(palabras)
    # Contar palabras
    frecuencia_palabras = {}
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    # Mostrar resultados
    print(f"\nPalabras únicas: {palabras_unicas}")
    print(f"Frecuencia palabras: {frecuencia_palabras}")

def ejercicio6():
    # Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
    # Luego, mostrá el promedio de cada alumno
    alumnos = {}

    # Cargar datos de 3 alumnos
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        notas = input(f"Ingrese 3 notas separadas por espacios para {nombre}: ")
        
        # Convertir las notas a tupla de enteros o flotantes
        notas_tupla = tuple(map(float, notas.split()))
        
        # Verificar que sean 3 notas
        if len(notas_tupla) != 3:
            print("Error: Debe ingresar exactamente 3 notas.")
            continue
        
        alumnos[nombre] = notas_tupla

    # Mostrar promedios
    print("\nPromedios de los alumnos:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")

def ejercicio7():
    # Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
    # y Parcial 2:
    # • Mostrá los que aprobaron ambos parciales.
    # • Mostrá los que aprobaron solo uno de los dos.
    # • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
    # Sets de estudiantes que aprobaron cada parcial
    parcial1 = {"Ana", "Luis", "María", "Juan"}
    parcial2 = {"Luis", "Pedro", "María", "Sofía"}

    # Aprobaron ambos parciales, intersección
    ambos = parcial1 & parcial2

    # Aprobaron solo uno, diferencia simétrica
    solo_uno = parcial1 ^ parcial2

    # Estudiantes que aprobaron al menos uno, unión
    al_menos_uno = parcial1 | parcial2

    # Mostrar resultados
    print("Aprobaron ambos parciales:", ambos)
    print("Aprobaron solo uno de los dos:", solo_uno)
    print("Aprobaron al menos un parcial:", al_menos_uno)

def ejercicio8():
    # Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
    # Permití al usuario:
    # • Consultar el stock de un producto ingresado.
    # • Agregar unidades al stock si el producto ya existe.
    # • Agregar un nuevo producto si no existe

    # Diccionario inicial de productos
    stock = {
        "manzanas": 50,
        "naranjas": 30,
        "bananas": 20
    }

    while True:
        producto = input("\nIngrese el nombre del producto (o 'salir' para terminar): ").lower()
        if producto == "salir":
            break

        if producto in stock:
            print(f"Stock actual de '{producto}': {stock[producto]}")
            agregar = input("¿Desea agregar unidades? (s/n): ").lower()
            if agregar == "s":
                unidades = int(input("¿Cuántas unidades desea agregar?: "))
                stock[producto] += unidades
                print(f"Nuevo stock de '{producto}': {stock[producto]}")
        else:
            print(f"'{producto}' no está en el inventario.")
            agregar_nuevo = input("¿Desea agregarlo como nuevo producto? (s/n): ").lower()
            if agregar_nuevo == "s":
                unidades = int(input("¿Cuántas unidades desea agregar?: "))
                stock[producto] = unidades
                print(f"'{producto}' agregado con {unidades} unidades.")

    # Mostrar stock final
    print("\nStock final de productos:")
    for prod, cant in stock.items():
        print(f"{prod}: {cant} unidades")

def ejercicio9():
    # Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
    # Permití consultar qué actividad hay en cierto día y hora.
    # Agenda con tuplas como clave (día, hora) y el evento como valor
    orden_dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    agenda = {
        ("lunes", "14:00"): "Reunión de equipo",
        ("martes", "09:00"): "Clase de matemáticas",
        ("viernes", "18:00"): "Gimnasio"
    }

    while True:
        dia = input("\nIngrese el día (o 'salir' para terminar): ").lower()
        if dia == "salir":
            break

        hora = input("Ingrese la hora (formato HH:MM): ")

        clave = (dia, hora)
        if clave in agenda:
            print(f"Existe una actividad agendada el {dia} a las {hora}: {agenda[clave]}")
        else:
            print(f"No hay ninguna actividad agendada el {dia} a las {hora}.")
            agregar = input("¿Desea agendar una nueva actividad en ese horario? (s/n): ").lower()
        if agregar == "s":
            evento = input("Ingrese el nombre del evento: ")
            agenda[clave] = evento
            print(f"Evento '{evento}' agendado el {dia} a las {hora}.")

    # Ordenar diccionario para imprimirlo:
    agenda_ordenada = sorted(
    agenda.items(),
    key=lambda item: (orden_dias.index(item[0][0]), item[0][1])
    )
    # Mostrar agenda completa al finalizar
    print("\nAgenda final:")
    for (dia, hora), evento in agenda_ordenada:
        print(f"{dia.capitalize()} {hora}: {evento}")

def ejercicio10():
    # Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
    # diccionario donde:
    # • Las capitales sean las claves.
    # • Los países sean los valores

    # Diccionario original: país -> capital
    paises_a_capitales = {
        "Argentina": "Buenos Aires",
        "Brasil": "Brasilia",
        "Francia": "París",
        "Japón": "Tokio",
        "Italia": "Roma"
    }

    # Crear nuevo diccionario: capital -> país
    capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

    # Mostrar resultados
    print("Diccionario original (país -> capital):")
    print(paises_a_capitales)

    print("\nDiccionario invertido (capital -> país):")
    print(capitales_a_paises)


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
    print("\n***EJERCICIOS TP - DATOS COMPLEJOS***")
    ejercicio = input("Indique el número de ejercicio desea ejecutar (1-10), 0 para salir: ")
    if ejercicio == '0':
        break

    if ejercicio in ejercicios:
        ejercicios[ejercicio]()