def lengthFinder(num):
    length = 0
    temp = (1)
    while(num>=temp):
        length+=1
        temp = (temp << 1)
    return length

def bitInsertion(N,M,i,j):
    length = lengthFinder(M)+1
    mask = (-1<<j+1) | ((1<<i)-1)
    print(bin(mask))
    masked = N & mask
    M = M<<i
    return masked | M
result = bitInsertion(1201,8,3,6)
print(result,bin(result))
