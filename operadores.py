# Ejemplos de operadores en Python explicados de forma sencilla

# Operadores aritméticos (para hacer cuentas)
a = 10
b = 3

# Sumar (+)
suma = a + b  # 10 + 3 = 13
print("Suma:", suma)

# Restar (-)
resta = a - b  # 10 - 3 = 7
print("Resta:", resta)

# Multiplicar (*)
multiplicacion = a * b  # 10 * 3 = 30
print("Multiplicación:", multiplicacion)

# Dividir (/)
division = a / b  # 10 / 3 = 3.333...
print("División:", division)

# Dividir y quedarte con el número entero (//)
division_entera = a // b  # 10 // 3 = 3
print("División entera:", division_entera)

# El resto de una división (%)
resto = a % b  # 10 % 3 = 1
print("Resto:", resto)

# Elevar a una potencia (**)
potencia = a ** b  # 10 ** 3 = 1000
print("Potencia:", potencia)

# Operadores de comparación (para comparar cosas)
x = 5
y = 8

# ¿Son iguales? (==)
print("¿x es igual a y?", x == y)  # False

# ¿Son diferentes? (!=)
print("¿x es diferente de y?", x != y)  # True

# ¿x es más grande que y? (>)
print("¿x es mayor que y?", x > y)  # False

# ¿x es más pequeño que y? (<)
print("¿x es menor que y?", x < y)  # True

# Operadores lógicos (para combinar condiciones)
llueve = True
tengo_paraguas = False

# AND (y)
print("¿Llueve y tengo paraguas?", llueve and tengo_paraguas)  # False

# OR (o)
print("¿Llueve o tengo paraguas?", llueve or tengo_paraguas)  # True

# NOT (no)
print("¿No está lloviendo?", not llueve)  # False

# Operadores de asignación (para guardar valores)
z = 10
z += 5  # Es lo mismo que z = z + 5
print("Nuevo valor de z:", z)  # 15