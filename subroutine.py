import random
def main_function():
    first_number = get_random(1,100)
    second_number = get_random(101,200)
    result = add(first_number, second_number)
    print(result)
#helper function #1(subroutine)
def get_random(start,end):
    random_number = random.randint(start, end)
    return random_number
#helper function #2(subroutine)
def add(number, anothernumber):
    return (number +anothernumber)

#call our main function to start the program 
main_function()