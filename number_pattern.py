def no(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")

        print("\r")
n=int (input("enter the no.of row:"))
no(n)
