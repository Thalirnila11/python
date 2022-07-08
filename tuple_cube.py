n=[2,3,4,5]
tuple=[(i,(i*i*i))for i in n]
print("tuple_list:", tuple)    

tuple1=[]
for i in n:
    a=(i,(i*i*i))
    tuple1.append(a)
print("tuple list:",tuple1)
