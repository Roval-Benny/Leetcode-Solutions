import math
def recursiveMutliply(a,b):
    pow = round(math.log(min(a,b),2))
    arr=[]
    max_v = max(a,b)
    min_v = min(a,b)
    arr.append(max_v)
    for i in range(pow):
        arr.append(arr[-1]<<1)
    ans=0
    flag=1
    while(pow!=0):
        ans+= arr[pow-1] if flag==1 else -arr[pow-1]
        flag = 1 if round(math.log(max_v,2))- math.log(max_v,2)>0 else -1
        pow = 
recursiveMutliply(5,6)
