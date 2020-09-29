# def rev_list(new_list):
#     return [ele for ele in reversed(new_list)]
# print(rev_list([1, 2, 3, 4, 5]))

# names = ["Liam", "Henry", ]
#
# def remove_dup(my_list):
#     new_list = []
#     for i in my_list:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# output = remove_dup([11, 22, 33, 44, 55, 55,])
# print(output)
#
#
#
# def rev_list(new_list):
#     return new_list[::-1]




def rev_list(list_nums, k):
    return list_nums[-k:]

output = rev_list([1,2,3,4,5,6,7], 3)
print(output)

# print("A: ", ord("A"))
# print("65: ", chr(65))

# user_input = input("Enter a word: ")
# secret_string = ""
#
# for char in user_input:
#     secret_string = ord(char.upper())
#     print(secret_string)










