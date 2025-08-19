#Entrada de seguridad

contraseña = "tuGato"
intentos = 0

while intentos <= 4: 

    contraseña_Ingresada =input("Ingrese la contraseña:")

    if contraseña == contraseña_Ingresada:
        
        print("Acceso concedido")
        break

    else:
        print("Acceso denegado")
        print("Numero de intentos restantes")
        intentos += 1
        print(5-intentos)
    if intentos == 4:
        print("Login anulado")
        


