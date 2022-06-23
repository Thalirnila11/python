n=int(input("enter the number:"))
sum=0
temp =n
while(n>0):
    t=n%10
    sum=(sum*10)+t
    n=n//10
print(sum)
if temp==sum:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
