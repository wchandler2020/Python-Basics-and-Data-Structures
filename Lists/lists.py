import random
import math

# rand_list = [1, 2, "William", 2.55]
# one_to_ten = list(range(11))
# new_list = rand_list + one_to_ten
# first_three = new_list[:3]

# for i in first_three:
#     print("{} : {}".format(first_three.index(i), i))

# print("William" in first_three)
# print("index of William: ", first_three.index("William"))

# new_rand_list = []

# for i in range(random.randrange(20)):
#     new_rand_list.append(i)

# print(new_rand_list)

# rand_list = []
# for i in range(5):
#     rand_list.append(random.randrange(20))



# for j in rand_list:
#     print(j, end=", ")

# even_list = [i*2 for i in range(30)]

# for k in even_list:
#     print(k, end=", ")


# num_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 8]
# my_new_list = num_list_1[5:]
# another_new_list = my_new_list + num_list_1[:5]
#
#
#
# ##remove deplicates from a list
#
# remove_dup_list = list(dict.fromkeys(num_list_1))
# print(remove_dup_list)
# print(type(another_new_list))


# healthy = ["chicken", "fish", "brocolli", "fruit"]
# refrig = ["candy", "pasta", "cheese"]
#
# if "cheese" not in healthy:
#     refrig.remove("cheese")
#
# print(len(refrig))



# squares = [i ** 3 for i in range(10) if i % 2 == 0]

workdays = ["Monday", "Tuesday", "Wednesday", "Friday"]
workdays.insert(3, "Thursday")
workdays.remove("Friday")

print(workdays)


