def element(list1,list2):
    result= False
    for x in list1:
        for y in list2:
            if x==y:
                result = True
                return result
            
    return result
a=[4,5,6,7,8]
b=[4,1,2,3,9]
n= element(a,b)
print("whether two list have same element:{}". format(n))
  
