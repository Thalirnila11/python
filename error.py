try:
    print(x)
except:
    print("an expection occur")
    
try:
    a=int(input("enter the numerator:"))
    b=int(input("enter the denominator:"))
    c=a/b
    print("division:{}". format(c))
except:
    print("denominator cannot be 0   TRY AGAIN")
print("programs end")

try:
    n=[2,4,3,5,6,1]
    print("list:",n)
    i=int(input("enter index:"))
print("index of list:",i)
