#Metodo para ver si son las mismas contrasnias
def VerificacionContraseña(Original,Contrasenia):
    if Original == Contrasenia :
        print("La contraseña es correcta\n")
    else :
        print("Las contraseñas no coinciden\n")

def Grupo (Nombre,Genero):
    if Genero == 1:
        if Nombre.lower() <"m":
            Grupo = "A"
        else :
            Grupo = "B"
    else :
        if Nombre.lower() > "n":
            Grupo = "A"
        else :
            Grupo = "B"
    print("Pertenece al grupo "+ Grupo+"\n")

print("\n------------------Bienvenido------------------")

Seguir = True

while Seguir ==True:

    print("Puedes ingresar el numero del ejercicio que deseas realizar")
    print("1.Verificacion contraseña.\n2.Grupos.\n3Terminar.")
    Opcion = int (input(">"))

    while Opcion>4 or 1>Opcion:
        print("Digita un numero dentro de las opciones mostradas")
        print("1.Asteriscos.\n2.Cuenta regresiva.\n3.Verificacion de numero primo.")
        Opcion = int (input(">"))



    if Opcion == 1:
        print("Ingresa un contraseña")
        Original =  (input(">"))
        print("")
        print("Ingresa nuevamente la contraseña")
        Contrasenia =  (input(">"))
        VerificacionContraseña(Original,Contrasenia)

    elif Opcion == 2:
        print("Ingresa un nombre")
        Nombre =  (input(">"))
        print("Digita 0 si eres hombre, o digita 1 si eres mujer :")
        Genero  =  int (input(">"))
        Grupo(Nombre,Genero)

    elif Opcion == 3:
        Seguir = False  
        print ("------ Fin ------") 


#Fin 