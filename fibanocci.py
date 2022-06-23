a=int(input("enter the number:"))
n1=0
n2=1
print("{0} ". format(n1))
print("{0} ". format(n2))
for i in range(2,a):
    n3=n1+n2
    print("{0}". format(n3))
    n1= n2
    n2 = n3
