#data validation - length check

password = input("enter a password")
password_length = len(password)

if(password_length < 7 or password_length >15):
    print("your password must be between 7 - 15 characters")

#----------------------------------------------------------------

#data validation - admin password

admin_password = input("enter your new password")
admin_password_length = len(admin_password)

if (admin_password_length >= 6 and admin_password_length <= 12):
    print("your password must be between 7 - 15 characters")
else:
    print("password must be 6 - 12 characters")

#------------------------------------------------------------------

name = input("enter your name:")
#(two == meansequal)
#check if user enters an empty string 
name_length = len(name)
if (name_length == 0):
    print("You cannot enter an empty name")
elif(name_length < 3):
    print("Name must be more than three letters")
elif(name_length > 25):
    print("name mmust be less than 25 characters")

#------------------------------------------------------------------
#VAILDATION TASK - WRITE CODE  THAT TAKES USER input and vaidates its length
#ask the user for  a resutrannt name 
#validate that the name is greater tha  5 letters and less than 25 letters
resturant_name = input("Enter your favorite resturant name:")
resturant_name_length = len(resturant_name)
if resturant_name_length == 0:
    print("please type a name ")
elif resturant_name_length < 5 :
    print("Name must be more than 5 letters")
elif resturant_name_length > 25:
    print("name must be less then 50 letters")
else:
    print("This is the most awful name I ever heard")
