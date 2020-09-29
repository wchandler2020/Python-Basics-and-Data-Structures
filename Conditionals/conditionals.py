# num1, operator, num2 = input("enter a number: ").split()

# num1 = int(num1)
# num2 = int(num2)

# if(operator == "+"):
#     print(num2 + num2)
# elif(operator == "-"):
#     print(num1 - num2)
# elif(operator == "*" or "x"):
#     print(num1 * num2)
# elif(operator == "/"):
#     print(num1 / num2)
# else:
#     print("can't provide an answer at this time.")

age = int(input("how old are you: "))

if(age < 5):
    print("You are not ready for school yet")
elif(age > 6 and age < 10):
    print("you should be in elementry school.")
elif(age > 10 and age < 14):
    print("you should be in middle school.")
elif(age > 14 and age < 18):
    print("you should be in high school.")
else:
    print("you are ready for college.")