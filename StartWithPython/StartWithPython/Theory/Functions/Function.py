# -------------------------------------------------------------------------------------------------
# FUNCTIONS
# -------------------------------------------------------------------------------------------------

print('\n\t\tFUNCTIONS\n')

def test_one():                                         # define a 'normal' function
    print('Dayum, function is cool')                    # body of a function 

test_one()                                              # call the function 
test_one()                                              # call the function 
test_one()                                              # call the function 

print ('')

def bitcoin_to_usd(btc):                                # define a function that take in input also a variable
    amount = btc * 527                                  # body of function
    print(amount,'$')                                   # ...

bitcoin_to_usd(5.85)                                    # call the fuction
bitcoin_to_usd(1)                                       # call the fuction

print ('')

# -------------------------------------------------------------------------------------------------
# RETURN VALUES
# -------------------------------------------------------------------------------------------------

print('\n\t\tRETURN VALUES\n')


def sample(number):                                     # define the function
	operation = (number / 2 + 7)                       # body of the function
	return operation                                   # return a value


test_sample = sample(20)                                # storage the returned value in a variable
print('Testing Sample: ' + str(test_sample) + '\n')     # simple print statement


# -------------------------------------------------------------------------------------------------
# DEFAULT VALUES for ARGUMENTS
# -------------------------------------------------------------------------------------------------

print('\n\tDEFAULT VALUES for ARGUMENTS\n')


def get_gender(sex = 'Unknown'):                        # define a function with a DEFAULT VALUE
    if sex is 'm':                                      # body of the function (if -elif condition)
        sex = 'Male'                                    # ...
    elif sex is 'f':                                    # ...
        sex = 'Female'                                  # ...
    print(sex)                                          # body of the function (print the final sex)

get_gender('m')                                         # call the function 
get_gender('f')                                         # many time to display
get_gender()                                            # the functionality
	
print('')

# -------------------------------------------------------------------------------------------------
# KEYWORD ARGUMENTS
# -------------------------------------------------------------------------------------------------

print('\n\t\tKEYWORD ARGUMENTS\n')


def dumb_sentence(name = 'Pippo', action = 'ate', item = 'nuts'):       # define a function with 3 default value
    print(name,action,item)                                             # ...

dumb_sentence()                                                         # call the function 
dumb_sentence(name = 'SuperPippo')                                      # call the function with one different keyword argument
dumb_sentence(action = 'drive', item = 'a car')                         # call the function with two different keywords arguments
dumb_sentence('Captain','plays','guitar')                               # call the function with different keywords arguments

print('')

# -------------------------------------------------------------------------------------------------
# FLEXIBLE NUMBER OF ARGUMENTS
# -------------------------------------------------------------------------------------------------

print('\n\tFLEXIBLE NUMBER of ARGUMENTS\n')


def add_numbers(*args):                                         # define a function with a variable number of arguments
    total = 0                                                   # create a variable to store the final result
    for a in args:                                              # loop that adds numbers and print the total
        total += a                                              # ...
    print(total)                                                # ...

add_numbers(3)                                                  # some examples of function call
add_numbers(1, 2, 43)                                           # ...
add_numbers(112312, 1232134, 35765, 146547, 5563)               # ...

print('')

# -------------------------------------------------------------------------------------------------
# UNPACKING ARGUMENTS
# -------------------------------------------------------------------------------------------------

print('\n\t\tUNPACKING ARGUMENTS\n')

def healt_calculator(age, apples_ate, cigs_smoked):                             # define a function
    answer = (100 - age) + (apples_ate * 0.35) - (cigs_smoked * 1)			# ...
    print(answer)                                                               # ...
    	
sample_data = [20, 2, 0]
                                                                                # call the function and ... 
healt_calculator(sample_data[0],sample_data[1],sample_data[2])                  # ...pass arguments one by one ...
healt_calculator(*sample_data)                                                  # ...or unpacking argument list

print('')