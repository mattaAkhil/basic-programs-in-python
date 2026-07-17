import numpy as np
arr=list(map(int,input().split()))
ar=np.array(arr)
print(ar)
high=0
low=99
for i in ar:
    if i>high:
        high=i
    if i<low:
        low=i
print(f"high={high} and low={low}")    
ar1=np.sort(ar)
h1=ar1[-1]
l1=ar1[0]
print(h1,l1)
