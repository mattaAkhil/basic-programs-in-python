def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
rows=int(input("enter no of rows"))
for n in range(rows):
    print((rows-n)*" ",end="")
    for r in range(n+1):
        ncr=fact(n)//((fact(r)*fact(n-r)))    
        print(ncr,end=" ")
    print() 

#n = int(input("enter no of rows:"))
#res = [[1]]
#for i in range(n - 1):
    #temp = [0] + res[-1] + [0]
    #row = []
    #for j in range(len(res[-1]) + 1):
     #res.append(row)

# Print Pascal's triangle centered as a triangle
#max_width = len(" ".join(str(x) for x in res[-1]))
#for row in res:
    #line = " ".join(str(x) for x in row)
   # print(line.center(max_width))               