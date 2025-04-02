# Las tuplas son como cajas donde guardamos cosas, pero no podemos cambiar lo que hay dentro.
# Son como una lista, pero no se pueden modificar.

# Ejemplo 1: Crear una tupla
mi_tupla = (1, 2, 3)
print("Mi tupla:", mi_tupla)  # Esto muestra: Mi tupla: (1, 2, 3)

# Ejemplo 2: Acceder a un elemento de la tupla
# Imagina que los números en la tupla son juguetes en una caja.
# Puedes sacar un juguete diciendo su posición.
primer_elemento = mi_tupla[0]  # El primer juguete está en la posición 0
print("Primer elemento:", primer_elemento)  # Esto muestra: Primer elemento: 1

# Ejemplo 3: Las tuplas no se pueden cambiar
# Si intentas cambiar algo, Python no te dejará.
# mi_tupla[0] = 10  # Esto daría un error porque las tuplas no se pueden modificar.

# Ejemplo 4: Tuplas con diferentes tipos de datos
# Puedes guardar diferentes tipos de cosas en una tupla.
mi_tupla_diferente = ("manzana", 3, True)
print("Tupla con diferentes tipos:", mi_tupla_diferente)
# Esto muestra: Tupla con diferentes tipos: ('manzana', 3, True)

# Ejemplo 5: Desempaquetar una tupla
# Puedes sacar todo lo que hay en la tupla de una vez.
a, b, c = mi_tupla
print("a:", a, "b:", b, "c:", c)  # Esto muestra: a: 1 b: 2 c: 3

# Ejemplo 6: Usar tuplas para cosas que no cambian
# Las tuplas son útiles para cosas que no deberían cambiar, como coordenadas.
coordenadas = (10, 20)
print("Coordenadas:", coordenadas)  # Esto muestra: Coordenadas: (10, 20)

# Recuerda: Las tuplas son como cajas mágicas que no puedes cambiar, pero puedes mirar dentro.