n,q = map(int,input().split(' '))
lastAns = 0
seqList = [[] for i in range(0,n)]
for i in range(0,q):
    cmd = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    if cmd[0]==1:
        x = cmd[1]
        y = cmd[2]
        ind = (x ^ lastAns)%n
        seqList[ind].append(y)
    else:
        x = cmd[1]
        y = cmd[2]
        ind = (x ^ lastAns)%n
        size = len(seqList[ind])
        itm = seqList[ind][y%size]
        lastAns = itm
        print(lastAns)
        