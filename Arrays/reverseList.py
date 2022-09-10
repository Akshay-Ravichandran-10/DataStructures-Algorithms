def reverse_list(array):
    low = 0
    high = len(array) - 1
    while low < high:
        array[low],array[high] = array[high],array[low]
        low += 1
        high -= 1
    return array


def reverse_list1(array):
    array[::-1]
    return array


def reverse_list2(arr):
    arr.reverse()
    return arr


def reverse_list3(array):
    arr = list(reversed(array))
    return arr


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    print(reverse_list(array))
    print("1: "+str(reverse_list1(array)))
    print(reverse_list2(array))
    print(reverse_list3(array))