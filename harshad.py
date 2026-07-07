n=int(input())
def sum(n):
    s=0
    while n!=0:
        r=n%10
        s=s+r
        n=n//10
    return s
print(f"the sum of the digits of {n} is {sum(n)}")    
if n%sum(n)==0:
    print(f"the given number {n} is a harshad number")        
else:
    print(f"the given number {n} is not a harshad number")    