sus
from flask import Flask,request,send_file
app = Flask(__name__)
import sqlite3

user_ = 'nitis'
pass_ = 'pass' 
email_='123'
phone_='123'
status_='...'
qian_=0
daka_=False
database_='.'
x=0
feiyong_=0


@app.route('/e', methods=['GET'])
def hello_world():
  return 'k'

@app.route('/test', methods=['POST'])
def test():
  return 'OK'

@app.route('/register', methods=['POST'])
def register():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    user_=data['user']
    pass_=data['pass']
    email_=data['email']
    phone_=data['phone']
    status_=data['status']
    qian_=data['qian']
    daka_=data['daka']
    print(data)
    conn = sqlite3.connect('testdatabase.db')
    conn.execute("INSERT INTO xiangmu3 (user,pass,email,phone,status,qian,daka) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}','{5}','{6}')".format(user_,pass_,email_,phone_,status_,qian_,daka_))
    conn.commit()
    conn.close
    if data["user"] == user_ and data["pass"] == pass_:
       return {"Status":True}
    else:
       return {"Status":False}
    return {"Status":"test"}
  else:
    return 'Wrong token!'

@app.route('/login', methods=['POST'])
def login():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    user_=data['user']
    pass_=data['pass']
    print(data)
    conn = sqlite3.connect('testdatabase.db')
    c = conn.cursor()
    cursor = conn.execute("SELECT pass,status,qian FROM xiangmu3 WHERE user = '{0}';".format(user_))
    for row in cursor:
        if row[0]==pass_:
          print(row[2])
          return {"statusTrueorFalse":True,"status":row[1],"user":user_,"qian":row[2]}
        else:
          return {"statusTrueorFalse":False} 
    conn.close
  else:
    return 'Wrong token!'


@app.route('/zhufu', methods=['POST'])
def zhufu():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    user_=data["user"]
    daka_=data["daka"]
#    daka_='True'
    conn = sqlite3.connect('testdatabase.db')
    cursor = conn.execute("UPDATE xiangmu3 SET daka='{0}' WHERE user='{1}';".format(daka_,user_))
    conn.commit()
    if data["daka"]==daka_:
       return {"Status":True,"statusTrueorFalse":daka_}
    else:
       return {"Status":False,"statusTrueorFalse":daka_}
    conn.close
  else:
    return 'Wrong token!'


@app.route('/zhufumeitian', methods=['POST'])
def zhufumeitian():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    user_=data["user"]
    daka_=data["daka"]
#    daka_='False'
    conn = sqlite3.connect('testdatabase.db')
    cursor = conn.execute("UPDATE xiangmu3 SET daka='{0}' WHERE user='{1}';".format(daka_,user_))
    conn.commit()
    if data["daka"]==daka_:
       return {"Status":True,"statusTrueorFalse":daka_}
    else:
       return {"Status":False,"statusTrueorFalse":daka_}
    conn.close
  else:
    return 'Wrong token!'


@app.route('/jiaoshuidianfei', methods=['POST'])
def jiaoshuidianfei():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    user_=data["user"]
    qian_=data["qian"]
#    daka_='False'
    conn = sqlite3.connect('testdatabase.db')
    cursor = conn.execute("UPDATE xiangmu3 SET qian='{0}' WHERE user='{1}';".format(qian_,user_))
    conn.commit()
    if True:
       return {"Status":True,"statusTrueorFalse":daka_}
    else:
       return {"Status":False,"statusTrueorFalse":daka_}
    conn.close
  else:
    return 'Wrong token!'

@app.route('/logout', methods=['POST'])
def logout():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    user_=data["user"]
    daka_=data["daka"]
    qian_=data["qian"]
    print(user_)
    print(daka_)
    print(qian_)
    print(data)
    conn = sqlite3.connect('testdatabase.db')
    cursor = conn.execute("UPDATE xiangmu3 SET daka='{0}',qian='{1}' WHERE user='{2}';".format(daka_,qian_,user_))
    conn.commit()
    if data["daka"]==daka_:
       return {"Status":True}
    else:
       return {"Status":False}
    conn.close
  else:
    return 'Wrong token!'

page_=0
@app.route('/submit', methods=['POST'])
def submit():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    database_=data["database"]
    print(data)
    conn = sqlite3.connect('testdatabase.db')
    cursor = conn.execute("INSERT INTO database2 (database) VALUES ('{0}')".format(database_))
    conn.commit()
    if True:
       return {"Status":True}
    else:
       return {"Status":False}
    conn.close
  else:
    return 'Wrong token!'


@app.route('/submitDelete', methods=['POST'])
def submitDelete():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    page_=data["delete"]
    print(data)
    conn = sqlite3.connect('testdatabase.db')
    cursor2=conn.execute("SELECT rowid FROM database3")
    for row in cursor2:
        x=row[0]
    print(x)  
    y=int(x) 
    cursor = conn.execute(" DELETE FROM database2 WHERE rowid='{0}';".format(page_))
    conn.commit()
    a=int(page_)
    if y>a:
      for z in range(a, y+1):
        cursor = conn.execute("UPDATE database2 SET rowid='{0}' WHERE rowid='{1}';".format(z,z+1))
        conn.commit()
    if True:
       return {"Status":True}
    else:
       return {"Status":False}
    conn.close
  else:
    return 'Wrong token!'    

@app.route('/refresh', methods=['POST'])
def refresh():
  hd = request.headers
  if hd["Token"] == "1234567890":
    x=0
    conn = sqlite3.connect('testdatabase.db')
    cursor=conn.execute("SELECT rowid FROM database2")
    for row in cursor:
        x=row[0]
    print(x)  
    y=int(x) 
    return {"page":y}   
    conn.close
  else:
    return 'Wrong token!'


tongzhi_='.'

@app.route('/submitTongzhi', methods=['POST'])
def submitTongzhi():
  hd = request.headers
  if hd["Token"] == "1234567890":
    data = request.json
    x=data["page"]
    conn = sqlite3.connect('testdatabase.db')
    cursor=conn.execute("SELECT database FROM database2 WHERE rowid='{0}'".format(x))
    for row in cursor:
        tongzhi_=row[0]
    print(tongzhi_)  
    return {"text":tongzhi_}
    conn.close   
  else:
    return 'Wrong token!'




@app.route('/getfile', methods=['GET'])
def get_file():
    filename = 'Untitled.png'
    return send_file(filename)



@app.route('/postfile', methods=['POST'])
def post_file():
    data = request.files
    print(data)
    return {"status":"OK"}



if __name__ == '__main__':
  app.run()
