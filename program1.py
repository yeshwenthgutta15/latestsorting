#   Implement Binary Search

def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    list = [1, 3, 5, 7, 9]
    target = 5
    index = binary_search(list, target)
    if index != -1:
        print(f"The index of {target} in the list is {index}")
    else:
        print(f"The target {target} is not in the list")