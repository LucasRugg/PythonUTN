medicos = []
opcion = 5

while opcion != 4:
    
    print("1-Registrar medico")
    print("2-Agregar titulo reconocido")
    print("3-Mostrar resumen")
    print("4-Salir")
    opcion = int(input("Ingrese opcion: "))
    
    if opcion == 1:
        nombre = input("Ingrese nombre del medico: ")
        documento = int(input("Ingrese documento: "))
        existe = False
        for m in medicos:
            if m["documento"] == documento:
                existe = True
                
       
                     
        medico = {"nombre" : nombre, "documento" : documento, "titulos":[]}
        medicos.append(medico)
        if existe == True:
            print("El documento ya existe en la base de datos")
            medicos.pop()
            
       
    if opcion == 2:
        dniAbuscar = int(input("Ingrese dni del medico a buscar: "))
        encontrado = False
        for medico in medicos:
            if medico["documento"] == dniAbuscar:
                tituloAgregar = input("Ingrese titulo a agregar: ")
                medico["titulos"].append(tituloAgregar)
                encontrado = True
                break
        if not encontrado:
            print("No se encontro el medico")
    
    if opcion == 3:
        for medico in medicos:
            print(f"{medico["nombre"]} - Nro Doc: {medico["documento"]}")
            print(f"Titulos: {medico["titulos"]} ")
            print(f"Cantidad de titulos {len(medico[ 'titulos'])}")
    
    if opcion == 4:
        print("SALIR")        
                
             