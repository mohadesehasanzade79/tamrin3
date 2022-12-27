a,b,c=int(input("a:")),int(input("b:")),int(input("c:"))
delta=((b**2)-4*a*c)
print("")
print("delta={}".format(delta))
if delta>=0:
    x1=(-b+(delta**0.5))/(2*a)
    x2=(-b-(delta**0.5))/(2*a)
    print("x1={}".format(x1))
    print("x2={}".format(x2))
else:
    print("error:delta<0")
    exit()