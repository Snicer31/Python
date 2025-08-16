#Los condicionales sirven para manejar flujos de datos booleanos


print("Ingrese las calificaciones")
#Entrada de informmacion pero, la funcion input crea un dato de tipo string

nota = input()
#El dato strin es cambiado a flotante
nota = float(nota)

if nota >= 5:
    print("Pasaste la materia con ")
    print(nota)
else:
    print("Raspaste la materia con ")
    print(nota)

