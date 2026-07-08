#An abundant number is a number where the sum of its proper divisors is greater than the number itself.
n=int(input("enter a number"))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
print(sum)
if sum>n:
    print(f"{n} is an abundant number")
else:
    print(f"{n} is not an abundant number")            