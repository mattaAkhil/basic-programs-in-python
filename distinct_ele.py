import numpy as np
arr=np.array(list(map(int,input().split())))
unq=[]
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count+=1
    if count==1:
        unq.append(arr[i])     
print(len(unq))                