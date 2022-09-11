def kMaxSum(array,k):
    current = 0
    for i in range(k):
        current += array[i]
    result = current
    for i in range(k, len(array)):
        current = current + array[i] - array[i-k]
        result = max(result,current)
    return result


if __name__ == "__main__":
    array = [1,8,30,-5,20,7]
    print(kMaxSum(array,4))