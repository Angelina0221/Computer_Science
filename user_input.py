#get and store user input
name = input("Enter your name: ")

#output the user input on the screen 
print("Good morning", name)


# ask user to enter a number(interger)
#save it in a varible called "number"

user_input = int(input("Enter a number: "))

#defining a new function called"get_square"
#it takes one value and  returns value * value(square)
#pass input to a function that does math

def get_square(number):
    return number * number

#call function, pass user input, print output
#save the result in a varible called"square"
#print the"square" varible on screen

square = get_square(user_input)
print(square)