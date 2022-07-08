#sort by value
a={1:34,2:78,3:23}
sort=sorted(a. values())
b={}
for i in sort:
    for j in a.keys():
        if a[j]==i:
            b[j]=a[j]
            break
print(b)


#sort by key
b={2:89,3:23,1:11}
print(sorted(b.items()))
