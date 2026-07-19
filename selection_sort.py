def l_min(l):
    min=l[0]
    for i in l:
        if i<min:
            min=i
    return min
l1=list(map(int,input().split()))
print(f"before sorting:{l1}")
for i in range(len(l1)):
    min_value=l_min(l1[i:])
    min_index=l1.index(min_value)
    l1[i],l1[min_index]=l1[min_index],l1[i]
print(f"after sorting:{l1}")           