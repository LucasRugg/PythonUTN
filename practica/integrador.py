
empleados = []
cursos_disponibles = ["PHP", "Python", "C#", "HTML y CSS", "Java", "JS", "Ruby", "Git"]

def registrarEmpleado():
    nombre = input("Ingrese nombre del empleado: ")
    legajo = input("Ingrese legajo del empleado: ")
    antiguedad = int(input("Ingrese antiguedad del empleado: "))
    
    if antiguedad < 6:
        antiguedad = int(input("La antiguedad debe ser mayor a 6 meses: "))

    empleados.append({"nombre":nombre, "legajo":legajo,"cursos_realizados":[], "antiguedad":antiguedad})
    
    
