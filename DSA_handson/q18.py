def find_last(my_list, target):
    last_position = -1
    for i in range(len(my_list)):
        if my_list[i] == target:
            last_position = i
    return last_position

user_list = input("Enter items separated by spaces: ").split()
user_target = input("Enter the item to find its last spot: ")
print(find_last(user_list, user_target))