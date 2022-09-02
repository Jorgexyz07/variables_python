# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
print('Ingrese por consola el primer número entero a operar:')
numero_1 = int(input())

print('Ingrese por consola el segundo número entero a operar:')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números enteros solicitados
# print(....)
print ("Los dos números enteros solicitados son:", numero_1, "y", numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma

# Resta

# División

# Multiplicación
suma = numero_1 + numero_2
resta = numero_1 - numero_2
division_entera = int(numero_1 / numero_2)
division_decimal = numero_1 / numero_2
multiplicacion = numero_1 * numero_2
print ("La suma de los dos números enteros solicitados es:", suma)
print ("La resta de los dos números enteros solicitados es:", resta)
print ("La multiplicación de los dos números enteros solicitados es:", multiplicacion)
print ("La división entera entre los dos números enteros solicitados es:", division_entera)
print ("La división entre los dos números enteros solicitado es:", division_decimal)
print (f"La división, con dos decimales, entre los dos números enteros solicitados es: {division_decimal:.3}")


