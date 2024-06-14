import sqlite3
conn = sqlite3.connect('test.db')
print("success")

conn.execute("INSERT INTO TEACHERS VALUES(1,'CAROLYNE','KWAMBOKA',20,56000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'JOB','ONDARA',22,53000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'JAMES','KARIOKI',36,59000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'RUTH','KERUBO',42,60000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'ANN','KEMUMA',50,70000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'LINDA','ACHIENG',40,100000.00)")

conn.commit()
print("successfuly inserted records")
conn.close()
