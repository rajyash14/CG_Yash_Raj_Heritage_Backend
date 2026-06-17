def find_first(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1

user_list = input("Enter items separated by spaces: ").split()
user_target = input("Enter the item to find its first spot: ")
print(find_first(user_list, user_target))