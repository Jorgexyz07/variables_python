# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print("Ingrese un número real")
num_1 = float(input())
print("Ingrese otro número real")
num_2 = float(input())
suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2
division = num_1 / num_2
exponente = num_1 ** num_2
print("La suma entre", num_1, "y", num_2, "es", suma)
print("La resta entre", num_1, "y", num_2, "es", resta) 
print("La multiplicación entre", num_1, "y", num_2, "es", multiplicacion)
print("La división entre", num_1, "y", num_2, "es", division)
print("La exponencial entre", num_1, "y", num_2, "es", exponente)
