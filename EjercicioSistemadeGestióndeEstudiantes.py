# Programa de Gestión de Estudiantes

# Lista para guardar los estudiantes
estudiantes = []

# Función para agregar un nuevo estudiante
def agregar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    calificaciones = list(map(float, input("Ingresa las calificaciones separadas por espacio: ").split()))
    estudiantes.append({"nombre": nombre, "edad": edad, "calificaciones": calificaciones})
    print(f"Estudiante {nombre} agregado con éxito.\n")

# Función para calcular el promedio de calificaciones
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Función para mostrar estudiantes con promedio mayor a un valor dado
def mostrar_estudiantes_con_promedio_mayor():
    valor = float(input("Ingresa el valor del promedio: "))
    print(f"Estudiantes con promedio mayor a {valor}:")
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["calificaciones"])
        if promedio > valor:
            print(f"- {estudiante['nombre']} (Promedio: {promedio:.2f})")
    print()

# Función para buscar estudiantes por nombre
def buscar_estudiante():
    nombre = input("Ingresa el nombre del estudiante a buscar: ")
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            print(f"Estudiante encontrado: {estudiante}")
            return
    print("Estudiante no encontrado.\n")

# Menú principal
def menu():
    while True:
        print("1. Agregar estudiante")
        print("2. Mostrar promedio de calificaciones")
        print("3. Mostrar estudiantes con promedio mayor a un valor")
        print("4. Buscar estudiante por nombre")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            for estudiante in estudiantes:
                promedio = calcular_promedio(estudiante["calificaciones"])
                print(f"{estudiante['nombre']} tiene un promedio de {promedio:.2f}")
            print()
        elif opcion == "3":
            mostrar_estudiantes_con_promedio_mayor()
        elif opcion == "4":
            buscar_estudiante()
        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

# Iniciar el programa
menu()

