n=int(input("enter a number:"))
arm=0
temp=n
while n>0:
    n=n%10
    arm=arm+n**3
    n=n/10

if temp==arm:
    print("armstrong number")
else:
    print("not a armstrong number")
