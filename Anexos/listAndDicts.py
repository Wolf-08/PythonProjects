favorite_languages={
  'jen':['python','ruby'],
  'phil':['python','haskell'],
  'sarah':['c']
}

#We use the name defined in the loop 
#and the variable language to hold each value from the dictionary
#beacuase we know than each value  will be a list 
"""
name is the key in the dictionary
"""
for name,languages in favorite_languages.items():
  print("\n "+ name + "'s favorite languages are:")
  for language in languages: #Se necesita un segundo for para iterar en la lista 
    print("\t" + language.title())

#Dictionary in a Dictionary 
user = {
  'albert':{
    'name':'albert',
    'last_name':'einsten',
    'country':'germany',},
    'alex':{
    'name':'wolf',
    'last_name':'the wall',
    'country':'north',
    }
}
#username contains the keys of the dictionary principal
#user_info contains the dictionary of user information 
for username,user_info in user.items():
  print("\n username: " + username)
  full_name = user_info['name'] + " " + user_info['last_name']
  location =  user_info['country']

  print("Full name: " + full_name)
  print("Location: " + location)