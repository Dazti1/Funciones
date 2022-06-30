def ponderado(nota,ponderacion):
    ponderacion=ponderacion/100
    nota=round((nota*ponderacion),2)
    return nota

def nota_eximicion(nota_eximicion,nota_acumulada,ponderacion_acumulada):
    ponderacion=0
    ponderacion=1-(ponderacion_acumulada/100)
    nota_eximicion=round((((nota_eximicion-nota_acumulada)/ponderacion)+0.05),1) # El +0.05 es para redondear por exceso en el primer decimal
    return nota_eximicion

def nota_examen(nota_presentacion):
    nota_examen=round((3.95-(nota_presentacion*0.6))/0.4,1)
    return nota_examen
