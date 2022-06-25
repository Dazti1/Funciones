import numpy as np
import os
import Funciones_gym as fg
# --------------- VARIABLES ---------------
opcion_menu=""
tamaño=2
nombres=np.empty(tamaño, dtype=object)
edades=np.empty(tamaño, dtype=int)
pesos=np.empty(tamaño,dtype=int)
estaturas=np.empty(tamaño,dtype=float)
imcs=np.empty(tamaño,dtype=float)
clasificaciones=np.empty(tamaño,dtype=object)
maximo=0
# --------------- CODIGO PRINCIPAL ---------------
while True:
    os.system("cls")
    opcion_menu=str(input("""
--------------- Menu Principal ---------------
1.- Cargar datos y ver IMC
2.- Listar registros por sobre lo normal
3.- Nombre edad del max imc
4.- Salir\n"""))
    if opcion_menu=="1":
        os.system("cls")
        print("\n-----CARGAR DATOS-----")
        for k in range(tamaño):
            nombres[k]=str(input("Ingrese nombre: ")).strip().capitalize()
            while not len(nombres[k])>0:
                print("ERROR... campo vacío detectado")
                nombres[k]=str(input("Ingrese nombre: ")).strip().capitalize()
            edades[k]=int(input("Ingrese la edad: "))
            while not edades[k]>=1:
                print("ERROR... Edad tiene que  ser mayor o igual a 1")
                edades[k]=int(input("Ingrese la edad: "))
            pesos[k]=int(input("Ingrese el peso: "))
            while not pesos[k]>0:
                print("ERROR... Peso tine que ser mayor que 0")
                pesos[k]=int(input("Ingrese el peso: "))
            estaturas[k]=float(input("Ingrese estatura: "))
            while not estaturas[k]>=1:
                print("ERROR... Estatura no válida")
                estaturas[k]=float(input("Ingrese estatura: "))
            imcs[k]=fg.calcular_imc(pesos[k],estaturas[k])
            clasificaciones[k]=fg.determinar_clasificacion(imcs[k])
            fg.imprimir_datos(nombres[k],edades[k],pesos[k],estaturas[k],imcs[k],clasificaciones[k])
            os.system("pause")
            os.system("cls")
        os.system("pause")
    elif opcion_menu=="2":
        os.system("cls")
        print("\n----- Listar Datos -----")
        for k in range(tamaño):
            if imcs[k]>25:
                fg.imprimir_datos(nombres[k],edades[k],pesos[k],estaturas[k],imcs[k],clasificaciones[k])
        os.system("pause")
    elif opcion_menu=="3":
        os.system("cls")
        maximo=np.max(imcs)
        for k in range(tamaño):
            if imcs[k]==maximo:
                fg.imprimir_datos(nombres[k],edades[k],pesos[k],estaturas[k],imcs[k],clasificaciones[k])
        os.system("pause")
    elif opcion_menu=="4":
        break
