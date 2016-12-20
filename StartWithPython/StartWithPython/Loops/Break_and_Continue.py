#BREAK and CONTINUE

print('\n\t\tBREAK and CONTINUE\t\t\n')

magicNumber = 25
													# example break statement
for n in range(101):								# ...
	if n is magicNumber:							# ...
		print(n, "is the magic number!")			# ...
		break										# ...
	else:											# ...
		print(n)									# ...
													# ...
print('')											# ...

numbersTaken = [2, 5, 12, 33, 17]							# example continue statement
															# ...
print('Here are the numbers that are taken:')				# ...s
print(numbersTaken)											# ...
print('')													# ...
															# ...
print('Here are the numbers that are still avaiable:')		# ...
for n in range(1, 20):										# ...
	if n in numbersTaken:									# ...
		continue											# ...
	print(n)												# ...
															# ...
print('')												    # ...
