# Ex1 - String 
# Enter text and display it one by one

# text = input("enter a text: ")
# for char in text:
#     print(char)



# Ex2 - String
# Enter text and display number of letter

# text = input("enter a text: ")
# for char in range(len(text)):
#     print(char)



# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter
 
# text = input("enter text: ")
# result = "no"
# for char in range(len(text)):
#     if text[char].upper() == text[char]:
#         result = "yes"
# print(result)



# Ex4 - String 
# We have text = "3 4 5 6"
# Q1 - display number 1 by one without space
# Q2 - Sum all number (Total: 18)

# Q1. display number 1 by one without space

# text = input("enter text: ")
# result = ""
# for char in text:
#     if char != " ":
#         result += char
# print(result)

# Q2. Sum all number (total: 18)

# text = input("enter text: ")
# sum = 0 
# for char in text:
#     if char != ' ':
#         sum += int(char)
# print(sum)




# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse 

# Q1 - Count odd and even number in text

# text = input("enter a text: ")
# Odd_number = 0
# Even_number = 0
# for i in range(len(text)):
#     if i % 2 == 1:
#         Odd_number += 1
#     else:
#         Even_number += 1
# print(Odd_number)
# print(Even_number)


# Q2 - Sum all number 

# text = input("enter a text:")
# sum = 0
# for i in range(len(text)):
#     sum += int(text[i])
# print(sum)


# Q3 - Sum only even number 

# text = input("enter a text: ")
# sum = 0
# for i in range(len(text)):
#     if int(text[i]) % 2 == 0:
#         sum += int(text[i])
# print(sum)


# Q4 - Reverse

# text = input("enter a text: ")
# result = ""
# for i in range(len(text)):
#     result += text[len(text) -1 -i]
# print(result)



# Ex6 - Number
# Enter number and check 
# if odd number print "Odd" otherwise print "Even"

# number = int(input("enter a number: "))
# if number % 2 == 1:
#     print("Odd_number")
# else:
#     print("Even_number")



# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20

# number = int(input("enters a munber: "))
# result = "Out of range"
# for i in range(number):
#     if number >= 10 and number <= 20:
#         result = "Continue"
# print(result)



# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8


# Q1 - How many number 8 in string

# text = input("enter a text; ")
# Counter_8 = 0
# for char in text:
#     if char == "8":
#         Counter_8 += 1
# print("Counter_8 is: ", Counter_8)


# Q2 - What is first index of letter 8

# text = input("enter text: ")
# isfound = False
# index = 0
# while not isfound:
#     if text[index] == "8":
#         print(index)
#         isfound = True
#     index += 1



# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"


# Q1 - Remove space and keep result = "3456"

# string = input("enter text: ")
# result = ""
# for char in string:
#     if char != " ":
#         result += char
# print(result)


# Q2. Multiple each and keep result = "6 8 10 12"


# string = "3 4 5 6"
# total = " "
# i = 0
# while i < len(string):
#     cha = string[i]
#     if cha != " ":
#         total += str(int(cha) * 2) + " "
#     i += 1 
# print(total)


# Ex10 - Number
# Enter 5 numbers and find maximum and minimum value
# Example:
# 1
# 5
# 6
# 7
# 0
# output : Max = 7, Min = 0


# print("Please enter your number : ")
# bigest_number = 0
# smailest_number = 0
# for i in range(5):
#     number = int(input("Enter number : "))
#     if bigest_number == 0 and smailest_number == 0:
#         bigest_number = number
#         smailest_number = number
#     else:
#         if number > bigest_number:
#             bigest_number = number
#         if number < smailest_number:
#             smailest_number = number
# print("Bigest number : ", bigest_number)
# print("Smaillest number : ", smailest_number)
