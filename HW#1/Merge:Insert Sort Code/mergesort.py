filename = "data.txt"

def mergesort(arr):
    l = len(arr)
    if (l < 2):
        return arr
    middle = l // 2
    left = mergesort(arr[:middle])
    right = mergesort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    arr2 = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            arr2.append(left[i])
            i += 1
        else:
            arr2.append(right[j])
            j += 1
    arr2 += left[i:]
    arr2 += right[j:]

    return arr2

with open(filename, "rb") as file:
    for line in file:
        newL = line.rstrip('\n')
        old = map(int, newL.split(' '))
        newArr = mergesort(old[1:])
        string = ' '.join(str(e) for e in newArr)
        with open('merge.txt', 'a') as mFile:
            mFile.write(string)
            mFile.write('\n')