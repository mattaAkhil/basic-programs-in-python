a=int(input("enter first number"))
b=int(input("enter second number"))
def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//hcf(a,b)
print(f"hcf of {a} and {b} is {hcf(a,b)}")
print(f"lcm of {a} and {b} is {lcm(a,b)}")            