#Módulo de la historia clinica
from almacenamiento import cargar_datos
from pacientes import buscar_paciente

def mostrar_historia():
    datos = cargar_datos()

    print ("\n --- HISTORIA CLÍNICA ---")
    identificacion = input ("Identificación del paciente: ").strip()
    paciente = buscar_paciente(datos, identificacion)

    if paciente == None:
        print ("El paciente no está registrado")
        return

    #encabezado -> datos del paciente
    print ("\n =====================================")
    print ("Identificación:", paciente["identificacion"])
    print ("Nombre:", paciente["nombres"], paciente["apellidos"])
    print ("Teléfono:", paciente["telefono"])
    print("E-mail:", paciente["email"])
    print("Dirección:", paciente["direccion"])
    print("Género:", paciente["genero"])
    print("Estado civil:", paciente["estado_civil"])
    print("==============================")

    #Existencia de consultas del paciente

    exis_consultas = False
    for consulta in datos ["consultas"]:
        if consulta["paciente"] == identificacion:
            exis_consultas = True
            print ("\n Fecha:", consulta["fecha"])
            print("Médico:", consulta["nombre_medico"])
            print("Síntomas:", ", ".join(consulta["sintomas"]))
            print("Diagnóstico:", consulta["diagnostico"])
            print("Medicamentos:")

            for med in consulta["medicamentos"]:
                print (f"-{med["medicamento"]} | cantidad: {med["cantidad"]} | dosis: {med["dosis"]} | días: {med["dias"]}")
            print ("----------------------------------")

        if exis_consultas == False:
            print ("\n El paciente aún no tiene consultas")
