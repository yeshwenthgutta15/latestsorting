#   Write a program to sort list of strings (similar to that of dictionary)

def strings_sorting(strings):
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if strings[i] > strings[j]:
                strings[i], strings[j] = strings[j], strings[i]

    return strings


if __name__ == "__main__":
    strings = ["pineapple", "mango", "pig", "lion", "abroad", "dog", "yeshwenth"]
    strings_sorted = strings_sorting(strings)
    print(strings_sorted)