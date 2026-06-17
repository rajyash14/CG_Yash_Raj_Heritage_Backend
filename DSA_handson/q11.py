def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1
user_list = input("Enter items separated by spaces: ").split()
user_target = input("What do you want to find? ")
print(linear_search(user_list, user_target))