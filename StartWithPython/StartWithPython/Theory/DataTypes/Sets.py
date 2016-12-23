# -------------------------------------------------------------------------------------------------
# SETS
# -------------------------------------------------------------------------------------------------

print('\n\t\tSETS\n')

groceries = {'cereal', 'milk', 'starcrunch', 'beer', 'duct tape', 'lotion', 'beer'} # list that can't containe any duplicate... 
print(groceries)                                                                    # ... in fact,beer is print only once	

if 'milk'in groceries:
    print('You already have milk hoss!')
else:
    print('You need milk!')

if 'sausages'in groceries:
    print('You already have sausages hoss!')
else:
    print('You need sausages!')

print('')

