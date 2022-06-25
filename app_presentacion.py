import os
import Funciones_presentacion as fp

# --------------- VARIABLES ---------------
nota=0
ponderacion=0
ponderado=0
c_notas=0
opcion_menu=""
nota_acumulada=0
# --------------- CODIGO PRINCIPAL ---------------
while True:
    opcion_menu=str(input("""
--------------- Menu Principal ---------------
1.- Ingresar notas
x.- Salir
"""))
    if opcion_menu=="1":
        os.system("cls")
        c_notas=int(input("¿Cuantas notas tiene el ramo?\n"))
        for k in range(c_notas):
            nota=float(input(f"Ingrese nota {(k+1)}: "))
            ponderacion=int(input("Ingrese valor de la prueba: %"))
            nota_acumulada=fp.ponderado(nota,ponderacion)+nota_acumulada
        print(f"Su nota de presentación es {nota_acumulada}")
        os.system("pause")
    elif opcion_menu=="x":
        break
