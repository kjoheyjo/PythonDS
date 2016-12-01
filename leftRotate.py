n,d = map(int,input().split())
arr = [int(temp) for temp in input().split(' ')]
l = []
for i in range(0,n):
    ind = (i + d)%n
    print(arr[ind],end=' ')
      
       