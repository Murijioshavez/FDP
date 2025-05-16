a=0
b=10
while a <=b:
    print(a)
    a+=1
    print(a) if a == b else None
    if a == b:
        for i in range(b, -1, -1):
            print(i)
        break

