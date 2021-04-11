import mysql
import mysql.connector

def DataUpdate(FirstName, PhoneNumber, EmailID):
    mydb = mysql.connector.connect(
        host= 'localhost',
        user= 'root ',
        passwd= 'root',
        # database='Rasa_database'
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")
    dblist = [ ]
    for x in mycursor:
      dblist.append(x[0])
    
    print(dblist)
    
    if 'Rasa_database' not in dblist:
        mycursor.execute("CREATE DATABASE Rasa_database")

    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="Rasa_database"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    table_list = [ ]
    for x in mycursor:
      table_list.append(x[0])
    
    print(table_list)
    if 'User_info' not in table_list:
        sql = "CREATE TABLE User_info( Personid INTEGER NOT NULL AUTO_INCREMENT, firstName VARCHAR(255), phoNe VARCHAR(255), emailID VARCHAR(255), PRIMARY KEY (Personid))";
        mycursor.execute(sql)        
    
    sql = 'INSERT INTO User_info(firstName , phoNe, emailID) VALUES ("{}", "{}", "{}");'.format(FirstName, PhoneNumber, EmailID)
    mycursor.execute(sql) 

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

if __name__ =="__main__":
    DataUpdate("Mayuri", "9822263", "hjsbh@g.com")