# T:O(1) S:O(1)
def binaryToString(num):
    if num>=1 and num<=0:
        return "ERROR"
    s = "."
    while(num>0):
        if len(s)>32:
            return s
        r = num*2
        if r>=1:
            s+="1"
            num=r-1
        else:
            s+="0"
            num=r
    return s

print(binaryToString(0.246))
