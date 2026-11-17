# =====================================================================
# CURSO: Fundamentos de Programación (Código: 213022)
# FASE 5: Evaluación Final POA - Problema 1
# DESCRIPCIÓN: Evaluación del nivel de compromiso de sesiones digitales
#              mediante el uso de matrices y funciones.
# AUTOR: JAIDER FERNANDO MENDOZA CAMPOS
# =====================================================================

def clasificar_compromiso(duracion, clics):
    """
    Función que calcula la clasificación de compromiso de una sesión
    a partir de su duración (segundos) y número de clics.
    Lógica de negocio:
    - Alto: Duración > 180 y Clics > 8
    - Bajo: Duración < 60 u Clics < 3
    - Medio: Cualquier otro caso
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

def generar_informe(matriz_sesiones):
    """
    Función que recorre la matriz de sesiones, evalúa el compromiso
    de cada cliente e imprime el informe en consola.
    """
    print("\n==================================================")
    print("      INFORME DE COMPROMISO DE LOS CLIENTES       ")
    print("==================================================")
    print(f"{'ID Cliente':<15}{'Clasificación Final':<20}")
    print("--------------------------------------------------")
    
    # Recorrido de la matriz fila por fila
    for fila in matriz_sesiones:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]
        
        # Llamado a la función de lógica de negocio
        clasificacion = clasificar_compromiso(duracion, clics)
        
        # Formateo de salida para que se alinee estéticamente
        print(f"{id_cliente:<15}{clasificacion:<20}")
    print("==================================================\n")

def main():
    """
    Módulo principal que inicializa los datos y ejecuta el programa.
    """
    # Matriz inicial con 5 sesiones (Formato: [ID, Duración en seg, Clics])
    # Se incluyen ejemplos que disparan los tres tipos de clasificación
    sesiones = [
        ["CLI-001", 181, 10],  # Cumple Alto (>180 y >8)
        ["CLI-002", 45, 5],    # Cumple Bajo (<60 o <3 por duración)
        ["CLI-003", 120, 5],   # Cae en Medio (No cumple Alto ni Bajo)
        ["CLI-004", 190, 2],    # Cumple Bajo (<60 o <3 por clics)
        ["CLI-005", 250, 12]   # Cumple Alto (>180 y >8)
    ]
    
    # Ejecución del módulo encargado de mostrar los resultados
    generar_informe(sesiones)

# Punto de entrada estándar en Python para ejecutar el programa
if __name__ == "__main__":
    main()
