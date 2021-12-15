#dictionary to repersent sibling names of student

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
