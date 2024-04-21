def validar_estandar_conocimiento(cantidad_cursos:int,antiguedad:int):
   
    if antiguedad - (cantidad_cursos * 6) <= 6:
        return True
   
    
   