#   Implement Quick Sort

def quick_sorting(list, low, high):
    if low < high:
        pivot = parted(list, low, high)
        quick_sorting(list, low, pivot - 1)
        quick_sorting(list, pivot + 1, high)


def parted(list, low, high):
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high] = list[high], list[i + 1]
    return i + 1


if __name__ == "__main__":
    list = [7, 1, 5, 3, 8, 6, 4, 0, 2, 9, -1]
    quick_sorting(list, 0, len(list) - 1)
    print(list)