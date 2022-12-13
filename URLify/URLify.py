'''
Time Complexity O(N) Space Complexity O(1)
'''
def URL(string,size):
    size-=1
    pos = len(string)-1
    string=list(string)
    print(string)
    while(size>-1 and pos>-1):
        if string[size]==' ':
            string[pos] = '0'
            pos-=1
            string[pos]='2'
            pos-=1
            string[pos]= '%'
        else:
            string[pos] = string[size]
        size-=1
        pos-=1
    if size==-1 and pos==-1:
        return ''.join(string)
    return 'Invalid url'

print(URL('Roval Benny Puthu para      ',22))
