#strong number is a number whose sum of factorial of digits is equal to the number itself
def fact(n):
    if n==0:
        return 1
    else:
        return n* fact(n-1)    
n=int(input())
n1=n
sum=0
while n1!=0:
    r=n1%10
    sum=sum+fact(r)
    n1=n1//10
if sum==n:
    print(f"the given number {n} is a strong number")
else:
    print(f"the given number {n} is not a strong number")
