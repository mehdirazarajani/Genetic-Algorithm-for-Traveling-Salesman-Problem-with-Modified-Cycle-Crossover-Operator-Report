def fillNoneWithSwappedValue(arr1 ,arr2 ,final1 ,final2 ):
    for a in range(0,arr1.__len__()):
        if final1[a] == None:
            final1[a] = arr2[a]
        if final2[a] == None:
            final2[a] = arr1[a]
    return final1,final2

def indexOf(arr,x):
    for a in range(0,arr.__len__()):
        if arr[a] == x:
            return a
    return -1


def crossoverOperator( parent1, parent2 ):
    offspring1 = [None] * parent1.__len__()
    offspring2 = [None] * parent2.__len__()
    size1 = 1
    size2 = 1

    initalSelected = parent1[0]
    offspring1[0] = parent1[0]
    latestUpdated2 = parent2[0]
    check = 1

    while size1 < parent1.__len__() or size2 < parent2.__len__():
        if latestUpdated2 == initalSelected:
            index2 = indexOf(parent2,latestUpdated2)
            offspring2[index2] = parent2[index2]
            ans1,ans2 = fillNoneWithSwappedValue(parent1, parent2, offspring1, offspring2)
            offspring1 = ans1
            offspring2 = ans2
            size1 = parent1.__len__()
            size2 = parent2.__len__()
            check = 0
        else:
            index2 = indexOf(parent2,latestUpdated2)
            offspring2[index2] = parent2[index2]
            size2 += 1
            index1 = indexOf(parent1,parent2[index2])
            offspring1[index1] = parent1[index1]
            size1 += 1
            latestUpdated2 = parent2[index1]
    if check:
        index2 = indexOf(parent2, latestUpdated2)
        offspring2[index2] = parent2[index2]
    return offspring1,offspring2

def findUnusedIndexValues(parent,offspring):
    res = list()
    for a in parent:
        if indexOf(offspring,a) == -1:
            res.append(a)
    return res

def crossoverOperator2( parent1, parent2 ):
    print('hellol shakoob')
    offspring1 = [None] * parent1.__len__()
    offspring2 = [None] * parent2.__len__()
    i1 = 0
    i2 = 0
    initalSelected = parent1[0]
    offspring1[i1] = parent2[0]
    i1 += 1
    # latestUpdated2 = parent2[0]
    check = 1

    while i1 < parent1.__len__() and i2 < parent2.__len__():
        index1 = indexOf(parent1,offspring1[i1-1])
        index1 = indexOf(parent1,parent2[index1])
        latestUpdated2 = parent2[index1]
        if latestUpdated2 == initalSelected:
            offspring2[i2] = latestUpdated2
            i2 += 1
            # print("cycle detected")
            check = 0
            res1 = findUnusedIndexValues(parent1,offspring1)
            res2 = findUnusedIndexValues(parent2,offspring2)
            # print(res1,res2)
            ans1,ans2 = crossoverOperator2(res1, res2)
            offspring1[i1:] = ans1
            offspring2[i2:] = ans2
            check = 0
            break
        else:
            offspring2[i2] = parent2[index1]
            i2 += 1
            index1 = indexOf(parent1,offspring2[i2-1])
            offspring1[i1] = parent2[index1]
            i1 += 1
    if check:
        index1 = indexOf(parent1, offspring1[i1 - 1])
        index1 = indexOf(parent1, parent2[index1])
        latestUpdated2 = parent2[index1]
        offspring2[i2] = latestUpdated2
        i2 += 1
    return offspring1,offspring2



def main():
    # ans = crossoverOperator([1,2,3,4,5,6,7,8],[8,5,2,1,3,6,4,7])
    # ans = crossoverOperator([3,4,8,2,7,1,6,5],[4,2,5,1,6,8,3,7])

    ans1,ans2 = crossoverOperator2([3,4,8,2,7,1,6,5],[4,2,5,1,6,8,3,7])
    print(ans1)
    print(ans2)

    ans1, ans2 = crossoverOperator2([1,2,3,4,5,6,7,8],[2,7,5,8,4,1,6,3])
    print(ans1)
    print(ans2)

    ans1, ans2 = crossoverOperator2([1,2,3,4,5,6,7,8,9,10,11,12,13,14],[2,7,5,8,4,1,6,3,14,13,10,11,12,9])
    print(ans1)
    print(ans2)

if __name__ == '__main__':
    main()