#   Implement Insertion Sort

def insertion_sorting(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key


if __name__ == "__main__":
    list = [3, 2, 4, 7, 9, 11, 5, -13, -7, 15, 0,19 ]
    insertion_sorting(list)
    print(list)