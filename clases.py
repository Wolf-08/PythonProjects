"""
class NombreClass:
"""
class Person:
  pass
  #With pass tell us pyhon that only create the class

"""
Self--> To reference a class parameter
execute when the class is create
"""
class Person1:
  def __init__(self,name,age):
    self.name=name
    self.age=age

#No is a  object of the class
#The class is a object in python 
Person1.name="Alex"
Person1.age=38
#Accesing to values
print(Person1.name)
#Create a object 
person1= Person1("Manuel",35)
#Accces to values of the object
print(person1.name,person1.age)
#print out memory location with id
print(id(person1))