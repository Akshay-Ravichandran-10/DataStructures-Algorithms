
def get2largest(array):
    largest = None
    seclargest = None

    if len(array) == 1:
        largest = array[0]

    for i in array:
        if largest == None or i > largest:
            seclargest = largest
            largest = i

        elif i != largest:
            if seclargest == None or i > seclargest:
                seclargest = i

    return largest,seclargest


if __name__ == '__main__':
    array = [20, 1000, 22, 594]
    largest, secLargest = get2largest(array)
    print("Largest "+ str(largest))
    print("Second Largest "+ str(secLargest))


