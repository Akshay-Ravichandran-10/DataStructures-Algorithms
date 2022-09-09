def findodd(array):
    res = 0
    for i in array:
        res = res ^ i

    return res

def findOdd1(array):
    res = None
    for i in array:
        count = array.count(i)
        if count % 2 != 0:
            res = i
            break
    return res


if __name__ == "__main__":
    array = [10,20,20,30,10,10,30,10]
    print(findOdd1(array))
    print(findodd(array))