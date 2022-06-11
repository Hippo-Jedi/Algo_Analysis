import time
import random

def insertsort(arr):
    i = 0
    l = len(arr)
    while(i < l):
        temp = arr[i]
        j = i
        while(j > 0 and temp < arr[j - 1]):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
        i += 1
    return arr

n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
index = 0
while (index < len(n)):
    a = time.time()
    insertsort([random.random() for _ in range(n[index])])
    z = time.time()
    runtime = (z - a)
    print("n Value: " + str(n[index]), "time: " + str(runtime))
    index += 1