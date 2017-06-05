# -------------------------------------------------------------------------------------------------
# STRING
# -------------------------------------------------------------------------------------------------

print('\n\t\tSTRING\n')

print("Hello Word!")                            # first example 
print('Hello Word!')                            # second example
			
print("I don't think")                          # aphostrophe problem resolution (1)
print('He said :" Look at the sky!"...')        # aphostrophe problem resolution (2)	
print('I don\'t think')                         # aphostrophe problem resolution (3)
print(r'/home/Captain/example')                 # aphostrophe problem resolution (4)

print('Hi' + str(5))                            #convert argument

firstName = 'Captain '                          # use of variable (1)
print(firstName)                                # ...
print(firstName + 'Mich')                       # ...

print(firstName * 5)                            # multiply a string 

# -------------------------------------------------------------------------------------------------
# WORK with STRING
# -------------------------------------------------------------------------------------------------

print('\n\t\tWORK with STRING\n')

user = 'Tuna'

print(user[0])                          # use it if you want a specif letter of a string
print(user[1])                          # ...
print(user[2])                          # ...
print(user[3])                          # ...

print('')

print(user[-1])                         # ...if you want to start from the end
print(user[-2])                         # ...
print(user[-3])                         # ...
print(user[-4])                         # ...
		
print('')

print(user[1:3])                        # to slicing up a string[from character 'x' to(:) character 'y' not including 'y')
print(user[0:4])                        # ...
print(user[1:])                         # ...
print(user[:])                          # ...

print('')

print(len(user))                        # to measure the lenght of a string ( N.B: blank space count as character)
print(len('Tuna'))                      # ...
	
print(user.find('un'))                  # find the offset of a substring in 'user'; return 1 if the substring is found
print(user.replace('una', 'omb'))       # replace occurencesof a string in 'user' with another

print(user)                             # notice that the originally string is not permanently modified

print(user.upper())                     # convert all the contenent upper or lowercase 
print(user.isalpha())                   # find out if all the character in the string are alphabetic and return true if there is at least one character, 						 
                                        # false otherwise

line = 'aaa,bbb,cccccc,dd\n'

print(line.split(','))                  # split on a specific delimiter into a list of substring
print(line.rstrip())                    # remove whitespace characters on the right side 
print(line.rstrip().split())            # combine two operation 


print('%s, eggs, and %s' % ('spam', 'SPAM!'))           # formatting expression
print('{}, eggs, and {}'.format('spam', 'SPAM!'))       # formatting_Method

# -------------------------------------------------------------------------------------------------
# PATTERN MATCHING
# -------------------------------------------------------------------------------------------------

import re                                                       

str_example = 'Hello    Python world'                           # search for a substring that begins with the word "Hello" followed by zero or more tabs 
match = re.match('Hello[\t]*(.*)world', str_example)            # or space, followed by arbitrary characters 
print(match.group(1))                                           # saved as matched group (avaiable only if a substring is found)

pattern = '/usr/home/testuser'                                  # another example that picks out three groups separated by slashes
match = re.match('[/:](.*)[/:](.*)[/:](.*)', pattern)           # ...
print(match.groups())                                           # ...

match = re.split('[/:]', pattern)                               # in this case split give out the same result as previous example
print(match)                                                    # ...


