a = int(input("enter the terms"))
f = 0
s = 1
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end="")
    for x in range(2,a):
        d=f+s
        print(d,end="")
        f=s
        s=d
