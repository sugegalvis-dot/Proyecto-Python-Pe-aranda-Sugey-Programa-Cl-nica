#Modulo inicio de sesión (iniciar_sesion) - importa funcion cargar_datos que está en otro archivo
from almacenamiento import cargar_datos

def iniciar_sesion():
    datos = cargar_datos()
    intentos = 3

    while intentos > 0:
        correo = input("Digite su correo: ").strip()
        contraseña = input("Digite contraseña: ").strip()

        for usuario in datos["usuarios"]:
            if usuario["e-mail"].lower() == correo.lower() and usuario["contraseña"] == contraseña:
                print ("Bienvenido,", usuario["nombres"])
                return usuario
        intentos = intentos -1
        print ("Correo o contraseña incorrectos. Intentos restantes: ", intentos)

    print ("Demasiados intentos fallidos.")
    return None
        

