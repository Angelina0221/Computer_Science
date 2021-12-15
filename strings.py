#What is a string
message = "hello world"
print(message)
#()means a function,to excute, do this to take a action
uppercase_message = message.upper()
print(uppercase_message)



#string operations-

#return lenght of a string
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
print(alphabet_length)

print(alphabet_length - 2)

for counter in range(alphabet_length):
    print("this is printed same # times as the lenght alphabet",counter)


#lowercase --> uppercase
upper_alphabet = alphabet.upper()
print(upper_alphabet)

#what is ASCII?
#computers represent "a" as a binary number
#convert character to it's ASCII code - ord()
# ord()由英文變成原本的數字
english_a = "a"
ASCII_a = ord(english_a)
print(ASCII_a)


#convert ASCII to a_z - chr()
#chr()由數字變成原本的英文
ASCII_code_for_a  = 97
a_z_letter = chr(97)
print(a_z_letter)

#add to strings togehter
string_one = "good morning"
string_two = "my heighbor"
combined = string_one + " " + string_two
print(combined)

#return the position of a specific letter
#012345678910111213141516171819202122232425(26 total)
alphabet = "abcdefghijklmnopqrstuvwxyz"
position_of_a_letter_d = alphabet.index("d")
print(position_of_a_letter_d + 1)