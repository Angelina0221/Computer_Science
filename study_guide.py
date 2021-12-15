#1 varible

#a)write a bollean to represent whether or not you will pass the exam
pass_the_exam = True

#b)write a interger varible to represent your score on the exam
exam_score = 90

#c)write a floating point to represent the class average on the exam
class_average = 87.5

#d)write a string varible to repersent something you'd say to your friend in the morning
what_you_say_to_your_friend = "Good morning"

#2 iterations - for loop

#a) write a for loop that prints "I am a polite and kind person"x101
for i in range (10):  
     print("I am a polite and kind person", i)

#control flow - write a simple if-elif statment to describe this...
#a)if student has a grade of 90-100 "you rock"
#b)elif student has a grade of 80-90 "you are great"
#c)elif if student has a grade of less than 70 - 80 print "not bad,keep working"
#d)else if student has a grade of less than 70 print "You can always do more and become more,growth mindset"
#>,<,=, and or not if_elif-else

grade = 90
if grade > 90 and grade <=100:
    print("You rock")
elif grade > 80 and grade <=90:
    print("You are great")
elif grade > 70 and grade <=80:
    print("Not bad, keep working")
else :
    print("You can always do more and become more,growth mindset")


#arithemetic operstions- write code to complete the follwing questions
1+5
99999 - 9494
38484 * 999
24 / 2
90 %10

a = 1
b = 5
c = a + b
print("1 +5 = ",c)

z = 99999
y = 9494
x =z - y
print("99999 - 94 = ",x)

w = 38484 
d = 999
s = w * d
print("38483 * 999 = ",s)

q = 24 
e = 2
r = q / e
print("24/2 = ",r)

v = 90
n = 10
m = v % n
print("90 % 10 = ",m)


computer_student = 21
money_per_student = 15.5
total = computer_student * money_per_student
print(total)

#strings operation

alphabet = "abcdefghijklmnopqrstuvwxyz"
#write the lenght of the string
alphabet_length = len(alphabet)
print(alphabet_length)

numbers = 123456789
number_length = len(numbers)
print(number_length)
#write code to find the index(position)of the letter "t"
#print the index on the screen 

position = alphabet.find("t")
print(position + 1)


#write code to ask fot the users name 
#print the messagehello to that person's name
name = input("Enter your name:")

#output the user input on the screen
print("Good morning", name)

#strings are object in python
#string the dot operater (.)we can access an object's functions(methods)
message = "This is my message"
uppercase_message = message.capitalize()
print(uppercase_message)

#len function isn't a part of the string object it's more""General"
#that's why it's not called using the dot operater message.len()
length = len(message)

#while loop
number = 0
while(number < 10):
    print("I love computer scinece",number)
    number = number + 1

working = True 
while(working == True):
    print("working")

    
#for loop
for i  in range (5):
    print("Good evening my neighbor", i)

