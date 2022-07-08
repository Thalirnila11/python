list=[[3,4,5],[7,6,8],[2,9,3],[1,3,4]]
print("input:{}". format(list))
result={list[0][ele]:list[ele + 1] for ele in range(len(list)-1)}
print("output:{}". format(result))
