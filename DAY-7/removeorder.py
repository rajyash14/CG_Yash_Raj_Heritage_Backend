order = ['pizza', 'burger', 'fries', 'coke', 'burger']

# Customer cancels one burger (removes FIRST occurrence)
order.remove('burger')
print(order)  # ['pizza', 'fries', 'coke', 'burger']

# Error if item not found:
# order.remove('pasta')  → ValueError: list.remove(x): x not in list

# Safe way to remove
if 'pasta' in order:
    order.remove('pasta')
else:
    print('Item not in order')
