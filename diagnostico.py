#Módulo -> diagnostico pacientes
from almacenamiento import cargar_datos, guardar_datos, guardar_prescripcion
from pacientes import buscar_paciente

#funcion que se encarga de pedir numero en cantidad y días
def pedir_numero(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.isdigit():
            return int(texto)
        print ("Digite solo numeros")

def diagnosticar_paciente(medico):
    datos = cargar_datos()

    print ("\n ----- DIAGNOSTICAR PACIENTE ----")

    identificacion = input("Identificación del paciente: ").strip()
    paciente = buscar_paciente(datos, identificacion)

    if paciente == None:
        print("El paciente no está registrado. Realice el registro.")
        return
    print ("Paciente: ", paciente["nombres"], paciente["apellidos"])


    fecha_valida = False
    while fecha_valida == False:

        fecha = input ("Fecha de la consulta (AAAA-MM-DD): ").strip()
        if len(fecha) == 10 and fecha [4] == "-" and fecha [7] == "-" and fecha.replace("-", "").isdigit():
            fecha_valida= True
        else:
            print ("Formato no válido. Ejemplo: 2026-22-13")

    sintomas = [] #1. Agrego sintomas a la lista
    print("Escriba los sintomas uno por uno. Escriba '/' fin '/' para terminar.")

    while True:
        sintoma = input("Sintoma: ").strip()
        if sintoma.lower() == "fin":
            break
        if sintoma:
            sintomas.append(sintoma)

    #2. diagnostico
    diagnostico = input("Diagnostico (Enfermedad o patología): ").strip()

    #PREESCRIPCIÓN MEDICA
    medicamentos = []
    print ("Registre los medicamentos. Deje el nombre vacío para terminar.")
    while True:
        nombre_medi = input ("Medicamento: ").strip()
        if nombre_medi == "":
            break
        cantidad = pedir_numero("cantidad: ")
        dosis = input ("Dosis (cuanto debe tomar al día): ").strip()
        dias = pedir_numero("Tiempo de aplicación del medicamento (días): ")

        medicamento = {
            "medicamento": nombre_medi,
            "cantidad": cantidad,
            "dosis": dosis,
            "dias": dias 
        }
        medicamentos.append(medicamento)

    consulta = {
        "fecha": fecha,
        "paciente": paciente["identificacion"],
        "nombre_medico": medico["nombres"] + " " + medico ["apellidos"],
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "medicamentos": medicamentos
    }

#se guarda en datos json para cada historia de la clinica

    datos["consultas"].append(consulta)
    guardar_datos(datos)

    #genera json -> De LA PREESCRIPCIÓN
    nombre_archivo = guardar_prescripcion(consulta)
    print ("Diagnóstico gauardado.")
    print ("prescripción generada en:", nombre_archivo)

