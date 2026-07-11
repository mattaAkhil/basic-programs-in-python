def is_palindrome(n):
    n1=n
    n=abs(n)
    re=0
    while n!=0:
        r=n%10
        re=re*10+r
        n=n//10
    if n1<0:
        re=-re    
    if n1==re:
        return True
    else:
        return False 
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
for j in l:
    if is_palindrome(j):
        print("YES")
    else:
        print("NO")
                       