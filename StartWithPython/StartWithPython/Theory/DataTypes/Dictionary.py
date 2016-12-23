# -------------------------------------------------------------------------------------------------
# DICTIONARY
# -------------------------------------------------------------------------------------------------

print('\n\t\tDICTIONARY\n')

car = {'Ferrari': 'is beautiful and super fast car',        # define a dictionary 
       'Lamborghini' : 'is incredible car',                 # = {'key..': 'value..',...}
       'Maserati' : 'is expensive car'}                     # N.B : more than one entry per key not allowed
                                                                                                                        
print(car,'\n')                                             # print all things in car
print('Ferrari', car['Ferrari'],'\n')                       # print the value of ['Ferrari']

for k,v in car.items():                                     # k = key, v = value
    print(k,v)                                              # print the dictionary

# -------------------------------------------------------------------------------------------------
# WORK with DICTIONARY
# -------------------------------------------------------------------------------------------------

print('\n\n\t\tWORK with DICTIONARY\n')

car['Maserati'] = 'is luxury car';                          # update existing element of a dict
print('Maserati', car['Maserati'],'\n')                     # ...

car['Mercedes'] = "is very comfortable car";                # add new element to a dict
print(car,'\n')                                             # ...


del car['Ferrari'];                                         # remove entry with key 'Name'
print("After delete Ferrari, dictionary is:")               # ...
print(car,'\n')                                             # ...
  
car.clear();                                                # remove all entries in dict
print("After delete all entries, dictionary is:")           # ...
print(car,'\n')                                             # ...

del car;                                                    # delete entire dictionary
print("After delete entire dictionary:")                    # (you should have a NameError, car list is no longer defined) 
print(car,'\n')                                             # ...