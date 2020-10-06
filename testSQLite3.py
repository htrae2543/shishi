import sqlite3
conn = sqlite3.connect('testdatabase.db')
c = conn.cursor()

user_ = 'earth'
#print(type(user_))
pass_ = 'pass' 
email_='123'
phone_='123456'
#print(type(phone_))
status_='刘小明'
daka_=False
qian_=60

# Create table
c.execute('''CREATE TABLE database3
             (database text PRIMARY KEY,other text)''')

#cursor = conn.execute("UPDATE xiangmu3 SET daka='{0}',qian='{1}' WHERE user='{2}';".format(daka_,qian_,user_))
#conn.commit()

#c = conn.cursor()   
#cursor = conn.execute("UPDATE xiangmu3 SET daka='{0}' WHERE user='{1}';".format(daka_,user_))
#conn.commit()
#c.execute("UPDATE settings SET (?) WHERE name=?",(title, LL, LR, RL, RR, distanceBack, title))
#conn.commit()
#c.execute("UPDATE settings SET (title=?,LL=?,LR=?,RL=?,RR=?,distanceBack=?) WHERE name=?",(title, LL, LR, RL, RR, distanceBack, title))

#c.execute("UPDATE xiangmu3 SET daka='true' WHERE user'?'",(user_))
#conn.commit()

# conn.execute("INSERT INTO xiangmu (user,pass,email,phone,status) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(user_,pass_,email_,phone_.status_))

#conn.execute("INSERT INTO xiangmu (user,pass,email,phone,status) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(user_,pass_,email_,phone_,status_))
# c.execute("INSERT INTO xiangmu  VALUES (?,?,?,?,?);",(user_,pass_,email_,phone_,status_))
#conn.commit()

#cursor = connection.cursor()
#        mySql_insert_query = """INSERT INTO xiangmu (user, pass, email,phone,status) 
#                                VALUES (%s, %s, %s, %s,%s) """#

#       recordTuple = (user_, pass_, email_, phone_,status_)
#        cursor.execute(mySql_insert_query, recordTuple)
#        connection.commit()
#        print("Record inserted successfully into Laptop table")
# listt = conn.execute('SELECT email FROM contacts where contact_id = 100;')
# print(listt)


#cursor = conn.execute("SELECT database FROM database ")
#cursor2=conn.execute("SELECT rowid FROM database WHERE rowid='{0}'".format(3))
#for row in cursor2:
#    print("row",row)
#    print("PackageData = ",row[0])
#for row in cursor:
#    print("row",row)
#    print("PackageData = ",row[0]) 

#x=''
#cursor=conn.execute("SELECT rowid FROM database")
#print(x)
#for row in cursor:
#    x=row
#    print(x)
#print(x)  