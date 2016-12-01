n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,input().split())
a = list(a)
arr = [0 for i in range(0,n)]
for i in range(0,n):
    ind = (n + (i - k))%n
    arr[ind] = a[i]
    
print(*arr, sep=" ")

