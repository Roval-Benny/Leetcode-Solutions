# T:O(N) S:O(1)

def getNext(num):
    temp = num
    count0 = 0
    count1 = 0
    
    while((temp & 1)==0 and temp!=0):
        count0 +=1
        temp = temp>>1
        
    while((temp & 1)==1):
        count1 +=1
        temp = temp>>1
        
    if count0+count1 == 31 or count0 + count1 ==0:
        return -1
    
    return num + (1<<count0) + (1<<(count1-1)) -1
    
def getSmall(num):
    temp = num
    count0 = 0
    count1 = 0
    
    while((temp & 1)==1):
        count1+=1
        temp>>=1
        
    if temp==0:
        return -1
        
    while((temp & 1)==0 and temp!=0):
        count0+=1
        temp>>=1
        
    return num - (1<<count1) - (1<<(count0-1)) +1
    
def main():
    num = 192
    print(bin(num))
    print(getNext(num),bin(getNext(num)))
    print(getSmall(num),bin(getSmall(num)))
    
main()
        
    