a=int(input("enter any year:"))
if(a%400==0)or (a%100!=0)and (a%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year")
