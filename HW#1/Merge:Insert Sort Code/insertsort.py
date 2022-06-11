filename = "data.txt"

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

with open(filename, "r") as file:
    for line in file:
        newL = line.rstrip('\n')
        old = map(int, newL.split(' '))
        newArr = insertsort(old[1:])
        string = ' '.join(str(e) for e in newArr)
        with open('insert.txt', 'a') as iFile:
            iFile.write(string)
            iFile.write('\n')