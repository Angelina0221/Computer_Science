
numbers = [100, 50, 10, 300, 55, 0, 1, 44, 23, 22, 55, 89, 90]

zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

numbers.sort()

for number in numbers:
    print(number)