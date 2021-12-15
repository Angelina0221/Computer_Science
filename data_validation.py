#outline the steps - algoritim
#ask user for pet name, store it in a varible
#use fn tp fet name length, store length in  new varible
#varidate - if elif to print error meassage if len is outside boundaries



pet_name = input("Enter your pet name:")

pet_name_length = len(pet_name)

if (pet_name_length == 0):
    print("You must enter something")
elif (pet_name_length < 2):
    print("Enter a name with more then 2 letters")
elif(pet_name_length >= 20):
    print("Enter a name that is less then 20 letters")




