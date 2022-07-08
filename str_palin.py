a=input("enter a string:")
b=''.join(reversed(a))
if(a==b):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
