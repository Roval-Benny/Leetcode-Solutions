#T:O(N) S:O(D) D - depth of tree

def nestedListWeightSum(arr,depth=1):
    sumValue = 0
    for i in arr:
        if type(i) == type(1):
            sumValue+=(i*depth)
        else:
            sumValue+=(nestedListWeightSum(i,depth+1))
    return sumValue

def main():
    arr = [1,[4,[6]]]
    print(nestedListWeightSum(arr))
main()
