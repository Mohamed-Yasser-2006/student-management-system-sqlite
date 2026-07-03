import sqlite3
conn=sqlite3.connect("Student.db")
cursor=conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER,
grade INTEGER)
""")
conn.commit()
conn.close()
def add_student():
    name=input("Enter Name: ")
    age=int(input("Enter Age: "))
    grade=int(input("Enter Grade: "))
    conn=sqlite3.connect("Student.db")
    cursor=conn.cursor()
    cursor.execute("""
    INSERT INTO students (name,age,grade)
    VALUES (?,?,?)""",(name,age,grade))
    conn.commit()
    conn.close()
    print("Added Successfully")
def show_students():
    conn=sqlite3.connect("Student.db")
    cursor=conn.cursor()
    cursor.execute("""
    SELECT * FROM students
    """)
    students=cursor.fetchall()
    if not students:
        print("No Student")
    else:
        for student in students:
            print("ID: ",student[0])
            print("Name: ",student[1])
            print("Age: ",student[2])
            print("Grade: ",student[3])
            print("-"*20)
            print()
    conn.close()
def search_student():
    search_id=int(input("Enter ID: "))
    conn=sqlite3.connect("Student.db")
    cursor=conn.cursor()
    cursor.execute("""
    SELECT * FROM students
    WHERE id=?""",(search_id,)
    )
    student=cursor.fetchone()
    if not student:
        print("Student Not Found")
    else:
        print("ID: ",student[0])
        print("Name: ",student[1])
        print("Age: ",student[2])
        print("Grade: ",student[3])
    conn.close()
def update_student():
    update_id=int(input("Enter ID: "))
    update_name=input("Enter Name: ")
    update_age=int(input("Enter Age: "))
    update_grade=int(input("Enter Grade: "))
    conn=sqlite3.connect("Student.db")
    cursor=conn.cursor()
    cursor.execute("""
    UPDATE students
    SET name=?,
        age=?,
        grade=?
    WHERE id=?""",(update_name,update_age,update_grade,update_id)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("Updated Successfully")
    else:
        print("Student Not Found") 
    conn.close()
def delete_student():
    delete_id=int(input("Enter ID: "))
    conn=sqlite3.connect("Student.db")
    cursor=conn.cursor()
    cursor.execute("""
    DELETE FROM students
    WHERE id=?""",(delete_id,)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("Deleted Successfully")
    else:
        print("Student Not Found")
    conn.close()
def count_students():
    conn=sqlite3.connect("Student.db")
    cursor=conn.cursor()
    cursor.execute("""
    SELECT COUNT(*) FROM students
    """)
    result=cursor.fetchone()
    print("Students Count: ",result[0])
    conn.close()
while True:
    print("1-Add Student")
    print("2-Show Students")
    print("3-Search Student By ID")
    print("4-UPdate Student")
    print("5-Delete Student")
    print("6-Count Students")
    print("7-Exit")
    
    choice=input("choose: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
        print("-"*20)
    elif choice == "3":
        search_student()
        print("-"*20)
    elif choice == "4":
        update_student()
        print("-"*20)
    elif choice == "5":
        delete_student()
        print("-"*20)
    elif choice == "6":
        count_students()
        print("-"*20)
    elif choice == "7":
        print("Good Bye")
        break
    else:
        print("Invalid choice")