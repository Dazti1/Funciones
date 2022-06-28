import os
import numpy as  np
import Funciones_pyme as fp

# ---------- VARIABLES ----------
opcion_menu=""
tamaño=5
nombres=np.empty(tamaño, dtype=object)
valor_hora=np.empty(tamaño, dtype=int)
horas_trabajadas=np.empty(tamaño, dtype=float)
sueldos_recibidos=np.empty(tamaño, dtype=int)
horas=0
menor_sueldo=0
# ---------- CODIGO PRINCIPAL ----------
while True:
    os.system("cls")
    print("\n---------- Menú Principal ----------")
    opcion_menu=str(input("""
1.- Registrar empleados
2.- Empleados con mas de 100 horas trabajadas
3.- Promedio de sueldos a pagar
4.- Empleado con menor sueldo
5.- Salir\n"""))
    if opcion_menu=="1":
        os.system("cls")
        print("---------- Registrar Empleados ----------")
        for k in range(tamaño):
            os.system("cls")
            nombres[k]=str(input("Ingrese nombre del colaborador: ")).strip().capitalize()
            valor_hora[k]=int(input("Ingrese valor hora del colaborador: "))
            while not valor_hora[k]>=0:
                print("ERROR... Valor hora no válido.")
                valor_hora[k]=int(input("Ingrese valor hora del colaborador: "))
            horas_trabajadas[k]=int(input("Ingrese horas trabajadas por el colaborador: "))
            while not horas_trabajadas[k]>=0:
                print("ERROR... Horas trabajadas no válidas.")
                horas_trabajadas[k]=int(input("Ingrese horas trabajadas por el colaborador: "))
            sueldos_recibidos[k]=fp.calcular_sueldo(valor_hora[k],horas_trabajadas[k])
            fp.imprimir_estadisticas(nombres[k],valor_hora[k],horas_trabajadas[k],sueldos_recibidos[k])
            os.system("pause")
    elif opcion_menu=="2":
        os.system("cls")
        print("---------- +100 horas trabajadas ----------")
        for k in range(tamaño):
            horas=horas_trabajadas[k]
            if horas>100:
                fp.imprimir_estadisticas(nombres[k],valor_hora[k],horas_trabajadas[k],sueldos_recibidos[k])
        os.system("pause")
    elif opcion_menu=="3":
        os.system("cls")
        print("---------- Promedio de sueldo a pagar ----------")
        print(sueldos_recibidos.mean())
        os.system("pause")
    elif opcion_menu=="4":
        os.system("cls")
        menor_sueldo=np.where(sueldos_recibidos == np.min(sueldos_recibidos))
        fp.imprimir_estadisticas(nombres[menor_sueldo],valor_hora[menor_sueldo],horas_trabajadas[menor_sueldo],sueldos_recibidos[menor_sueldo])
        os.system("pause")
    elif opcion_menu=="5":
        break
