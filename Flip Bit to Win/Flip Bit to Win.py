'''
You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of ls you could create.
EXAMPLE
Input: 1775  (or: 11011101111) 
Output: 8

Input: 12
Output: 3

Input:15
Output: 5

Input: 71
Output: 4
'''
# T:O(N) S:O(1)
def flipBitToWin(num):
    temp = 1
    current = 0
    prev = 0
    result = 0
    num = abs(num)
    while(temp<num):
        if ((temp & num) == 0):
            result = max(result,current+prev+1)
            prev = current
            current = 0
        else:
            current+=1
        temp=temp<<1
    return max(result,current+prev+1)
print(flipBitToWin(7))



# To Find Length Convert to string T:O(N) S:O(N)
def counter(num):
    string = bin(num)
    count = []
    print(string)
    temp = 0
    for i in string:
        if i=='1':
            temp+=1
        else:
            if temp!=0 or len(count)!=0:
                count.append(temp)
            temp = 0
    if temp!=0:
        count.append(temp)
    print(count[::-1])
    return count[::-1]

def flipBitToWinSpaceN(num):
    flipper = 1
    count = counter(num)
    result = 0
    index = 0
    while(flipper<=num):
        temp = num | flipper
        if temp>num:
            if index+1<len(count):
                result = max(result, count[index]+count[index+1]+1)
                index+=1
            else:
                return max(result,count[-1]+1)
        flipper = flipper<<1
    if result == 0:
        return count[index]+1
    return result


