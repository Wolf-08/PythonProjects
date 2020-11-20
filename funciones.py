"""
def mi_func():
  codigo_funcion
No se ejecuta hasta que es llamado
"""
"""
Two concepts of python functions and 
compression lists
"""
def listCompress():
  lista=(x**2 for x in range (10))
  return lista 

listaPorCompresion=listCompress()
for element in listaPorCompresion:
  print(element)

"""
Parametros y argumentos para funcs
Muchas veces se trata de manera igual 
Pero no lo son parametro es lo que se envia 
Argumento lo que se recibe 
"""
def func_arg(name):
  print("My name is  ", name)

func_arg("Juan")
"""
Notes about return in python 
return can be a plus or arguments or a value 
and the value can be print out in print funcion
""" 
#Default values in the definition of function
def sum(a=0,b=4):
  return a+b

print(sum(3,3))
#It not define values in the function call 
#python taken the default values 
print(sum())
"""
read the book for more notes
"""