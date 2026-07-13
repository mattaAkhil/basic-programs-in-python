len=int(input("enter length"))
breadth=int(input("enter breadth"))
for i in range (0,len):
    for j in range(0,breadth):
        if (i==0 or i==len-1 or j==0 or j==breadth-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")           
    print()        