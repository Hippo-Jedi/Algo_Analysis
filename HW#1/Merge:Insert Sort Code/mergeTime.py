import time
import random


def mergesort(arr):
    l = len(arr)
    if (l < 2):
        return arr
    m = l // 2
    left = mergesort(arr[:m])
    right = mergesort(arr[m:])
    return merge(left, right)

def merge(left, right):
    new = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new += left[i:]
    new += right[j:]
    return new

n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
index = 0
while (index < len(n)):
    a = time.time()
    mergesort([random.random() for _ in range(n[index])])
    z = time.time()
    runtime = (z - a)
    print("n value: " + str(n[index]), "time: " + str(runtime))
    index += 1