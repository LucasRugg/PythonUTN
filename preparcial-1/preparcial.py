import modulo1
opcion = 5 #Inicializo la variable en un valor aleatorio para que ingrese al bucle
empleados = []
cantidadEmpleados = 2 #cambiar a numero de empleados necesarios

while(opcion != 4):
    print("1- Registrar empleado")
    print("2- Agregar nuevo curso")
    print("3-Mostrar resumen")
    print("4-Salir")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
       for i in range(cantidadEmpleados):
           nombre = input("Ingrese nombre del empleado: ")
           antiguedad = int(input("Ingrese antiguedad en meses: "))
           legajo = input("Ingrese el legajo del empleado: ")
           while len(legajo) != 5:
               print("EL legajo debe tener 5 caracteres")
               legajo = input("Ingrese nuevamente legajo: ")
           empleado = {"nombre": nombre, "legajo": legajo, "antiguedad": antiguedad, "cursosRealizados":[]} 
           empleados.append(empleado)    
           
        
         
    if opcion == 2:
        legajo = input("Ingrese el legajo del empleado a buscar: ")
        encontrado = False
        for empleado in empleados:
            if empleado["legajo"] == legajo:
                encontrado = True
                nombreCurso = input("Ingrese nombre del curso realizado: ")
                empleado["cursosRealizados"].append(nombreCurso)
                print("Curso agregado correctamente")
                break
        if not encontrado:
            print("No se encontro al empleado")
        
    if opcion == 3:
        empleadosOrdenados = sorted(empleados, key=lambda x:len(x["cursosRealizados"]),reverse = True)
        for empleado in empleadosOrdenados:
            
            print(empleado["nombre"]," - ", empleado["legajo"], " -  Antiguedad ", empleado["antiguedad"]," meses")
            print("Cursos :",empleado["cursosRealizados"])
            print("Cantidad de cursos: ", len(empleado["cursosRealizados"]))
            if modulo1.validar_estandar_conocimiento(len(empleado["cursosRealizados"]), empleado["antiguedad"]) == True:
                print("Cumple con el estandar")
            else:
                print("No cumple con el estandar")
            print("-------------------------------------------------------------------")
    if opcion == 4:
        print("SALIR")