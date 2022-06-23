import numpy as np

def calcular_descuentos_legales(sueldo_bruto):
    salud=sueldo_bruto*0.07
    pension=sueldo_bruto*0.13
    liquido=sueldo_bruto-salud-pension
    
    return salud,pension,liquido

def imprimir_liquidacion(rut, nombre, sueldo_bruto,salud,pension,liquido):
    print(f"""
    =================== LIQUIDACION ===================
    \tRut: {rut} \t\t Nombre: {nombre}
    \tSueldo Bruto: ${sueldo_bruto}
    \tDscto. Salud: ${salud}
    \tDscto. Pension: ${pension}
    
    \tLiquido pagar: ${liquido}
    ===================================================""")

def maximo(ruts,nombres,sueldos_liquidos):
    max = sueldos_liquidos.max()
    for k in range(3):
        if max==sueldos_liquidos[k]:
            print(f'''
            Rut: {ruts[k]}
            Nombre: {nombres[k]}\t ${sueldos_liquidos[k]}''')
