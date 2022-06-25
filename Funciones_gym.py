import numpy as np
import os

def calcular_imc(peso,estatura):
    imc=peso/(estatura**2)
    return round(imc,2)

def determinar_clasificacion(imc):
    if imc<=16.00:
        clasificacion="Infrapeso: Delgadez Severa"
    elif 16.00<imc<=16.99:
        clasificacion="Infrapeso: Delgadez moderada"
    elif 17.00<imc<=18.49:
        clasificacion="Infrapeso: Delgadez aceptable"
    elif 18.50<imc<=24.99:
        clasificacion="Peso Normal"
    elif 25.00<imc<=29.99:
        clasificacion="Sobrepeso"
    elif 30.00<imc<=34.99:
        clasificacion="Obeso: Tipo I"
    elif 35.00<imc<=40.00:
        clasificacion="Obeso: Tipo II"
    else:
        clasificacion="Obeso: Tipo III"
    return clasificacion

def imprimir_datos(nombre,edad,peso,estatura,imc,clasificacion):
    print(f"""
==============INFO==============
\t Nombre: {nombre} \t\t Edad:{edad} años
\t Peso:{peso}Kg.  \t\t Estatura:{estatura}m.
\t IMC:{imc}  \t\t Clasificación: {clasificacion}
================================""")
