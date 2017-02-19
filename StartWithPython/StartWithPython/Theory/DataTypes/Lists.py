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
print(players)                      # to see the change

print(players + [0,1,2])            # concatenate list to another list, and see the change...
print(players)                      # ... but it is not a permanently change

players = players * 2               # multiply the list 
print(players)                      # to see the change

players.append(4)                   # to permanently add an element to the list
print(players)                      # to see the change

players.pop(2)                      # to permanently remove an element to the list (position of the list is indicate in brackets)
print(players)                      # to see the change

players.sort()                      # to order list in ascending fashion
print(players)                      # to see the change

players.reverse()                   # to reverse list 
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


# -------------------------------------------------------------------------------------------------
# NESTING and List COMPREHENSION
# -------------------------------------------------------------------------------------------------

print('\n\tNESTING and List COMPREHENSION\n')

matrix = [[1,2,3],                                      # 3 x 3 Matrix, as nested list
          [4,5,6],                                      # ...
          [7,8,9]]                                      # ...

print(matrix)                                           # print entire list
print(matrix[1])                                        # print row 2
print(matrix[1][2])                                     # print element 3 of the row 2

col2 = [row[1] for row in matrix]                       # collect the items in column 2
print(col2)                                             # to see the change

print(matrix)                                           # matrix is unchanges
                                                        # .. some other examples
print([row[1] + 1 for row in matrix])                   # add 1 to each item in column 2
print([row[1] for row in matrix if row[1] % 2 == 0])    # filter out odd items of column 2

diag = [matrix[i][i] for i in [0,1,2]]                  # collect diagonal from matrix
print(diag)                                             # to see the result

doubles = [letter * 2 for letter in 'spam']             # repeat character in a string
print(doubles)                                          # to see the result






