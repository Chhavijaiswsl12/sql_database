import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='admin@123',
    database="a-14(pdbc)"
)

cursor=conn.cursor()

while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by name")
    print("4. Update Student Fees")
    print("5. Delete Student" )
    print("6. Exit")

    choice=int(input("enter the choice"))
    if choice==1:
        sid=int(input("enter the student id"))
        sname=input("enter the student name")
        course=input("enter the student course")
        fees=int(input("enter the student fees"))
        city=input("enter the student city")

        query="insert into student_pdbc values(%s,%s,%s,%s,%s)"
        values=(sid,sname,course,fees,city)
        cursor.execute(query,values)
        conn.commit()
        print("student added successfully")


    if choice==2:
        query="select * from student_pdbc"
        cursor.execute(query)
        data=cursor.fetchall()
        for row in data:
            print(row)

    if choice==3:
        sname=input("enter the student name to search")
        query="select * from student_pdbc where sname=%s"
        values=(sname,)
        cursor.execute(query,values)
        data=cursor.fetchall()
        for row in data:
            print(row)
            
    if choice==4 :




    

