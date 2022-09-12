def subArraywithSum(array,targetSum):
    index = 0
    current = 0

    for e in range(len(array)):
        current += array[e]

        while (current > targetSum):
            current -= array[index]
            index += 1
        if (current == targetSum):
            return True
    return False

if __name__ == "__main__":
    array = [1,8,12,5,14,6]
    print(subArraywithSum(array,22))