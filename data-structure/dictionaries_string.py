#dictionary to repersent sibling names of student + list

student_siblings = {
    "Howard":['Barbie',"Anthony",'Annie'],
    "Barbie":['Howard',"Anthony",'Annie'],
    "yujing":["Jimmy"],
    "Mike":["Angel"]
}
student_brother_sisters = student_siblings.get("Howard")
student_brother_sisters.sort()
for sibiling in student_brother_sisters:
    print(sibiling)


student_siblings = {
    "Howard":["Barbie","Anthony"],
    "yujing":["jimmy"]
}
student_brother_sisters = student_siblings.get("Howard")
student_brother_sisters.sort()
for sibiling in student_siblings:
    print(sibiling)

