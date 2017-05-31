# -------------------------------------------------------------------------------------------------
# DICTIONARY
# -------------------------------------------------------------------------------------------------

print('\n\t\tDICTIONARY\n')

identity = {}                                               # define empty dictionary 
identity['name'] = 'Bob'                                    # create keys by assignment
identity['job'] = 'Car driver'                              # ...
identity['age'] = 25                                        # ...

print(identity,'\n')                                        # print the dictionary (first way)

car = {'Ferrari': 'is beautiful car',                       # define a dictionary 
       'Lamborghini' : 'is incredible car',                 # = {'key..': 'value..',...}
       'Maserati' : 'is expensive car'}                     # N.B : more than one entry per key not allowed
                                                                                                                        
for k,v in car.items():                                     # k = key, v = value
    print(k,v)                                              # print the dictionary (second way)

# -------------------------------------------------------------------------------------------------
# WORK with DICTIONARY
# -------------------------------------------------------------------------------------------------

print('\n\n\t\tWORK with DICTIONARY\n')

print('Ferrari', car['Ferrari'],'\n')                       # print the value of ['Ferrari']

car['Ferrari'] += ',it is also very fast'                   # add string to 'Ferrari' value
print('Ferrari', car['Ferrari'],'\n')                       # ... 

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