def is_prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
num=int(input())
l1=[]
for k in range(2,num+1):
    if is_prime(k):
        l1.append(k)
def is_sum(l1,num):
    for i in l1:
        for j in l1:
            if i+j==num:
                return i,j
    return 0,0        
a=0
b=0
a,b= is_sum(l1,num)
if a !=0 and b!=0:
    print(f"{a}+{b}={num}")
else:
    print("No such prime numbers found")    
               