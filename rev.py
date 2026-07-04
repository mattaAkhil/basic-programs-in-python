def rev_fun(n):
    rev=0
    while n!=0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev    
n=int(input("enter a number:"))
reverse=rev_fun(n)
print(f"reverse of {n} is {reverse}")
