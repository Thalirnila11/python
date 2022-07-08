def remove(str,i):
    a=str[:i]
    b=str[i+1:]
    return a+b
s=input("enter the string:")
i=int(input("enter the ith index:"))
remove(s,i-1)
print("removed string:",remove(s,i-1))
#when we declare i=3 it takes it remove 4 th element to remove 3rd element we define it as i-1
