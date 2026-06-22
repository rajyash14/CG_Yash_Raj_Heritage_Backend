#Iterative Binary Search
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

inventory = [101, 205, 312, 456, 589, 623, 741, 850, 912, 999]
product_id = 623

result = binary_search_iterative(inventory, product_id)
if result != -1:
    print(f'Product {product_id} found at position {result}')
else:
    print(f'Product {product_id} not in inventory')