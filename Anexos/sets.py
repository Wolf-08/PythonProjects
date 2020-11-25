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

"""
Python dict 
more notes comming son from the book
"""

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
  print(key,"->",dicc[key],end=" ,")

#Dictionary book python crash course 
person= {
  'first_name': "Lucas",
  'last_name':   "Gomez",
  'age': 35,
  'city' : "Ciduad Mexico",
}
print("Su nombre es :",person['first_name']+ person['last_name'] +
  "y su edad es" + str(person['age']) + "vive en" + person['city'] 
)

fav_number={
  'raul':23,
  'alex':2,
  'raul':8,
  'karen':9,
  'dan':16,
  }
#Items: list of  key,value pairs in the dictionary
#Keys is  a default behaviario when looping through a dictionary 
for key,value in fav_number.items():
  print("\n key: " + key)
  print("Value: " ,value)

#The dicctionary can use the sorted() function to get a copy of 
#the keys in order

for key in sorted(fav_number.keys()):
  print("\n key: " + key)
  #print("Value: " ,value)

"""
Nesting: Can nest a ser of dictionaries inside a list 
, a list of items inside a dictionary, or even a dictionary 
inside another dictionary
"""
#List of dictionaries
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'blue','points':15}
alien_2 = {'color':'red','points':10}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
  print(alien)

#creating a 30 aliens
aliens2=[]
#make 30 green aliens
for alien in range(30):
  new_alien={'color':'green','point':5,'speed':'slow'}
  aliens2.append(new_alien)

#show the fist 5 aliens 

for alien in aliens2[:5]:
  print(alien)

print("Total of aliens (len of the list )",len(aliens2))

for alien in aliens2[:3]:
  if alien['color']== 'green':
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['point'] = 10