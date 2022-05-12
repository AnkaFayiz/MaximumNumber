# Finding Max Number
import random

def max_number(arr):
    
    maxNumber = arr[0]

    for i in range(len(arr)):
        if maxNumber < arr[i]:
            maxNumber = arr[i]
        else:
            maxNumber = maxNumber
    return maxNumber

if __name__ == '__main__':
    arr = []
    n = int(input("Input length of an array : "))
    for i in range(n):
        generateNumber = random.randint(1, n / 2 - 1 % 2)
        arr.append(generateNumber)
    
    print(arr)
    print(max_number(arr))
