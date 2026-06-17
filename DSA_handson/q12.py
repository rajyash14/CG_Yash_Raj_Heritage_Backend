def find_all_positions(my_list, target):
    positions = []
    for i in range(len(my_list)):
        if my_list[i] == target:
            positions.append(i)
    return positions
user_list = input("Enter items separated by spaces: ").split()
user_target = input("What item do you want to find ? ")
print(find_all_positions(user_list, user_target))