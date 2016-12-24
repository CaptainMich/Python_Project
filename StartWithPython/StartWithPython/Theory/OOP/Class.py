# -------------------------------------------------------------------------------------------------
# CLASS
# -------------------------------------------------------------------------------------------------

print('\n\t\tCLASS\n')

class Enemy:                                                # define a class; 
                                                            # group similiar variables and function togheter
    life = 3 							               # ...
    def attack(self):                                       # ...
        print('\tOuch -> life -1')                          # ...
        self.life -= 1                                      # ...
                                                    
    def checkLife(self):                                    # ...
        if self.life <= 0:                                  # ...
            print('\tI am dead')                            # ...
        else:                                               # ...
            print('\t' + str(self.life) + ' life left')     # ...

firstEnemy = Enemy()                                        # how to access to the class
print('Enemy_One:')                                         # ...
firstEnemy.checkLife()                                      # ...
firstEnemy.attack()                                         # ...
firstEnemy.checkLife()                                      # ...

print('')
                                                             
secondEnemy = Enemy()                                       # access again to the class and discover that
print('Enemy_Two:')                                         # each object is indipendent of one another
secondEnemy.checkLife()                                     # ...
secondEnemy.attack()                                        # ...      
secondEnemy.attack()                                        # ... 
secondEnemy.attack()                                        # ... 
secondEnemy.checkLife()                                     # ...

# -------------------------------------------------------------------------------------------------
# CLASS __INIT__
# -------------------------------------------------------------------------------------------------

print('\n\n\t\tCLASS __INIT__\n')

class Character:									
	
    def __init__(self, x):                                  # __init__ = initialize --> pass a value to them and use 
        self.energy = x                                     # it in a different way for the object that we'll create

    def get_energy(self):                                   # ...                           
        return self.energy                                  # ...

Pippo = Character(5)                                        # initialize Pippo's energy to 5
Pluto = Character(18)                                       # initialize Pluto's energy to 18

print('Pippo energy is ' + str(Pippo.get_energy()))
print('Pluto energy is ' + str(Pluto.get_energy()) + '\n')