# Ejercicio sobre cine

print("Seleccione la película a ver (coloque un número del 1 al 4 por favor):")
print("1. Mision imposible (PG-13)")
print("2. Jurassic World (G)")
print("3. Al filo del mañana (PG-13)")
print("4. Terminator (R)")

tipo_de_pelicula = int(input())

print("Ingresa tu edad:")
edad = int(input())

print("¿Vienes con tus padres? (si/no):")
representante = input().strip().lower()  # Convertir a minúsculas y quitar espacios

# Verificar si viene con representante
representante = representante == 'si'  # Esto devolverá True o False

"""
Clasificaciones:
G (General): Apta para todos los públicos.
PG-13: Mayores de 13 o menores con padres.
R: Mayores de 17 o menores con padres.
"""

# Película tipo PG-13 (Misión imposible)
if tipo_de_pelicula == 1:
    if edad >= 13 or (edad < 13 and representante):
        print("Puedes ver la película")
    else:
        print("No puedes ver la película sin supervisión de tus tutores")

# Película tipo G (Jurassic World)
elif tipo_de_pelicula == 2:
    print("Puedes ver la película (apta para todos los públicos)")

# Película tipo PG-13 (Al filo del mañana)
elif tipo_de_pelicula == 3:
    if edad >= 13 or (edad < 13 and representante):
        print("Puedes ver la película")
    else:
        print("No puedes pasar sin tus tutores")

# Película tipo R (Terminator)
elif tipo_de_pelicula == 4:
    if edad >= 17 or (edad < 17 and representante):
        print("Puedes pasar a ver la película")
    else:
        print("No puedes ver esta película sin tus padres")

else:
    print("Selección de película no válida")