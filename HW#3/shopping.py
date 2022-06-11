import string
import numpy

#This function initializes knapsack(K) and uses the knapsack algorithm to store best 
#family member price in last element of K. Then uses a for loop to determine price an weight.

def knapsack(memberWeight, itemWeight, price, num, case):
    priceTotal = 0
    itemChosen = []
    for a in range(len(memberWeight)):
        K = [[0 for col in range(memberWeight[a]+1)] for row in range(num+1)]
        for i in range(num+1):
                for j in range(memberWeight[a]+1):
                        if i == 0 or j == 0:
                            K[i][j] = 0
                        elif itemWeight[i-1] <= j:
                            K[i][j] = max(price[i-1] + K[i-1][j - itemWeight[i-1]], K[i-1][j])
                        else:
                            K[i][j] = K[i-1][j]
        maxPrice = K[num][memberWeight[a]]
        priceTotal = priceTotal + maxPrice
        maxIdx = memberWeight[a]
        arr = []
        for k in range(num, 0, -1):
            if maxPrice <= 0:
                break
            if maxPrice == K[k-1][maxIdx]:
                continue
            else:
                arr.append(k)

                maxPrice = maxPrice - price[k-1]
                maxIdx = maxIdx - itemWeight[k-1]
        itemChosen.append(sorted(arr))
    with open("results.txt", "a") as w:
        w.write("Test Case {0}\nTotal Price {1}\n".format(case, priceTotal))
        w.write("Member Items:\n")
        for x in range(len(memberWeight)):
            w.write("{0}: ".format(x+1))
            w.write("{0}\n".format(' '.join(map(str, itemChosen[x]))))
        w.write("\n")

#Opens 'shopping.txt' file 
with open("shopping.txt", "r") as f:
    mylines = []
    file_size = 0
    for i, line in enumerate(f):
        file_size = i
        mylines.append(line.strip())
    mylines.pop(0)
    case = 1
    index = 0
    while index < len(mylines):
        price = []
        weight = []
        family_capacity = []
        item_ea = int(mylines[index])
        index += 1
        for j in range(item_ea):
            item_info = mylines[index].split()
            price.append(int(item_info[0]))
            weight.append(int(item_info[1]))
            index += 1
        family_num = int(mylines[index])
        index += 1
        for k in range(family_num):
            family_capacity.append(int(mylines[index]))
            index += 1
        knapsack(family_capacity, weight, price, item_ea, case)
        case += 1
f.close()
