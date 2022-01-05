#create a dictionary to store the student in IGCSE and wheter or not they've been 
# naughty = False, nice = True 
# to show which students are getting gifts

naughty_list = {"Yujing":True, "Barbie":False, "Angelina": True}
naughty_student = naughty_list.__getitem__("Barbie")
print("Barbieeeeeeeeeeee", naughty_student)

#create a dictionary to repersent Secret Santa

Secret_santa_list = {"Barbie": "Old_big_nose_santa"}
who_got_barbie = Secret_santa_list.__getitem__("Barbie")
print(who_got_barbie)


