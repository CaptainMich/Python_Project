# -------------------------------------------------------------------------------------------------
# DICTIONARY
# -------------------------------------------------------------------------------------------------

print('\n\t\tDICTIONARY\n')

identity = {}                                                           # define empty dictionary 
identity['name'] = 'Bob'                                                # create keys by assignment
identity['job'] = 'Car driver'                                          # ...
identity['age'] = 25                                                    # ...

print(identity,'\n')                                                    # print the dictionary (first way)


car = {'Ferrari': 'is beautiful car',                                   # define a dictionary 
       'Lamborghini' : 'is incredible car',                             # = {'key..': 'value..',...}
       'Maserati' : 'is expensive car'}                                 # N.B : more than one entry per key not allowed
                                                                                                                        
for k,v in car.items():                                                 # k = key, v = value
    print(k,v)                                                          # print the dictionary (second way)
print()                                                                 # ...
    

games =  dict(name='Call of Duty',                                      # define a dictionary (keyword arguments)
              genre='shooter',                                          # ...
              minimum_age=18)                                           # ...
print(games)                                                            # print the dictionary (third way)


team_player = dict(zip(['name', 'role', 'number'],                      # define a dictionary (zipping togheter sequences of key and values)
                       ['Lebron', 'Guard', '23']))                      # ...
print(team_player)                                                      # print the dictionary(fourth way)   
                          
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

#del car;                                                   # delete entire dictionary
#print("After delete entire dictionary:")                   # (you should have a NameError, car list is no longer defined) 
#print(car,'\n')                                            # ...(uncomment the code to see the error)

# -------------------------------------------------------------------------------------------------
# NESTING 
# -------------------------------------------------------------------------------------------------

print('\n\t\tNESTING \n')

character = {'name': {'first' : 'Luk', 'last': 'De Vek'},           # three key values ('name', 'jobs', 'age'), but values now are more complex:
            'jobs' : ['lawyer','driver'],                           # - nested dict for name
            'age' : 35}                                             # - nested list for jobs
print(character)                                                    # print the dictionary

print(character['name'])                                            # different way to access the components
print(character['name']['last'])                                    # ... index the nested dictionary
print(character['jobs'])                                            # ...
print(character['jobs'][-1])                                        # ... index the nested list 

character['jobs'].append('advisor')                                 # expand character's job description
print(character)                                                    # ... to see the change