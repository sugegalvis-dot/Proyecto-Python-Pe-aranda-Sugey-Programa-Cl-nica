#módulo
import json

ruta = r"C:\Users\juand\OneDrive\Desktop\Proyecto_Python_PeñarandaSugey\datos.json"

def cargar_datos():
    with open (ruta, "r", encoding="utf-8") as arch:
        datos = json.load(arch)
        return datos

def guardar_datos(datos):
    with open ( ruta, "w", encoding="utf-8") as arch:
        json.dump(datos, arch, indent=4, ensure_ascii=False)

def guardar_prescripcion(consulta):
    nombre = "prescripcion_" + consulta["paciente"] + consulta["fecha"] + ".json"

    with open (nombre, "w", encoding="utf-8") as arch:
        json.dump(consulta, arch, indent=4, ensure_ascii=False) #Crea el archivo json para la prescripción
    return nombre
