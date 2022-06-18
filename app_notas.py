import os
import funciones_notas as fn
#--------- VARIABLES ---------
opcion_menu=""
nota1=0
nota2=0
nota3=0
promedio=0
estado="" # Situación final "Aprobado/Reprobado"
#--------- código principal ---------
while True:
    os.system("cls")
    print("--------- Menú principal")
    opcion_menu=input("""1.- Cargar notas
2.- Estadísticas
3.- Salir
""").strip()
    if opcion_menu=="1":
        os.system("cls")
        print("--------- Cargar notas ---------")
        nota1=float(input("Ingrese primera nota: "))
        while not 1<=nota1<=7:
            nota1=float(input("Nota no válida, intentelo nuevamente: "))
        nota2=float(input("Ingrese segunda nota: "))
        while not 1<=nota2<=7:
            nota2=float(input("Nota no válida, intentelo nuevamente: "))
        nota3=float(input("Ingrese tercera nota: "))
        while not 1<=nota3<=7:
            nota3=float(input("Nota no válida, intentelo nuevamente: "))
        # llamamos a la función sacar promedio
        promedio=fn.sacar_promedio(nota1, nota2, nota3)
        estado=fn.determinar_estado(promedio)
        fn.imprimir_reporte(nota1, nota2, nota3)
        
        os.system("pause")
    elif opcion_menu=="2":
        os.system("cls")
        min, max, prom=fn.sacar_estadisticas(nota1,nota2,nota3)
        print(f"""
              MIN:{min} \t MAX:{max} \t PROM:{prom}""")
        os.system("pause")
    else:
        os.system("cls")
        break
