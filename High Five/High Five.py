# Time:O(NlogN) S:O(N)
from heapq import _heapify_max, _heappop_max

def topFiveAvg(items):
    scores = {}
    output = []
    for i in items:
        if i[0] in scores:
            scores[i[0]].append(i[1])
        else:
            scores[i[0]] = [i[1]]

    maxSID = 0
    for i in scores:
        maxSID = max(maxSID,i)
    studentIDs = [0]*maxSID
    for score in scores:
        temp = scores[score]
        _heapify_max(temp)
        studentIDs[score-1] =(_heappop_max(temp)+_heappop_max(temp)+_heappop_max(temp)+_heappop_max(temp)+_heappop_max(temp)) //5
    for i in range(len(studentIDs)):
        if studentIDs[i]!=0:
            output.append([i+1,studentIDs[i]])
    return output

def main():
    items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
    print(topFiveAvg(items))
main()
