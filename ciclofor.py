# Ejemplo 1: Imprimir números del 1 al 5
# Este ciclo for recorre un rango de números desde 1 hasta 5 (el límite superior no se incluye).
for i in range(1, 6):
    print(i)  # Imprime el valor actual de i en cada iteración.

# Ejemplo 2: Iterar sobre una lista
# Aquí usamos un ciclo for para recorrer una lista de frutas y mostrar cada elemento.
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)  # Imprime cada fruta de la lista.

# Ejemplo 3: Usar for con la función enumerate
# La función enumerate nos da el índice y el valor de cada elemento en una lista.
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"Índice: {indice}, Color: {color}")

# Ejemplo 4: Anidar ciclos for
# Este ejemplo muestra cómo usar ciclos for anidados para generar combinaciones.
for i in range(1, 4):  # Ciclo externo
    for j in range(1, 4):  # Ciclo interno
        print(f"Combinación: ({i}, {j})")

# Ejemplo 5: Usar for con una condición
# Este ciclo for imprime solo los números pares de una lista.
numeros = [1, 2, 3, 4, 5, 6]
for numero in numeros:
    if numero % 2 == 0:  # Verifica si el número es par.
        print(numero)

# Ejemplo 6: Romper un ciclo con break
# Este ciclo se detiene cuando encuentra el número 3.
for i in range(1, 6):
    if i == 3:
        break  # Sale del ciclo cuando i es igual a 3.
    print(i)

# Ejemplo 7: Saltar una iteración con continue
# Este ciclo omite el número 3 y continúa con las siguientes iteraciones.
for i in range(1, 6):
    if i == 3:
        continue  # Salta el resto del código en esta iteración.
    print(i)
    
    