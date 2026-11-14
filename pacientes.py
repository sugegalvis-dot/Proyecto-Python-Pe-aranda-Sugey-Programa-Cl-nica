# Módulo que registra y busca pacientes
from almacenamiento import guardar_datos, cargar_datos


def buscar_paciente(datos, identificacion):
    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            return paciente
    return None

def registrar_paciente():
    datos = cargar_datos()

    print ("\n ---- REGISTRO DE PACIENTES ----")

    #Pedir la identificaciónpara que no esté repetida

    existe = True
    while existe:
        identificacion = input("Número de identificación: ").strip()

        if buscar_paciente(datos, identificacion) != None:
            print("Ya existe un paciente con esa identificación. Intenta de nuevo")
        else:
            existe = False

    nombres = input ("Nombres: ").strip()
    while nombres == "":
        print ("El nombre es obligatorio.")        
        nombres = input("Nombres: ").strip()
    
    apellidos = input ("apellidos: ").strip()
    while apellidos == "":
            print ("El apellido es obligatorio")  
            apellidos = input("Apellidos: ").strip()

    while True:
        telefono = input ("Teléfono: ").strip()
        if telefono.replace(" ", "").isdigit():
            break
        else: print ("Escribe solo números.")

    while True:
        email = input ("E-mail: ").strip()
        if "@" in email and "." in email:
            break
        else:
            print ("El correo debe incluir @ y un punto.")

    direccion = input ("Direccion: ").strip()
    genero = input ("Género: ").strip()
    estado_civil = input ("Estado civil: ").strip()

    nuevo = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil
    }

    datos["pacientes"].append(nuevo)
    guardar_datos(datos)
    print("Paciente registrado correctamente.")
