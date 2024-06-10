# python programme for simple calculation
# function to add two numbers
def add(num1, num2):
    return num1 + num2
# function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
# function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
# function to divide two numbers
def divide(num1, num2):
    return num1 / num2

print ("please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
        
# take input from the user
select = int(input("Select operation from 1, 2, 3, 4: "))

number_1 = int(input("enter first number: "))
number_2 = int(input("enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))
elif select == 2:
    print(number_1,"-", number_2, "=",
          subtract(number_1, number_2))
elif select == 3:
    print(number_1,"*", number_2, "=",
          multiply(number_1, number_2))
elif select == 4:
    print(number_1,"/", number_2, "=",
          divide(number_1, number_2))
    
else:
    print("makosa")