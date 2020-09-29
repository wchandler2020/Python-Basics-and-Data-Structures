1
nums = [1, 2, 3, 4, 5 ]
my_list = [x ** 2 if x == 5 else x * 2 for x in nums]

#2
my_string = "Hello from the otherside"
stripped = my_string.strip()

#3
new_list = [1,2,3, "text", 7, 10]
filtered = list(filter(lambda x: isinstance(x, int), new_list))


#4
def what_to_buy(item, *args, **kwargs):
    if 'store' in kwargs:
        return f"Buy {item} in {kwargs['store']}"
    else:
        return f"Buy {item} in any store"
    return item

# print(what_to_buy("Laptop", store = "Walmart"))

all([num % 2 == 0 for num in [2, 4, 6, 8, 10, 11]])
 