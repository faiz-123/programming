import sqlite3



def connect():
    conn=sqlite3.connect("business.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXIST data (id INTEGER PRIMARY KEY , name TEXT , date TEXT , total INTEGER , mo_no INTEGER)")
    conn.commit()
    conn.close()

def insert(name,date,total,mo_no):
    conn=sqlite3.connect("business.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO data VALUE (NULL, ?,?,?,?)",(name,date,total,mo_no))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("business.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")
    row = cur.fetchall()
    conn.close()
    return row


def search(name="",date="",total="",mo_no=""):
    conn=sqlite3.connect("business.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM data WHERE name=? or date=? or total=? or mo_no=?",(name,date,total,mo_no))
    row = cur.fetchall()
    conn.close()
    return row


def delete(id):
    conn=sqlite3.connect("business.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM data WHERE id=?",(id))
    cur.commit()
    conn.close()        

def update(id,name,date,total,mo_no):
    conn=sqlite3.connect("business.db")
    cur = conn.cursor()
    cur.execute("UPDATE data SET name=?, date=?, total=?, mo_no=?, id=?",(name,date,total,mo_no,id))
    conn.commit()
    conn.close()
    



    

