"""
edad = int(input("introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
    print("Eres un adulto")
    print("puedes ver peliculas para adultos")
    print("puedes votar")
    print("puedes conducir")
    print("puedes beber alcohol")
    print("puedes fumar")
    print("puedes tener relaciones sexuales")
    print("puedes casarte")
else:
    print("Eres menor de edad")
    print("Eres un niño")
    print("puedes ver peliculas para niños")
    print("no puedes votar")
    print("no puedes conducir")
print("Fin del programa")"""


"""edad = int(input("introduce tu edad: "))
if edad >= 0 and edad < 6:
    print("Primera infancia")
elif edad >= 6 and edad < 12:
    print("Infancia")
elif edad >= 12 and edad < 18:
    print("Adolescentes")
elif edad >= 18 and edad < 26:
    print("Adultos jóvenes")
elif edad >= 26 and edad < 60:
    print("Adultos")
elif edad >= 60 and edad < 120:
    print("Adultos mayores")
else:
    print("Edad incorrecta")"""
    
dias = int(input("indroduce el nombre del dia de la semana: "))
if dias == 1:
    print("Lunes")
elif dias == 2:
    print("Martes")
elif dias == 3:
    print("Miercoles")
elif dias == 4:
    print("Jueves")
elif dias == 5:
    print("Viernes")
elif dias == 6:
    print("Sabado")
elif dias == 7:
    print("Domingo")
else: 
    print("Valor fuera de rango")