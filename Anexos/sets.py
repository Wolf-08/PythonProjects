#Set es una coleccion sin orden y sin indices
#No se permiten elementos repetidos y los elemnos no 
#Pueden modificarse

#El set o coleccion permite los mismo metodos que 
#tupplas y listas 
planetas = {"marte", "jupiter","venus"}
#Largo del set 
print(len(planetas))
planetas.discard("marte")
#Quitar un elemento 
planetas.add("Tierra")
print(planetas)
#Para limpiar el ser 
planetas.clear()
print(planetas)