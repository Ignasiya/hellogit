sample = [5, 3, 6, 2, 7, 1, 4, 8, 0, 9, 10, 19, 17, 15, 13, 18, 11, 16, 12, 14]
left = 0
right = len(sample) - 1
while left <= right:
    for i in range(left, right, +1):
        if sample[i] > sample[i + 1]:
            sample[i], sample[i + 1] = sample[i + 1], sample[i]
    right -= 1

    for i in range(right, left, -1):
        if sample[i - 1] > sample[i]:
            sample[i], sample[i - 1] = sample[i - 1], sample[i]
    left += 1

print(sample)