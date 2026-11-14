#Módulo-> registro de usuarios (Médico y administrativos)
#1.*Queremos cargar los datos y guardar los registros de datos*

from almacenamiento import cargar_datos, guardar_datos

def registrar_usuario():
    datos = cargar_datos()

    print("\n ----REGISTRO DE USUARIOS----")


    existe = True
    while existe:     #para ver si la identificacion ya existe -> si es así intenta de nuevo, sino rompe el ciclo porque no existe= False
        identificacion = input("Numero de identificacion: ").strip()

        existe = False
        for usuario in datos["usuarios"]:
            if usuario ["identificacion"] == identificacion:
                existe = True
                break
        if existe:
            print("Ya existe un usuario con esa identificacion. Intenta de nuevo")
    #Si los espacios están vaciós, ingrese la informacion
    
    nombres = input("Nombres: ").strip()
    while nombres == "":
        print ("El nombre es obligatorio.")        
        nombres = input("Nombres: ").strip()

    apellidos = input("Apellidos: ").strip()
    while apellidos == "":
        print ("El apellido es obligatorio")  
        apellidos = input("Apellidos: ").strip()

    while True: #Solo deja ingresar numeros y puede ingresar espacios
        telefono = input("Teléfono: ").strip()
        if telefono.replace(" ", "").isdigit():
            break
        else:
            print("Escribe solo numeros.")

    while True:
        email= input("E-mail corporativo: ").strip()
        if "@" in email and "." in email:
            break
        else: 
            print ("El correo debe incluir @ y un punto.")

    direccion = input("Dirección: ").strip()

# Usuario -> Médico o administrativo
    rol = ""
    while rol != "medico" and rol != "administrativo":
        rol = input ("Ingrese su Rol (medico/administrativo): ").strip().lower()
        if rol == "medico":
            rol = "medico"
        if rol != "medico" and rol != "administrativo":
            print ("Rol no válido. Escriba (medico o administrativo): ")

    contraseña = input ("Contraseña: ").strip()


    
    nuevo = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "e-mail": email,
        "direccion": direccion,
        "rol": rol,
        "contraseña": contraseña
    }
    datos ["usuarios"].append(nuevo)
    guardar_datos(datos)
    print ("Usuario registrado correctamente")


