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


dicc= {
  "D1": "Dato1",
  "D2": "Dato2",
  "D3": "Dato3"
}

#Ways to print out a element in a dictionary 
#1. Show the key of dictionary
for element in dicc:
  print(element)
#2. Show the value of the key 
for element in dicc:
  print(dicc[element])
#3. Show the values trohugt the value 
for element in dicc.values():
  print(element)
#4.Show the key and the value
for key in dicc:
  print(key,"->",dicc[key], end=" ,")

