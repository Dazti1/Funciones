def imprimir_deptos(deptos):
    print(f"""
          A\tB\tC\tD  
Piso 10  [{deptos[36]}]\t[{deptos[37]}]\t[{deptos[38]}]\t[{deptos[39]}]
Piso 9   [{deptos[32]}]\t[{deptos[33]}]\t[{deptos[34]}]\t[{deptos[35]}]
Piso 8   [{deptos[28]}]\t[{deptos[29]}]\t[{deptos[30]}]\t[{deptos[31]}]
Piso 7   [{deptos[24]}]\t[{deptos[25]}]\t[{deptos[26]}]\t[{deptos[27]}]
Piso 6   [{deptos[20]}]\t[{deptos[21]}]\t[{deptos[22]}]\t[{deptos[23]}]
Piso 5   [{deptos[16]}]\t[{deptos[17]}]\t[{deptos[18]}]\t[{deptos[19]}]
Piso 4   [{deptos[12]}]\t[{deptos[13]}]\t[{deptos[14]}]\t[{deptos[15]}]
Piso 3   [{deptos[8]}]\t[{deptos[9]}]\t[{deptos[10]}]\t[{deptos[11]}]
Piso 2   [{deptos[4]}]\t[{deptos[5]}]\t[{deptos[6]}]\t[{deptos[7]}]
Piso 1   [{deptos[0]}]\t[{deptos[1]}]\t[{deptos[2]}]\t[{deptos[3]}]""")

def marcar_depto(deptos,piso,depto,nombres,ruts,tipo_A,tipo_B,tipo_C,tipo_D):
    if depto=="A":
        if deptos[(piso*4)-4]=="X":
            print("Este departamento no está disponible.\nRegresando al menú principal.")
        else:
            deptos[(piso*4)-4]="X"
            piso=(piso*4)-4
            nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            while not len(nombres[piso])>0:
                print("Error... Nombre no válido")
                nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            while not 10000000<ruts[piso]<99999999:
                print("Error... run no válido (Debe contener 8 dígitos)")
                ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            print("Compra realizada con exito, regresando al menú principal.")
            tipo_A=tipo_A+1
        return deptos,nombres,ruts,tipo_A,tipo_B,tipo_C,tipo_D
    elif depto=="B":
        if deptos[(piso*4)-3]=="X":
            print("Este departamento no está disponible.\nRegresando al menú principal.")
        else:
            deptos[(piso*4)-3]="X"
            piso=(piso*4)-3
            nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            while not len(nombres[piso])>0:
                print("Error... Nombre no válido")
                nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            while not 10000000<ruts[piso]<99999999:
                print("Error... run no válido (Debe contener 8 dígitos)")
                ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            print("Compra realizada con exito, regresando al menú principal.")
            tipo_B=tipo_B+1
        return deptos,nombres,ruts,tipo_A,tipo_B,tipo_C,tipo_D
    elif depto=="C":
        if deptos[(piso*4)-2]=="X":
            print("Este departamento no está disponible.\nRegresando al menú principal.")
        else:
            deptos[(piso*4)-2]="X"
            piso=(piso*4)-2
            nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            while not len(nombres[piso])>0:
                print("Error... Nombre no válido")
                nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            while not 10000000<ruts[piso]<99999999:
                print("Error... run no válido (Debe contener 8 dígitos)")
                ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            print("Compra realizada con exito, regresando al menú principal.")
            tipo_C=tipo_C+1
        return deptos,nombres,ruts,tipo_A,tipo_B,tipo_C,tipo_D
    elif depto=="D":
        if deptos[(piso*4)-1]=="X":
            print("Este departamento no está disponible.\nRegresando al menú principal.")
        else:
            deptos[(piso*4)-1]="X"
            piso=(piso*4)-1
            nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            while not len(nombres[piso])>0:
                print("Error... Nombre no válido")
                nombres[piso]=str(input("Ingrese su nombre: ")).strip().capitalize()
            ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            while not 10000000<ruts[piso]<99999999:
                print("Error... run no válido (Debe contener 8 dígitos)")
                ruts[piso]=int(input("Ingrese su run sin dígito verificador ni guión: "))
            print("Compra realizada con exito, regresando al menú principal.")
            tipo_D=tipo_D+1
        return deptos,nombres,ruts,tipo_A,tipo_B,tipo_C,tipo_D

def imprimir_ganancias(tipo_A,tipo_B,tipo_C,tipo_D):
    print(f"""
Tipo de departamento\tCantidad\tTotal
Tipo A 3.800 UF       \t{tipo_A}\t    {tipo_A*3800} UF
Tipo B 3.000 UF       \t{tipo_B}\t    {tipo_B*3000} UF
Tipo C 2.800 UF       \t{tipo_C}\t    {tipo_C*2800} UF
Tipo D 3.500 UF       \t{tipo_D}\t    {tipo_D*3500} UF
Total                 \t{tipo_A+tipo_B+tipo_C+tipo_D}\t    {(tipo_A*3800)+(tipo_B*3000)+(tipo_C*2800)+(tipo_D*3500)} UF""")
