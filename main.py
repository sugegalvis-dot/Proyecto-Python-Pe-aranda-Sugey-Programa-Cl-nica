#Archivo Main (maestro)-> Principal -ACME CLINIC
#1.1. print usuario y entrada al registro de usuarios.
from login import iniciar_sesion
from usuarios import registrar_usuario
from pacientes import registrar_paciente
from diagnostico import diagnosticar_paciente
from historia import mostrar_historia

print ("=== ACME CLINIC - GESTOR DE DIAGNÓSTICO CLÍNICO ===")

usuario = iniciar_sesion()

if usuario != None: 
    print ("Rol:", usuario["rol"])

    while True:
        print ("\n ----- MENÚ PRINCIPAL -----")
        print ("1. Registrar usuario")
        print ("2. Registrar paciente")
        print ("3. Diagnosticar paciente")
        print ("4. Mostrar historia")
        print ("5. Salir")
        opcion = input("Elija una opcion: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            registrar_paciente()
        elif opcion == "3":
            if usuario["rol"] == "medico":
                diagnosticar_paciente(usuario)
            else:
                print ("Solo los médicos pueden diagnosticar pacientes.")
        elif opcion == "4":
            mostrar_historia()
        elif opcion == "5":
            print ("Hasta luego, ", usuario["nombres"])
            break
        else: 
            print ("Opcion no valida.")
