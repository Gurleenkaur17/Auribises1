from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from datatry import DB
import matplotlib.pyplot as plt
mydb = mysql.connector.connect(user = 'root', password = 'Gurleen@123', host = '127.0.0.1', database = 'project')
cursor = mydb.cursor()
app = Flask(__name__)
my_db = DB()
@app.route('/')
def front():
    return render_template("front_page.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/success', methods = ["POST", "GET"])
def success():
    user = {
        "name": request.form['name'],
        "age": request.form['age'],
        "gender": request.form['gender'],
        "class": request.form['class'],
        "school": request.form['school'],
        "phone_number": request.form['phone number'],
        "password": request.form['password']
    }

    print(user)
    sql = "insert into didactic values('{name}', '{age}', '{gender}', '{class}', '{school}', '{phone_number}', '{password}')".format_map(user)
    my_db.execute_sql_query(sql)
    # print(register)

    return render_template("success.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/graph')
def graph():
    cursor.execute("select school as school_name, count(*) as count from didactic group by school")
    result = cursor.fetchall
    School = []
    Count = []

    for i in cursor:
        School.append(i[0])
        Count.append(i[1])

    print("Names of School = ", School)
    print("Count of Schools = ", Count)

    # Visulizing Data using Matplotlib
    plt.bar(School, Count)
    plt.ylim(0, 20)
    plt.xlabel("Names of School")
    plt.ylabel("Count of Schools")
    plt.title("School's Information")
    plt.show()
    return render_template("courses.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/auth', methods=["POST", "GET"])
def authenticate_user():
    error = None
    if request.method == 'POST':
        uname = request.form.get('name')
        upassword = request.form.get('password')
        query = "select * from didactic where name = %s AND password = %s"
        cursor.execute(query, (uname, upassword))
        Rows = cursor.fetchall()
        countrows = cursor.rowcount
        if countrows<1:
            return render_template("error.html")
        else:
            return render_template("auth.html")




def main():
    app.run(debug = True)

if __name__ == '__main__':
    main()
    """ name = request.form['name']
        class1 = request.form['class']
        school = request.form['school']
        email = request.form['email']
        password = request.form['password']
        print(name, class1, school, email, password)"""