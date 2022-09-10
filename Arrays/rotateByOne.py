def rotateByOne(array):
    n = len(array)
    x = array[0]
    for i in range(1,n):
        array[i-1] = array[i]
    array[n-1] = x
    return array


def rotateByOne1(array):
    array = array[1:] + array[0:1]
    return array

def rotateByOne2(array):
    array.append(array.pop(0))
    return array


if __name__ == "__main__":
    array = [10,20,30,40,50]
    print(rotateByOne2(array))