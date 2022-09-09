
def check_if_sorted(array):

    ascending = True
    descending = True

    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            ascending = False

        if array[i] > array[i-1]:
            descending = False

    return ascending or descending


if __name__ == "__main__":
    array = [10,9,30,40,50]
    res = check_if_sorted(array)
    print(res)



