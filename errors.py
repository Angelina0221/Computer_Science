#user input error - this throws an execution if a string is given by use
#age = int(input("Enter your age:"))

#try-catch block
try :
    age = int(input("Enter your age:"))
except ValueError as error:
    print("Please enter a number only")
    print(error)
    print(type(error))
else:
    print('No exceptions were thrown, execute this:')

#if age is 0!!!!
try :
    age = int(input("Enter your age:"))
    calculation = 10/age
except (ValueError,ZeroDivisionError) :
    print("Please enter a number only")
    print(error)

print("If this is executed the program didn't stop running")


