## STUDENT DATABAS
students = {}

## Add A Student To List
def add_student():
    global students
    student_id = input("__Enter Student ID :")
    student_name = input("__Enter Student Name :")
    student_age = input("__Enter Student Age :")
    student_grade = input("__Enter Student Grade :")
    students[student_id]={
        "name":student_name,
        "age":student_age,
        "grade":student_grade}
    print("__Student Added Successfully__")

## Remove A Student From List
def remove_student():
    global students
    student_id = input("__Enter Student ID To Remove:")
    if student_id in students:
        del students[student_id]   
        print("__Student ID Remove Successfully__")
    else:
        print("__Student not found__")     
        
## Update Student Information from List     
def update_student():
    global students
    student_id = input("__Enter Student ID To Update:")
    if student_id in students:
        student_name = input("__Enter Student Name To Update:")
        student_age = input("__Enter Student Age To Update:")
        student_grade = input("__Enter Student grade To Update:")
        print("__Student Information Updated Successfully__")
    else:
        print("__Student Name Not Present In Students__")
        
## Define A Main Function
def main():
    print("__Welcome__")
    while True:
        print("1:Add Student__")
        print("2.Remove Student__")
        print("3.Update Student__")
        choice=input("Enter Your Choice:")
        if choice=="1":
            add_student()
        if choice=="2":
            remove_student()
        if choice=="3":
            update_student()
            
main()
            