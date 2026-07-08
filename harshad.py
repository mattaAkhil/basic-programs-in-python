#sum of the digits is divisible by number itself
def sum(n):
    s=0
    while n!=0:
        r=n%10
        s+=r
        n=n//10
    return s    
n=int(input("enter a number"))
if n%sum(n)==0:
    print(f"{n} is a harshad number")
else:
    print(f"{n} is not a harshad number")    