# Simulador de Gestión de Tránsito Urbano
import time
import random

class ControladorSemaforico:
    """Controla el estado de los semáforos en una intersección"""
    
    def __init__(self, identificador):
        self.identificador = identificador
        self.estado_actual = "rojo"
        self.duracion_verde = 6
        self.duracion_amarillo = 3
        self.duracion_rojo = 5
        self.contador_ciclos = 0
    
    def alternar_estado(self):
        """Alterna el estado del semáforo al siguiente"""
        self.contador_ciclos += 1
        
        if self.estado_actual == "rojo":
            self.estado_actual = "verde"
            return self.duracion_verde
        elif self.estado_actual == "verde":
            self.estado_actual = "amarillo"
            return self.duracion_amarillo
        else:
            self.estado_actual = "rojo"
            return self.duracion_rojo
    
    def obtener_estado(self):
        """Devuelve la representación visual del estado"""
        colores = {
            "verde": "🟢 VERDE",
            "amarillo": "🟡 AMARILLO", 
            "rojo": "🔴 ROJO"
        }
        return f"Semáforo #{self.identificador}: {colores[self.estado_actual]}"
    
    def __str__(self):
        return self.obtener_estado()

class Vehiculo:
    """Representa un vehículo en el sistema de tránsito"""
    
    def __init__(self, placa):
        self.placa = placa
        self.velocidad = random.randint(45, 85)
        self.en_marcha = False
        self.cruzo_amarillo = False
        self.tipo = random.choice(["auto", "camion", "moto"])
    
    def evaluar_movimiento(self, controlador):
        """Evalúa si el vehículo debe moverse según el semáforo"""
        if controlador.estado_actual == "verde":
            self.en_marcha = True
            self.cruzo_amarillo = False
        elif controlador.estado_actual == "amarillo":
            # Vehículos rápidos o motos tienden a cruzar en amarillo
            if self.velocidad > 70 or self.tipo == "moto":
                self.en_marcha = True
                self.cruzo_amarillo = True
            else:
                self.en_marcha = False
                self.cruzo_amarillo = False
        else:  # rojo
            self.en_marcha = False
            self.cruzo_amarillo = False
    
    def obtener_info(self):
        """Devuelve información del vehículo"""
        estado = "🚗 EN MOVIMIENTO" if self.en_marcha else "🚦 DETENIDO"
        mensaje = f"{self.tipo.upper()} {self.placa}: {estado} ({self.velocidad} km/h)"
        
        if self.cruzo_amarillo:
            mensaje += " ⚠️  CRUZÓ EN AMARILLO!"
        
        return mensaje

def ejecutar_simulacion():
    """Ejecuta la simulación principal del sistema de tránsito"""
    print("🚦 SISTEMA DE SIMULACIÓN DE TRÁNSITO URBANO")
    print("=" * 50)
    print("⚠️  Vehículos >70 km/h o motos pueden cruzar en amarillo")
    print("=" * 50)
    
    # Configurar sistema
    semaforo_central = ControladorSemaforico(1)
    vehiculos = [Vehiculo(f"ABC-{i:03d}") for i in range(1, 8)]  # 7 vehículos
    
    # Mostrar configuración inicial
    print("\n📊 CONFIGURACIÓN INICIAL DE VEHÍCULOS:")
    for vehiculo in vehiculos:
        print(f"   {vehiculo.tipo.title()} {vehiculo.placa}: {vehiculo.velocidad} km/h")
    
    # Ejecutar 8 ciclos de semáforo
    for ciclo in range(1, 9):
        print(f"\n{' CICLO ' + str(ciclo) + ' ':=^40}")
        
        # Cambiar estado del semáforo
        tiempo_estado = semaforo_central.alternar_estado()
        print(f"{semaforo_central} (Duración: {tiempo_estado}s)")
        print("-" * 40)
        
        # Actualizar estado de vehículos
        for vehiculo in vehiculos:
            vehiculo.evaluar_movimiento(semaforo_central)
            print(vehiculo.obtener_info())
        
        # Pequeña pausa para visualización
        time.sleep(0.5)
    
    # Resumen final
    print(f"\n{' RESUMEN FINAL ':=^40}")
    for vehiculo in vehiculos:
        comportamiento = "AGRESIVO" if vehiculo.cruzo_amarillo else "PRUDENTE"
        print(f"{vehiculo.tipo.title()} {vehiculo.placa}: {comportamiento}")

def interfaz_principal():
    """Interfaz de usuario principal"""
    while True:
        print("\n" + "🔷" * 25)
        print("       SISTEMA DE SIMULACIÓN DE TRÁNSITO")
        print("🔷" * 25)
        print("1. Iniciar nueva simulación")
        print("2. Finalizar programa")
        print("-" * 45)
        
        opcion = input("Seleccione una opción (1-2): ").strip()
        
        if opcion == "1":
            ejecutar_simulacion()
        elif opcion == "2":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida")

# Punto de ejecución
if __name__ == "__main__":
    interfaz_principal()