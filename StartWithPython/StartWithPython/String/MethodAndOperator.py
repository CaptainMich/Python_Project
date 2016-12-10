#STRING(2) 
print('\n\t\tSTRING(2)\t\t\n')

user = 'Tuna'

print(user[0])								# use it if you want a specif letter of a string
print(user[1])								# ...
print(user[2])								# ...
print(user[3])								# ...

print('')

print(user[-1])								# ...if you want to start from the end
print(user[-2])								# ...
print(user[-3])								# ...
print(user[-4])								# ...
			
print('')

print(user[1:3])							# to slicing up a string[from character 'x' to(:) character 'y')
print(user[0:4])							# ...
print(user[1:])								# ...
print(user[:])								# ...

print('')

print(len(user))							# to measure the lenght of a string ( N.B: blank space count as character)
print(len('Tuna'))							# ...


# STRING (3)
print('\n\t\tSTRING(3)\t\t\n')

user = 'tuna'
	
print(user.find('un'))						# find the offset of a substring in 'user'; return 1 if the substring is found
print(user.replace('una', 'omb'))			# replace occurencesof a string in 'user' with another

print(user)									# notice that the originally string is not permanently modified

print(user.upper())							# convert all the contenent upper or lowercase 
print(user.isalpha())							# find out if all the character in the string are alphabetic and return true if there is at least one character, 						 
											# false otherwise least one character, false otherwise 
	
line = 'aaa,bbb,cccccc,dd\n'

print(line.split(','))						# split on a specific delimiter into a list of substring
print(line.rstrip())						# remove whitespace characters on the right side 
print(line.rstrip().split())				# combine two operation 


print('%s, eggs, and %s' % ('spam', 'SPAM!'))			# formatting expression
print('{}, eggs, and {}'.format('spam', 'SPAM!'))		# formatting_Method