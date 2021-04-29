import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306',
                                     user='root', password='vaibhav9221', database='python_test')

        query = 'create table if not exists user(user_ID int primary key,userName varchar(20),Phone varchar(20))'
        cur = self.con.cursor()
        cur.execute(query)
        print("CREATED")

    # Insert
    def insert_user(self, userid, username, phone):
        query = "insert into user(user_ID,userName,Phone) values({},'{}','{}')".format(
            userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("DATA INSETERD")

    def fetchAll(self):
        a = "select * from user"
        cur = self.con.cursor()
        cur.execute(a)
        print("***********ALL DATA************")
        for i in cur:
            
            print("userId :", i[0])
            print("userName :", i[1])
            print("Phone :", i[2])
            print("*****************************")
            

    def deleteData(self, userid):
        query = "delete from user where user_Id= {}".format(userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("DATA DELETED")

    def updateTable(self, userid, username):
        query = "update user set userName ='{}' where user_ID={}".format(
            username, userid)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("DATA UPDATED")

    def Alter(self):
        query = " A user_ID  TO used_ID;"
        cur = self.con.cursor()

        cur.execute(query)

        print("column name changed")


