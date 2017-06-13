# -------------------------------------------------------------------------------------------------
# TUPLES
# -------------------------------------------------------------------------------------------------

print('\n\t\tTUPLES\n')

numbers = (1,2,3,4,1)                                   # first example: 4-item tuple
print(numbers)                                          # ...

mixed_tuple = 'spam', 3.0, [10,20,30]                   # second example: pharenteses are generally omitted
print(mixed_tuple)                                      # ...

# -------------------------------------------------------------------------------------------------
# WORK with TUPLES
# -------------------------------------------------------------------------------------------------

print('\n\t\tWORK with TUPLES\n')

print(numbers + (5,6))                                  # concatenation
print(numbers)                                          # ...to see the changes

print(numbers[0])                                       # indexing(1)
print(mixed_tuple[2][1])                                # indexing(2)
print(numbers.index(4))                                 # type-specific method: number four appears at offset 3
print(numbers.count(1))                                 # counts how many times the argument occured

#numbers[0] = 2                                         # tuples are immutable(1) (uncomment to see the error)
#mixed_tuple.append(234)                                 # tuples are immutable(2) (uncomment to see the error)
mutable_numbers = (2,) + numbers[1:]                    # create a new tuple for change value
print(mutable_numbers)                                  # to see the changes



                