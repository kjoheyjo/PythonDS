n = int(input())
phonebook = {}
while(n):
    name,number = input().strip().split(' ')
    phonebook[name] = number
    n = n - 1
s = input()
while True: 
    if s=="":
        break
    else:
        if s not in phonebook:
            print("Not found")
        else:
            num = phonebook.get(s)
            print("%s=%s" %(s,num))
    s = input()
    