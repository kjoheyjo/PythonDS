d,m,y = input().strip().split(' ')
d,m,y = [int(d),int(m),int(y)]

dd,mm,yy = input().strip().split(' ')
dd,mm,yy = [int(dd),int(mm),int(yy)]
fine = 0
if y>yy:
    fine = 10000
elif y<yy:
    fine = 0
else:
    if m>mm:
        fine = (m-mm)*500
    elif m<mm:
        fine = 0
    else:
        if d>dd:
            fine = (d - dd)*15


print(fine)