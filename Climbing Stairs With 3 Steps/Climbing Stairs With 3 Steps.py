'''Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.'''

#Time:O(N) S:O(N)
def climbStairs(n):
    if n<=2:
        return n
    arr = [0]*(n+1)
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4,n+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    return arr[-1]

print(climbStairs(5))
