#key student name - value boolean repersent whether or not the student has pet

has_pets = {"Mars":False, "Henry":False, "Barbie":True, "Adrain":True, "Angelina": False}

#data structure operations - add , delete, search,sort
student_has_pet = has_pets.get("Barbie")
print("The student that has pet:", student_has_pet) 

#traverse the dictionary
for student in has_pets:
    print(student, 'has a pet:', has_pets.get(student))

#remove method - pop()
student_removed = has_pets.pop("Adrain")
print(student_removed)
print(has_pets)

#create a dictionary (key-value pair)
#key = student name
#value = list og scores numbers

student_scores = {
    "Adrain":[90,91,88],
    "Charlie":[88,99,100],
    "Mandy":[90,99,95],
    "Yujing":[99,100,100],
    "Angelina":[99,98,99],
    "Barbie":[100,99,99]
}

student_scores = student_scores.get("Barbie")
for score in student_scores:
    print(score)

