#list charachter
score = ["A","B"]
score.append("A")
score.append('C')
score.sort()
print(score)

score_C = score.count("C")
print("print number of score C", score_C)

#list interger
birthday_month = [ 9,8,7,3,2,1,]
birthday_month.append(9)
birthday_month_Jan = birthday_month.count(1)
print("Birthday that is janurary", birthday_month_Jan)

for birthday in birthday_month:
    print(birthday)


