while True:
    choice = int(input('Please enter the number of exercise: '))

# -------------------------------------------------------------------------------------------------
# Exercise_01
# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS
# -------------------------------------------------------------------------------------------------

    if(choice == 1):

        import struct

        print('\nExercise_01')  
        print(struct.calcsize("P") * 8)
        print('')

# -------------------------------------------------------------------------------------------------
# Exercise_02
# Write a Python program to get OS name, platform and release information
# -------------------------------------------------------------------------------------------------

    elif(choice == 2):

        import platform
        import os

        print('\nExercise_02')
        print(platform.system())
        print(platform.release())
        print(os.name)
        print('')

# -------------------------------------------------------------------------------------------------
# Exercise_03
# Write a Python program to find out the number of CPUs using
# -------------------------------------------------------------------------------------------------

    elif(choice == 3):

        import multiprocessing

        print('\nExercise_03')
        print(multiprocessing.cpu_count())
        print('')

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

    else:
        print('Make a choice')