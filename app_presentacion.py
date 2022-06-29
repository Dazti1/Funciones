import os
import funciones_presentacion as fp
# --------------- VARIABLES ---------------
nota=0
ponderacion=0
ponderado=0
c_notas=0
opcion_menu=""
nota_acumulada=0
nota_eximicion=0
ponderacion_acumulada=0
# --------------- CODIGO PRINCIPAL ---------------
while True:
    os.system("cls")
    opcion_menu=str(input("""
--------------- Menu Principal ---------------
1.- Ingresar notas
2.- Nota de eximición
x.- Salir
"""))
    if opcion_menu=="1":
        nota_acumulada=0
        os.system("cls")
        print("---------- Nota de Presentación ----------")
        c_notas=int(input("¿Cuantas notas tiene el ramo?\n"))
        for k in range(c_notas):
            nota=float(input(f"Ingrese nota {(k+1)}: "))
            ponderacion=int(input("Ingrese valor de la prueba: %"))
            nota_acumulada=fp.ponderado(nota,ponderacion)+nota_acumulada
        print(f"Su nota de presentación es {nota_acumulada}")
        os.system("pause")
    elif opcion_menu=="2":
        nota_acumulada=0
        ponderacion_acumulada=0
        os.system("cls")
        print("---------- Nota de eximición ----------")
        nota_eximicion=(float(input("¿Nota de eximición?\n")))-0.05 # el -0.05 es para el calculo de nota exacta, si por ejemplo la nota de eximicion es un 5 en realidad necesitas un 4.95
        c_notas=int(input("¿Cuantas notas tiene el ramo?\n"))
        for k in range(c_notas-1):
            nota=float(input(f"Ingrese nota {k+1}: "))
            ponderacion=int(input("ingrese valor de la prueba: %"))
            ponderacion_acumulada=ponderacion+ponderacion_acumulada
            nota_acumulada=fp.ponderado(nota,ponderacion)+nota_acumulada
        nota_eximicion=fp.nota_eximicion(nota_eximicion,nota_acumulada,ponderacion_acumulada)
        print(f"Usted necesita un {nota_eximicion} para eximirse del ramo.")
        os.system("pause")
    elif opcion_menu=="x":
        break
