from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/home/<string:name>', methods=("GET", "POST"))
def user_name(name):
    if request.method == "POST":
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="python_test_db")
        mycursor = mydb.cursor()
        sqlform = "Insert into test_expenses(months, typeExpense, expense, amount) values(%s, %s, %s, %s)"
        expense1 = [(request.form["months"], request.form["typeExpense"], request.form["expense"], request.form["amount"])]
        mycursor.executemany(sqlform, expense1)
        mydb.commit()
    return render_template('name.html', name = name)

@app.route('/home/no_access')
def no_access():
    return render_template('no_access.html')

@app.route('/expenses')
def all_expenses():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="python_test_db")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from test_expenses")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    return render_template('all_expenses.html', expenses = myresult)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    print(app.url_map)
    app.run(debug = True)

