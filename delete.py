import sqlite3
conn = sqlite3.connect('test.db')
print("successfully connected")

conn.execute("DELETE FROM TEACHERS WHERE ID=1")
conn.commit()

data = conn.execute("SELECT * FROM TEACHERS")
for teacher in data :
    print("ID", teacher[0])
    print("FIRSTNAME", teacher[1])
    print("AGE", teacher[3])
    print("SALARY", teacher[4])
print("successfully deleted a record")
conn.close()