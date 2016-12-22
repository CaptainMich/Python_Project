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
# Exercise_04
# Write a Python program to get the current username
# -------------------------------------------------------------------------------------------------

    elif(choice == 4):

        import getpass

        print('\nExercise_04')
        print(getpass.getuser())
        print('')

# -------------------------------------------------------------------------------------------------
# Exercise_05
# Write a Python program to get the current username
# -------------------------------------------------------------------------------------------------

    elif(choice == 5):

        import getpass

        print('\nExercise_05')
        print(getpass.getuser())
        print('')

# -------------------------------------------------------------------------------------------------
# Exercise_06
# Write a Python program to test whether the system is a big-endian platform or little-endian platform
# -------------------------------------------------------------------------------------------------

    elif(choice == 6):

        import sys
        
        print('\nExercise_06')
        if sys.byteorder == "little":
            print("Little-endian platform.\n")
        else:
            print("Big-endian platform.\n")

# -------------------------------------------------------------------------------------------------
# Exercise_07
# Write a Python program to get the size of an object in bytes.
# -------------------------------------------------------------------------------------------------

    elif(choice == 7):

        import sys

        print('\nExercise_07')
        user_input = (input('Please enter something, tell you the size: '))
        print("Memory size of '"+ user_input + "' = " + str(sys.getsizeof(user_input)) + " bytes\n")

# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------

    else:
        print('Make a choice')