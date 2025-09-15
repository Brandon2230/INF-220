# Sistema de Gestión de Pendientes con Persistencia
import csv
import os
from datetime import datetime

ARCHIVO_TAREAS = 'pendientes.csv'

def cargar_pendientes():
    """Carga los pendientes desde archivo CSV"""
    pendientes = []
    try:
        with open(ARCHIVO_TAREAS, 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            next(lector, None)  # Saltar encabezados
            for fila in lector:
                if len(fila) >= 3:
                    pendientes.append({
                        'descripcion': fila[0],
                        'fecha_creacion': fila[1],
                        'estado': fila[2]
                    })
    except FileNotFoundError:
        pass
    return pendientes

def guardar_pendientes(pendientes):
    """Guarda los pendientes en archivo CSV"""
    with open(ARCHIVO_TAREAS, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Descripción', 'Fecha Creación', 'Estado'])
        for tarea in pendientes:
            escritor.writerow([
                tarea['descripcion'],
                tarea['fecha_creacion'],
                tarea['estado']
            ])

def añadir_pendiente():
    """Añade un nuevo pendiente a la lista"""
    descripcion = input("Ingrese el pendiente: ").strip()
    if not descripcion:
        print("❌ La descripción no puede estar vacía")
        return
    
    pendientes = cargar_pendientes()
    nuevo_pendiente = {
        'descripcion': descripcion,
        'fecha_creacion': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'estado': 'Pendiente'
    }
    pendientes.append(nuevo_pendiente)
    guardar_pendientes(pendientes)
    print(f"✅ Pendiente añadido: {descripcion}")

def mostrar_pendientes():
    """Muestra todos los pendientes con formato"""
    pendientes = cargar_pendientes()
    
    print(f"\n📋 LISTA DE PENDIENTES ({len(pendientes)})")
    print("═" * 50)
    
    if not pendientes:
        print("   No hay pendientes registrados")
        return
    
    for i, tarea in enumerate(pendientes, 1):
        print(f"{i:2d}. {tarea['descripcion']}")
        print(f"    📅 {tarea['fecha_creacion']} | 🎯 {tarea['estado']}")
        print("─" * 40)

def eliminar_archivo_datos():
    """Elimina el archivo de datos si existe"""
    if os.path.exists(ARCHIVO_TAREAS):
        confirmacion = input("¿Está seguro de eliminar todos los datos? (s/n): ").lower()
        if confirmacion == 's':
            os.remove(ARCHIVO_TAREAS)
            print("🗑️ Archivo de datos eliminado exitosamente")
        else:
            print("❌ Operación cancelada")
    else:
        print("ℹ️ No existe archivo de datos para eliminar")

def interfaz_principal():
    """Interfaz principal del sistema"""
    while True:
        print("\n" + "✦" * 40)
        print("       SISTEMA DE GESTIÓN DE PENDIENTES")
        print("✦" * 40)
        print("1. Añadir nuevo pendiente")
        print("2. Ver lista de pendientes")
        print("3. Limpiar archivo de datos")
        print("4. Salir del sistema")
        print("─" * 40)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            añadir_pendiente()
        elif opcion == "2":
            mostrar_pendientes()
        elif opcion == "3":
            eliminar_archivo_datos()
        elif opcion == "4":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")

# Punto de ejecución
if __name__ == "__main__":
    interfaz_principal()