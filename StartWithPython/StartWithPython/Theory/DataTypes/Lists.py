# -------------------------------------------------------------------------------------------------
# LISTS
# -------------------------------------------------------------------------------------------------

print('\n\t\tLISTS\n')

players = [70,5,9]                  # syntax of a list
print(players)                      # print entire list

# -------------------------------------------------------------------------------------------------
# WORK with LIST
# -------------------------------------------------------------------------------------------------

print('\n\tWORK with LISTS\n')

print(players[2])                   # to access a member of a list in the position ['x']
players[2] = 96                     # to permanently change the value of a member 
print(players)                      # to see the changes

print(players + [0,1,2])            # add list to another list, and see the change...
print(players)                      # ... but it is not a permanently change

players.append(4)                   # to permanently add an element to the list
print(players)                      # to see the change

players = players + [5]             # another way to permanently add element to the list
print(players)                      # to see the change

print('')

print(players[0:2])                 # to slicing up a list [from element 'x' to(:) element 'y']
print(players[1:2])                 # ...
print(players[1:])                  # ...
print(players[:])                   # ...

print('')

players[:2] = [0,1,2]               # to change multiple values [from element 'x' to(:) element 'y']
print(players)                      # to see the changes	

players[:2] = []                    # to delete items from the list(1)
print(players)                      # to see the changes

players[:2] = []                    # to delete item from the list(2)
print(players)                      # to see the change

players[:] = []                     # to delete the entire list	
print(players)                      # to see the change

