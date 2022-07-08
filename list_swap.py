a=[3,4]
print("old list:")
print(a)
n=len(a)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("swapped list:")
print(a)
