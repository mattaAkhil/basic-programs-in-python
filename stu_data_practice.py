students=[]
def insert_stu(students):
    name=input("enter name:")
    roll=input("enter roll no:")
    section=input("enter section:")
    marks=list(map(int,input("enter all subs marks:").split()))
    total=0
    for i in marks:
        total+=i
    if 400<=total<=499:
        grade="A"
    elif 300<total<=399:
        grade="B"
    elif 200<total<=299:
        grade="C"
    elif 100<total<=199:
        grade="D"
    else:
        grade="E"                    
    students.append({
        "name":name,
        "roll":roll,
        "section":section,
        "marks":marks,
        "total":total,
        "grade":grade
    })
def who_is_topper(students):
    topper=students[0]
    for student in students:
        if topper["total"]<student["total"]:
            topper=student
    print(topper["name"]," is the topper")        
def total_avg(students):
    sum=0
    for stu in students:
        sum+=stu["total"] 
    avg=sum//len(students) 
    print("avg:",avg)
def show_data(students):
    print("Name\troll\tsection\tsub1\tsub2\tsub3\tsub4\tsub5\ttotal\tgrade")
    for student in students:
        print(
            student["name"],
            student["roll"],
            student["section"],
            *student["marks"],
            student["total"],
            student["grade"],
            sep="\t"
        ) 
ex=0                        
while ex<=0:
    print("1.insert students\n2.show in table format\n3.show topper\n4.find avg of total\n5.exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        insert_stu(students)
    if choice==2:
        show_data(students)
    if choice==3:
        who_is_topper(students)
    if choice==4:
        total_avg(students)
    if choice==5:
        ex=1