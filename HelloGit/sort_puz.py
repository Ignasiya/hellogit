numbers = [5, 3, 6, 2, 7, 1, 4, 8, 0, 9, 10, 19, 17, 15, 13, 18, 11, 16, 12, 14]
size = len(numbers)
sortIndex = 0
while (sortIndex < size - 1):
    index = 0
    while (index < size - 1 - sortIndex):
        if (numbers[index] > numbers[index + 1]):
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
        index = index + 1
    sortIndex = sortIndex + 1
print(numbers)