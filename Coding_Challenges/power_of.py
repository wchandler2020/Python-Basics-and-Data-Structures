def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

def is_power_of_three(num):
    while(num % 3 == 0):
        num /=3
    return num == 1

output = is_power_of_two(64)
print(output)