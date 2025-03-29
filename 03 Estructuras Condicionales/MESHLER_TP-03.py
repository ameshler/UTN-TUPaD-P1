# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad_usuario = int(input("Por favor, ingrese su edad: "))
if edad_usuario > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.
nota_usuario = int(input("Por favor, ingrese su nota: "))
print("Aprobado") if nota_usuario >= 6 else print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input("Por favor, ingrese un número entero: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.
edad_usuario = int(input("Por favor, ingrese su edad: "))
if edad_usuario < 12:
    print("Usted es un niño/a.")
elif edad_usuario >=12 and edad_usuario < 18:
    print("Usted es un adolscente.")
elif edad_usuario >= 18 and edad_usuario < 30:
    print("Usted es un adulto/a joven.")
elif edad_usuario >= 30:
    print("Usted es un adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.
contrasenia = input("Por favor, ingrese una contraseña: ")
longitud = len(contrasenia)
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana > moda:
    sesgo = "Sesgo positivo"
elif media < mediana < moda:
    sesgo = "Sesgo negativo"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "Sesgo Indeterminado"

print("***RESULTADOS***")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Distribución: {sesgo}")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.
frase_usuario = input("Por favor, ingrese una frase o palabra: ")
ultima_letra = frase_usuario[-1]

if ultima_letra in "aeiou":
    frase_mostrar = frase_usuario + "!"
else:
    frase_mostrar = frase_usuario

print(frase_mostrar)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Por favor, ingrese su nombre: ")
print("Elige una opción:")
print("1. Mostrar tu nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Mostrar tu nombre en minúsculas. Por ejemplo: pedro.")
print("3. Mostrar tu nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
opcion = int(input("Ingresa el número de la opción que prefieras (1, 2 o 3): "))

if opcion == 1:
    mensaje = nombre.upper()
elif opcion == 2:
    mensaje = nombre.lower()
elif opcion == 3:
    mensaje = nombre.title()
else:
    mensaje = "Opcion inválida. Por favor, vuelva a intentar."

print(mensaje)

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Pidiendo al usuario que ingrese la magnitud del terremoto (mt)...
mt = float(input("Por favor, ingresa la magnitud de un terremoto: "))

# Validando mt en la escala de Richter y obtener resultado (er)...
if mt < 3:
    er = "Muy leve (imperceptible)."
elif mt >= 3 and mt < 4:
    er = "Leve (ligeramente perceptible)."
elif mt >= 4 and mt < 5:
    er = "Moderado (sentido por personas, pero generalmente no causa daños)."
elif mt >= 5 and mt < 6:
    er = "Fuerte (puede causar daños en estructuras débiles)."
elif mt >= 6 and mt < 7:
    er = "Muy Fuerte (puede causar daños significativos)."
else:
    er = "Extremo (puede causar graves daños a gran escala)."

print(f"La intensidad según la escala de Richter es: {er}")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Por favor, ingrese en que hemisferio se encuentra (N/S): ").lower()
mes = input("Ingrese el mes (ej: enero): ").lower()
dia = int(input("Ingrese el número de día: "))

# Validando hemisferio ingresado:
hemisferio_valido = True if hemisferio in ["n", "s"] else False
# Validando mes ingresado:
mes_valido = True if mes in ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"] else False
# Validando dia ingresado:
dia_valido = True if (dia >= 1 and dia <= 31) else False
estacion_valida = True 

# Determinando estacion a partir de los datos ingresados:
if mes in ["enero", "febrero"] or (mes == "diciembre" and dia >= 21) or (mes == "marzo" and dia <= 20):
    estacion = "invierno" if hemisferio == "n" else "verano"

elif mes in ["abril", "mayo"] or (mes == "marzo" and dia >= 21) or (mes == "junio" and dia <= 20):
    estacion = "primavera" if hemisferio == "n" else "otoño"

elif mes in ["julio", "agosto"] or (mes == "junio" and dia >= 21) or (mes == "septiembre" and dia <= 20):
    estacion = "verano" if hemisferio == "n" else "invierno"

elif mes in ["octubre", "noviembre"] or (mes == "septiembre" and dia >= 21) or (mes == "diciembre" and dia <= 20):
    estacion = "otoño" if hemisferio == "n" else "primavera"
else:
    estacion_valida = False

if (hemisferio_valido and mes_valido and dia_valido and estacion_valida):
    print(f"Se encuentra en la estación: {estacion}")
else:
    print("Usted ha ingresado datos inválidos, por favor vuelva a intentar")

