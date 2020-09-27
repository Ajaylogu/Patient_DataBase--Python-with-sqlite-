import sqlite3
con=sqlite3.connect('Covind19Patient.sqlite3')
cur=con.cursor()
sql='''create table if not exists User(id int,name varchar(15),age varchar(15),status varchar(15))'''
cur.execute(sql)
sql='''insert into User(id,name,age,status)values(?,?,?,?)'''
print("////////////////////////")
print("Enter the Required Details\n");
id=int(input("Enter_User_id\n"))
name=input("Enter The name\n")
age=input("Enter The age\n")
status=input("Enter The status Of the Patient")
cur.execute(sql,(id,name,age,status))
con.commit()
cur.execute('''Select *from User''')
row=cur.fetchall()
print("Retrive all the details of user where age is below 18 and affected by Covind19\n")
li=[]
print("id\t\t\tname\t\tage\t\t\tstatus\n")
for j in row:
    l1=list(j)
    if(int(l1[2])<=17):
        if(str(l1[3])=="positive"):
           print(l1[0],end="\t\t\t")
           print(l1[1],end="\t\t\t")
           print(l1[2],end="\t\t\t")
           print(l1[3])
        
print("///////////////////////")
print("Retrive all the details of user where age is above 50 and affected by Covind19\n")
print("id\t\t\tname\t\tage\t\t\tstatus\n")
for j in row:
    l2=list(j)
    if(int(l2[2])>=50):
        if(str(l2[3])=="positive"):
           print(l2[0],end="\t\t\t")
           print(l2[1],end="\t\t\t")
           print(l2[2],end="\t\t\t")
           print(l2[3])
print("///////////////////////")
print("Retrive all negative case")
for j in row:
    l2=list(j)
    if(str(l2[3])=="negative"):
           print(l2[0],end="\t\t\t")
           print(l2[1],end="\t\t\t")
           print(l2[2],end="\t\t\t")
           print(l2[3])
con.close()
