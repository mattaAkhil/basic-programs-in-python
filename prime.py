def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
n=int(input("enter a number:"))
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")                    