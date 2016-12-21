# -------------------------------------------------------------------------------------------------
# Exercise_01
# Write a Python program which accepts the radius of a circle from the user and compute the area
 # -------------------------------------------------------------------------------------------------

from math import pi

print('Exercise_01')

radius = float(input ('Input the radius of the circle: '))
area = (pi * radius**2)
print('The area of the circle with radius ' + str(radius) + ' is ' + str(area) + '\n\n')

# -------------------------------------------------------------------------------------------------
# Exercise_02
# Write a Python program to calculate number of days between two dates
# -------------------------------------------------------------------------------------------------

from datetime import date

print('Exercise_02')

yy = int(input('Input the start date year: '))
mm = int(input('Input the start date month: '))
dd = int(input('Input the start date day: '))
start_date = date(yy,mm,dd)

yy = int(input('Input the finish date year: '))
mm = int(input('Input the finish date month: '))
dd = int(input('Input the finish date day: '))
finish_date = date(yy,mm,dd)

diff = (finish_date - start_date)

print('Number of days between ' + str(start_date) + ' and ' + str(finish_date) + ' is ' + str(diff))

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------