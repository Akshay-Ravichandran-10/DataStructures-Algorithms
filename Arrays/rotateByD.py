def rotateByD(array,d):
    reverse(array,0,d-1)
    reverse(array,d,len(array)-1)
    reverse(array,0,len(array)-1)
    return array


def reverse(array,low,high):
    while(low < high):
        array[low],array[high] = array[high],array[low]
        low += 1
        high -= 1


if __name__ == "__main__":
    array = [10,20,30,40,50]
    print(rotateByD(array,3))