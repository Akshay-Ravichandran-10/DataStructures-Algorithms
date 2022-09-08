```
def insertElement(array, index, element):
    sizeOfArray = len(array)

    array.append(element)

    arr = array.copy()

    for i in range(len(arr)-1,index,-1):
        arr[i],arr[i-1] = arr[i-1],arr[i]

    return arr


def insertElement1(array, index, element):
    array.insert(index,element)
    return array


if __name__ == "__main__":
    array = [1,2,3,4,5]
    print(insertElement1(array, 2, 10))
```
