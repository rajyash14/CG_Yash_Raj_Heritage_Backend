def count_comparisons(my_list, target):
    comparisons = 0
    for item in my_list:
        comparisons += 1
        if item == target:
            return f"Found it! It took {comparisons} checks."
    return f"Not found. It took {comparisons} checks."

user_list = input("Enter items separated by spaces: ").split()
user_target = input("What are we looking for? ")
print(count_comparisons(user_list, user_target))