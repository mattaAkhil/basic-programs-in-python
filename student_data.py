n=int(input("enter no of students:"))
students=[]
for i in range(n):
    stu_roll=int(input(f"enter roll_no of student {i+1}:"))
    stu_name=input(f"enter name of student {i+1}:")
    section=input(f"enter the section of student{i+1}:")
    marks=[]
    subs=["c","java","python","html","css"]
    for k in subs:
        m=int(input(f"enter marks in {k}:"))
        marks.append(m)
    total=0    
    for j in marks:
        total+=j
    students.append({
        "roll":stu_roll,
        "name":stu_name,
        "section":section,
        "marks":marks,
        "total":total
    })

def who_is_topper(students):
    topper =students[0]
    for stu in students:

        if stu["total"]>topper["total"]:
            topper=stu
    print(f"topper:{topper["name"]}")        

def above_75(students):
    above=[]
    for student in students:
        if student["total"]>375:
           above.append(student["name"]) 
    print("students scored above 75%:")        
    for i in above:
        print(i) 

def display(students):
    print("roll_no\tname\tsection\tc\tjava\tpython\thtml\tcss\t")
    for student in students:
        print(
            student["roll"],
            student["name"],
            student["section"],
            *student["marks"],
            sep="\t"
        )  
ex=0
while ex==0:
    print("1.topper 2.above 75 3.display 4.exit")
    n=int(input("enter your choice:"))
    if n==1:
        who_is_topper(students)
    elif n==2:
        above_75(students)
    elif n==3:
        display(students)
    elif n==4:
        ex=1
    else:
        print("wrong input try again")            




