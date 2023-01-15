import pymysql as sql

def getConnection():
    conn=sql.connect(host="localhost",port=3307,user="root",database="flask_project")
    return conn

def addData(t):
    conn=getConnection()
    cur=conn.cursor()
    q1="insert into register(email,phoneno,username,password) values(%s,%s,%s,%s)"
    cur.execute(q1,t)
    conn.commit()
    conn.close()