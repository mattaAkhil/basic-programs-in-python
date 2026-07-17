n=input("enter string:")
non_repeated=""
for i in range(len(n)):
    count=0
    for j in range(len(n)):
        if n[i]==n[j]:
            count+=1
    if count==1:
        non_repeated+=n[i]
print(non_repeated)
