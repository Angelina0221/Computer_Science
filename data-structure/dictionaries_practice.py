student_in_ICGSE = {
    "Yujing":["Computer Science","Physics"],
    "Angelina":["Computer Science","Physics"],
    "Barbie":["Math","Chemistry","Computer Science"],
    "Howard":["Math","Chemistry","Computer Science"],
}
student_in_ICGSE = student_in_ICGSE.get("Yujing")
student_in_ICGSE.sort()
for students in student_in_ICGSE:
    print(students)
