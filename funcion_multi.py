#4.	Elabore un módulo llamado operaciones 
# que almacene dos funciones: funcion_suma() y f
# unción_prod() que sumen y multipliquen respectivamente
#  todos los números de una lista. Por ejemplo: funcion_
# suma() ([1,2,3,4]) debería imprimir 10 y 
# función_prod ([1,2,3,4]) debería devolver 24. 

def funcion_suma(x):
    return sum(x)

def funcion_prod(x):
    producto=1
    for i in x:
        producto *=i
    return producto    