import math
def recusiveMult(a,b):
    ans = 0
    while a>=0:
        nearestMult2 = math.log(a,2)
        print(a,nearestMult2,1<<round(nearestMult2))
        ans = ans+ b<< round(nearestMult2) if nearestMult2> round(nearestMult2) else ans - b<<round(nearestMult2)
        a-= (1<<round(nearestMult2))
        
    return ans
print(recusiveMult(11,14))
    
    
