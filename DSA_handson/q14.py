def check_inventory(inventory, product_id):
    for item in inventory:
        if item == product_id:
            return True
    return False

inventory_list = input("Enter product IDs separated by spaces: ").split()
product_target = input("Which product ID do you want to check? ")
print(check_inventory(inventory_list, product_target))