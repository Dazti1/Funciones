import funciones_empleado as fe 
import numpy as np
import os

#----------- VARIABLES -----------
opcion_menu=""
tamaño=3
ruts=np.empty(tamaño, dtype=object)
nombres=np.empty(tamaño, dtype=object)
sueldos_brutos=np.empty(tamaño, dtype=int)
sueldos_liquidos=np.empty(tamaño, dtype=float)
#----------- CODIGO PRINCIPAL -----------
while True:
    os.system("cls")
    opcion_menu=str(input("""
----------- MENU PRINCIPAL -----------
1.- Cargar Datos y ver liquidación
2.- Ver estadisticas
3.- Salir
"""))
    if opcion_menu=="1":
        os.system("cls")
        print("\n----- CARGAR DATOS -----")
        for k in range(tamaño):
            ruts[k]=str(input("Ingrese rut: ")).strip()
            while not len(ruts[k])>0:
                print("¡ERROR! no campo vacío")
                ruts[k]=str(input("Ingrese rut: ")).strip()
            nombres[k]=str(input("Ingrese nombre: ")).strip().capitalize()
            while not len(nombres[k])>0:
                print("¡ERROR! no campo vacío")
                nombres[k]=str(input("Ingrese nombre: ")).strip().capitalize()
            sueldos_brutos[k]=int(input("Ingrese sueldo bruto: "))
            while not sueldos_brutos[k]>=0:
                print("¡ERROR! no menor de 0")
                sueldos_brutos[k]=str(input("Ingrese sueldo bruto: "))
            # ahora envianos los parámetros a nuestras funciones
            # las cuales nos van a retornar 3 datos
            salud,pension,liquido=fe.calcular_descuentos_legales(sueldos_brutos[k])
            
            sueldos_liquidos[k]=liquido
            
            fe.imprimir_liquidacion(ruts[k], nombres[k],sueldos_brutos[k],salud,pension,sueldos_liquidos[k])
            
        os.system("pause")
    elif opcion_menu=="2":
        os.system("cls")
        fe.maximo(ruts,nombres,sueldos_liquidos)
        os.system("pause")
    elif opcion_menu=="3":
        break
