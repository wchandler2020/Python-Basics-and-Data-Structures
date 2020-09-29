import random

# for nums in range(21):
#     if(nums % 2 != 0):
#         print(nums)

num = random.randrange(1, 10)
num_guesses = 0

while num_guesses < 5:
    user_guess = int(input("guess a number between 1 and 10: "))
    if(user_guess == num):
        print("you got it")
        break
    else:
        num_guesses = num_guesses + 1
        print("No please try again.", 5 - num_guesses, " guesses remaining")
        continue
