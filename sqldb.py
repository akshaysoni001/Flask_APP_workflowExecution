import sqlite3

def execute():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")
    conn.execute('CREATE TABLE workflow (id int, name TEXT, company TEXT, city TEXT)')
    print("Table created successfully")
    conn.close()

def create_sample():
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (1,'Akshay','Opcito','Pune')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (2,'Arpit','Opcito1','Pune')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (3,'Ankita','Opcito22','Pune')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (2,'Aash','Amdocs','Pune')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (1,'Ankit','Wipro','Mumbai')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (6,'Arun','Opcito','Pune')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (2,'Shreyas','Zensar','Banglore')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (8,'Sunil','Opcito','Mumbai')")
        cur.execute("INSERT INTO workflow (id,name,company,city) VALUES (1,'Arshad','Opcito','US')")
            
        con.commit()
        msg = "Record successfully added"
        print("Record successfully added")
# execute()
create_sample()

