# Ejemplo 1: Contar hasta 5
# Imagina que tienes que contar del 1 al 5 usando un bucle.

contador = 1  # Empezamos con el número 1

while contador <= 5:  # Mientras el número sea menor o igual a 5
    print(contador)  # Mostramos el número
    contador += 1  # Sumamos 1 al número para pasar al siguiente

# Ejemplo 2: Pedir una contraseña
# Aquí pedimos al usuario que escriba una contraseña correcta.

contraseña = ""  # Empezamos con una contraseña vacía

while contraseña != "secreto":  # Mientras la contraseña no sea "secreto"
    contraseña = input("Escribe la contraseña: ")  # Pedimos al usuario que escriba

print("¡Contraseña correcta!")

# Ejemplo 3: Salir cuando el usuario escriba "salir"
# Aquí seguimos pidiendo palabras hasta que el usuario escriba "salir".

palabra = ""  # Empezamos con una palabra vacía

while palabra != "salir":  # Mientras la palabra no sea "salir"
    palabra = input("Escribe algo (o escribe 'salir' para terminar): ")  # Pedimos al usuario que escriba
    print(f"Escribiste: {palabra}")  # Mostramos lo que escribió

print("¡Adiós!")
# Ejemplo 4: Realizar operaciones matemáticas hasta que el usuario decida salir
while True:
    print("\nOperaciones disponibles:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "5":
        print("¡Hasta luego!")
        break
    
    if opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            
            if opcion == "1":
                print(f"Resultado: {num1 + num2}")
            elif opcion == "2":
                print(f"Resultado: {num1 - num2}")
            elif opcion == "3":
                print(f"Resultado: {num1 * num2}")
            elif opcion == "4":
                if num2 != 0:
                    print(f"Resultado: {num1 / num2}")
                else:
                    print("Error: No se puede dividir entre cero.")
        except ValueError:
            print("Error: Por favor, introduce números válidos.")
    else:
        print("Opción no válida. Intenta de nuevo.")