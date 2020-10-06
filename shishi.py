# from flask import Flask
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'mathus159357'
# app.config['MYSQL_DB'] = 'MyDB'

# mysql = MySQL(app)

# # @app.route('/earth',method=['GET'])
# # def index():
# #     curr=mysql.connection.cursor()
# #     curr.execute('''CREATE TABLE example (id INTEGER,name VARCHAR(20))''')
# #     mysql.connection.commit()
# #     curr.close()
# #     return 'Done'

# @app.route('/')
# def hello():
#     return 'Hello World'

# if __name__ == '__main__':
#   app.run(port=200)









from flask import Flask, send_file, request, render_template
from flask_mysqldb import MySQL
# import  requests


# Create the application instance
app = Flask(__name__, template_folder="templates")

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'mathus159357'
# app.config['MYSQL_DB'] = 'MyDB'

# mysql = MySQL(app)



# Create a URL route in our application for "/"
@app.route('/')
def hello():
    return 'Hello World'


@app.route('/test',methods=['GET','POST'])
def test():
    if request.method=='POST':
        print("POST_____________")
        reply = {"test":"OK POST"}
        r = request.body
        print(r)
    if request.method=='GET':
        print("GET_____________")
        reply = {"test":"OK GET"}
    return reply
    



if __name__ == '__main__':
    # app.run(port=200)     #localhost:200/
    app.run(debug=True)     #localhost:5000/
