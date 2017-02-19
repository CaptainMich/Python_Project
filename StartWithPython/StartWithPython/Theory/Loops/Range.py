# -------------------------------------------------------------------------------------------------
# RANGE
# -------------------------------------------------------------------------------------------------

print('\n\t\tRANGE\n')
									
for x in range(10):                                         # to make an action ('n') times
    print("Pippo")                                          # ...
print('')                                                   # ...

for x in range(5, 12):                                      # second example -->  (from 'x' to(,) 'y') 
    print(x)                                                # ...
print('')                                                   # ...

for x in range(10, 40, 5):                                  # third example -->  (from 'x' to(,) 'y' in steps of(,) 'z') 
    print(x)                                                # ...
print('')                                                   # ...

print(list(range(4)))                                       # create new list from 0 to 3     
print(list(range(-6,7,2)))                                  # -6 to +6 by 2
                                             
print([[x ** 2, x ** 3] for x in range(4)])                 # some more complicated example
print([[x, x / 2, x*2] for x in range(-6, 7, 2) if x > 0])  # ...
