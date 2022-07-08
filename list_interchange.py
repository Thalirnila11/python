a=[34,56,78,90,45,3]
print("old list:{}". format(a))
n=len(a)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("interchanged list:{}". format(a))
