is_computer_science_student = False
is_chang_jung_student = True

#and-both values must be true for the expression to be true
is_enrolled_cs = is_computer_science_student and is_chang_jung_student
print("is_enrolled_cs", is_enrolled_cs)

#or - one of the values must be true for the expression to be true
is_enrolled_chang_jung = is_computer_science_student or is_chang_jung_student
print("the value of our OR statment", is_enrolled_chang_jung)


#- - - - - - - - - - - - - - - - - - - - - - - - - -  - - - -  - - - - - - - - - -- 

A = True
B = True
C = A or B #expect this to be true if eitherA or B is true

D = True 
E = False
F = D or E #expect F to be false if both D and E are not true
print(C)
print(F)

is_computer_science_student = False
is_chang_jung_student = True

if(is_chang_jung_student and is_computer_science_student):
    print("You are enrolled in my computer science class")
elif(not is_computer_science_student and is_chang_jung_student):
    print("You are not in my computer science class")