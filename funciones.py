# Calcular el promedio de 5 notas
def promedio_de_notas(Numero_de_notas):
    
    print("Introduzca el numero de notas que quiere calificar")

    Numero_de_notas = int(input())
    suma_de_notas = 0

    for i in range(Numero_de_notas):
        nota = float(input(f"Introduce la calificacion #{i+1}: "))
        suma_de_notas += nota

    promedio = suma_de_notas / Numero_de_notas

    return print(f"De un total de {Numero_de_notas} notas, el promedio es: {promedio:.2f}")