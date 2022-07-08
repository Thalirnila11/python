 def string(str1,substr):
    a=str1.split()
    count=0
    for i in range(0,len(a)):
        if(substr==a[i]):
            count=count+1
    return count
str1=input("enter your string:")
substr=input("enter your substring:")
b=string(str1,substr)
print("how many times substring prsent:{}".format(b))
