def calcular_sueldo(valor_hora,horas_trabajadas):
    sueldo=valor_hora*horas_trabajadas
    return sueldo

def imprimir_estadisticas(nombre,valor_hora,horas_trabajadas,sueldo):
    print(f"""
==========================
Nombre: {nombre}
Valor hora: {valor_hora}
Horas trabajadas: {horas_trabajadas}
Sueldo recibido: {sueldo}
==========================""")
