n = int(input())
strs = {}
for i in range(0,n):
    temp = input()
    if temp in strs:
        strs[temp] += 1
    else:
        strs[temp] = 1
    
q = int(input())
for i in range(0,q):
    query = input()
    if query in strs:
        print(strs[query])
    else:
        print(0)