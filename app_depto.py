import os
import numpy as np
import funciones_depto as fd
# ------------------ VARIABLES ------------------
opcion_menu=""
tamaño=40
deptos=np.empty(tamaño,dtype=object)
piso=0
depto=""
tipo_A=0
tipo_B=0
tipo_C=0
tipo_D=0
nombres=np.empty(tamaño,dtype=object)
ruts=np.empty(tamaño,dtype=int)
# ------------------ CODIGO PRINCIPAL ------------------
for k in range(tamaño):
    deptos[k]=""
print(ruts)
os.system("pause")
while True:
    os.system("cls")
    print(" ------------------ Casa Feliz ------------------ ")
    opcion_menu=str(input("""
1.- Comprar departamento
2.- Mostrar departamentos disponibles
3.- Ver listado de compradores
4.- Mostrar ganancias totales
5.- Salir\n"""))
    if opcion_menu=="1":
        os.system("cls")
        fd.imprimir_deptos(deptos)
        piso=int(input("¿En qué piso desea comprar?\n"))
        while not 0<piso<11:
            print("Error... piso no válido")
            piso=int(input("¿En qué piso desea comprar?\n"))
        depto=str(input("¿Qué tipo de departamento desea?\n")).strip().upper()
        while not depto in ["A","B","C","D"]:
            print("Error... tipo de departamento no válido")
            depto=str(input("¿Qué tipo de departamento desea?\n")).strip().upper()
        deptos,nombres,ruts,tipo_A,tipo_B,tipo_C,tipo_D=fd.marcar_depto(deptos,piso,depto,nombres,ruts,tipo_A,tipo_B,tipo_C,tipo_D)
        os.system("pause")
    elif opcion_menu=="2":
        os.system("cls")
        fd.imprimir_deptos(deptos)
        os.system("pause")
    elif opcion_menu=="3":
        os.system("cls")
        print(np.sort(ruts))
        os.system("pause")
    elif opcion_menu=="4":
        os.system("cls")
        fd.imprimir_ganancias(tipo_A,tipo_B,tipo_C,tipo_D)
        os.system("pause")
    elif opcion_menu=="5":
        os.system("cls")
        opcion_menu=str(input("¿Está seguro de que quiere salir? S/N\n")).strip().upper()
        if opcion_menu=="S":
            break
        else:
            print("Volviendo al menú principal")
            os.system("pause")
