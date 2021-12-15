#character (letter) list
letter_grades = ["A", "A-", "A", "B","B", "C", "C-", "A-", "B+"]
letter_grades.append("B")
letter_grades.append("A")
letter_grades.append("A")

#count number of people with grade A
number_of_A_grades = letter_grades.count("A")
print("number of grades A:", number_of_A_grades)
#-------------------------------------------------
#integer list
numbers = [0, 0, 1, 1, 2,3,4,0,0,1,1,0]
#count number of zeros
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)
#sort list
numbers.sort()

#printeach item in list(iteration)
for number in numbers:
    print(number)
#----------------------------------------------------
#bolean list
has_completed_homework = [True, True, False]
number_of_completed_homeworks = has_completed_homework.count(True)
print("Number of the people who did homwwork", number_of_completed_homeworks)



#create a list of boolean values to repersent students who have done their homework

has_done_homework = [True,False,True]
print(has_done_homework)
has_done_homework.sort()
print(has_done_homework)

#how many false values are in this data sturcture
number_false = has_done_homework
print(number_false)

#iterate(tranvese the data structure)
for student in has_done_homework:
    print(student)

amount_of_money_in_each_student=[100,50,40,70]
amount_of_money_in_each_student.sort()
print(amount_of_money_in_each_student)
amount_of_money_in_each_student.append(56)
print(amount_of_money_in_each_student)

#list strings

student_names = ["Adrian","Mike","Charlie","Hanson","Yujing","Barbie"]
print(student)
student_names.sort()
print(student_names)


