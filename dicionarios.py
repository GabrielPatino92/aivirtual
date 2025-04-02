# Un diccionario es como una caja mágica donde guardamos cosas usando etiquetas.
# Cada etiqueta tiene algo guardado, como un juguete o un dulce.

# Ejemplo 1: Diccionario simple
mi_diccionario = {
    "manzana": "fruta roja y dulce",
    "plátano": "fruta amarilla y larga",
    "zanahoria": "verdura naranja y crujiente"
}
# Aquí, "manzana", "plátano" y "zanahoria" son las etiquetas.
# Lo que está después de los dos puntos (:) es lo que guardamos.

print(mi_diccionario["manzana"])  # Esto muestra: fruta roja y dulce

# Ejemplo 2: Cambiar algo en el diccionario
mi_diccionario["manzana"] = "fruta roja, dulce y jugosa"
print(mi_diccionario["manzana"])  # Ahora muestra: fruta roja, dulce y jugosa

# Ejemplo 3: Agregar algo nuevo
mi_diccionario["uva"] = "fruta pequeña y morada"
print(mi_diccionario)  # Ahora el diccionario tiene una nueva etiqueta: "uva"

# Ejemplo 4: Eliminar algo
del mi_diccionario["zanahoria"]
print(mi_diccionario)  # Ahora "zanahoria" ya no está en la caja mágica

# Ejemplo 5: Recorrer el diccionario
for etiqueta, valor in mi_diccionario.items():
    print(f"La etiqueta es '{etiqueta}' y guarda '{valor}'")
# Esto muestra todas las etiquetas y lo que tienen guardado.

# ¡Y eso es todo! Los diccionarios son muy útiles para organizar cosas.