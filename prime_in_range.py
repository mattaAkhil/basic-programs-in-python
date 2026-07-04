def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
lower=int(input("enter lower limit:"))
upper=int(input("enter upper limit:"))
print(f"prime numbers between {lower} and {upper} are:")
for i in range(lower,upper+1):
    if is_prime(i):
        print(i,end=" ")    