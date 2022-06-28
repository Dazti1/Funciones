
def ponderado(nota,ponderacion):
    ponderacion=ponderacion/100
    nota=nota*ponderacion
    return nota

def nota_eximicion(nota_eximicion,nota_acumulada,ponderacion_acumulada):
    ponderacion=0
    ponderacion=1-(ponderacion_acumulada/100)
    nota_eximicion=(nota_eximicion-nota_acumulada)/ponderacion
    return nota_eximicion
