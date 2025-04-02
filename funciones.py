# Ejemplo 1: Función que suma dos números
def sumar(a, b):
    """
    Esta función toma dos argumentos (a y b) y devuelve su suma.
    """
    return a + b

# Uso:
resultado = sumar(3, 5)  # Llama a la función con 3 y 5 como argumentos
print(f"La suma es: {resultado}")  # Imprime "La suma es: 8"


# Ejemplo 2: Función que verifica si un número es par
def es_par(numero):
    """
    Esta función verifica si un número es par.
    Devuelve True si es par, de lo contrario False.
    """
    return numero % 2 == 0

# Uso:
print(es_par(4))  # Devuelve True
print(es_par(7))  # Devuelve False


# Ejemplo 3: Función que calcula el factorial de un número
def factorial(n):
    """
    Calcula el factorial de un número entero positivo n.
    El factorial de n (n!) es el producto de todos los enteros desde 1 hasta n.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Uso:
print(factorial(5))  # Devuelve 120 (5 * 4 * 3 * 2 * 1)


# Ejemplo 4: Función con argumentos por defecto
def saludar(nombre="Mundo"):
    """
    Esta función saluda al nombre proporcionado.
    Si no se proporciona un nombre, saluda a 'Mundo'.
    """
    return f"Hola, {nombre}!"

# Uso:
print(saludar())  # Devuelve "Hola, Mundo!"
print(saludar("Luis"))  # Devuelve "Hola, Luis!"


# Ejemplo 5: Función que encuentra el mayor de una lista
def encontrar_mayor(lista):
    """
    Encuentra y devuelve el número más grande en una lista.
    """
    if not lista:  # Verifica si la lista está vacía
        return None
    return max(lista)

# Uso:
numeros = [3, 7, 2, 8, 5]
print(encontrar_mayor(numeros))  # Devuelve 8