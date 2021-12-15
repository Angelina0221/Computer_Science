#program make decisions based on control logic (control)

student_grade = 93
if student_grade >= 90:
    print("Your grade is A")
elif student_grade < 90 and student_grade > 90:
    print("Your grade is B")
elif student_grade < 88 and student_grade > 78:
    print("Your grade is C")
else:
    print("Your grade is a D or F")
    


#write a program using if-elif-else that....
#looks at a variable for temperature = 20C
#if temperature is above 30 C, print it's hot
#elif temperature is above 10 C, but below 30 C, print it's warm
#elif temperature is below 10 C, print it's cold
#else print "bring an umbrella just in case"

temperature = 20
if temperature > 30:
    print("It's hot")
elif temperature < 10 and temperature > 30:
    print("It's warm")
elif temperature < 10 and temperature > 5:
    print("It's cold")
else:
    print("bring an umbrella just in case")
    

