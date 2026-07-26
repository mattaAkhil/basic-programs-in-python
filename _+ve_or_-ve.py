n=int(input())
if n>0:
    print("positive")
else:
    print("negative")    

n=int(input("enter of students:"))
students=[]
for i in range(n):
    roll_no=input(f"enter roll-no of student{i+1}:")
    name=input("enter name:")
    sub_marks=list(map(int,input("enter marks of 5 subjects:").split()))
    total=0
    for j in sub_marks:
        total+=j
    students.append({
        "roll_no":roll_no,
        "name":name,
        "sub_marks":sub_marks,
        "total":total
    })
for i in students:
    topper=students[0]
    if i["total"]>topper["total"]:
        topper=i
print("topper:",topper["name"])          
print("Roll_no\tName\ts1\ts2\ts3\ts4\ts5\ttotal")
for student in students:   
    print(
        student["roll_no"],
        student["name"],
        *student["sub_marks"],
        student["total"],
        sep="\t"
    ) 
