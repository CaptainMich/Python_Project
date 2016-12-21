# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
while True:
    choice = int(input('Please enter the number of exercise: '))

# -------------------------------------------------------------------------------------------------
# Exercise_01
# Write a Python program which accepts the radius of a circle from the user and compute the area
# -------------------------------------------------------------------------------------------------

    if(choice == 1):

        from math import pi

        print('\nExercise_01')

        radius = float(input ('Input the radius of the circle: '))
        area = (pi * radius**2)
        print('The area of the circle with radius ' + str(radius) + ' is ' + str(area) + '\n\n')

# -------------------------------------------------------------------------------------------------
# Exercise_02
# Write a Python program to calculate number of days between two dates
# -------------------------------------------------------------------------------------------------

    elif(choice == 2):

        from datetime import date

        print('\nExercise_02')

        yy = int(input('Input the start date year: '))
        mm = int(input('Input the start date month: '))
        dd = int(input('Input the start date day: '))
        start_date = date(yy,mm,dd)

        yy = int(input('Input the finish date year: '))
        mm = int(input('Input the finish date month: '))
        dd = int(input('Input the finish date day: '))
        finish_date = date(yy,mm,dd)

        diff = (finish_date - start_date)

        print('Number of days between ' + str(start_date) + ' and ' + str(finish_date) + ' is ' + str(diff) + '\n')

# -------------------------------------------------------------------------------------------------
# Exercise_03
# Write a Python program to compute the greatest common divisor (GCD)  and the least common multiple (LCM)
# of two positive integers.
# -------------------------------------------------------------------------------------------------

    elif(choice == 3):
    
        def gcd(x, y):
            while y != 0:
                (x, y) = (y, x % y)
            return abs(x)

        def lcm(x,y):
            return ((x * y)/ gcd(x,y))

        print('\nExercise_03')

        firstNumber = int(input('Please enter first number: '))
        secondNumber = int(input('Please enter second number: '))

        print('GCD between ' + str(firstNumber) + ' and ' + str(secondNumber) + ' is ' + str(gcd(firstNumber,secondNumber)))
        print('LCM between ' + str(firstNumber) + ' and ' + str(secondNumber) + ' is ' + str(lcm(firstNumber,secondNumber)) + '\n')

# -------------------------------------------------------------------------------------------------
# Exercise_04
# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). 
# -------------------------------------------------------------------------------------------------

    elif(choice == 4):       

        import math

        print('\nExercise_04')  

        p1 = [int(input('Enter the coordinates of the first point: ')) for x in range(2)]
        p2 = [int(input('Enter the coordinates of the second point: ')) for x in range(2)]
        distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

        print('Distance between ' + str(p1) + ' and ' + str(p2) + ' is ' +  str(distance) + '\n')
          
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

    else:
        print('Make a choice')