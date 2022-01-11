#initalize a list (linkedlist)
students_names = ["Mike","Mars","Charlie"]

#add a name to our list
students_names.append("Mars")
students_names.insert(0,"Mr.Amini") #insert at index (0) first position
#delete a name

students_names.remove("Charlie")

#iterate over our list
for name in students_names:
    print(name)

#get the length of the list
length = len(students_names)
print(length)

