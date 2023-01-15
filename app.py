from flask import Flask, redirect, render_template
from flask import request

from dbms import addData
app=Flask(__name__)

#1st Routing
@app.route("/")
def homeFunction():
    return render_template("home.html")

@app.route("/reglink")
def regFunc():
    return render_template("register.html")

@app.route("/savelink", methods=['POST'])
def saveFunction():
    emailid=request.form['email']
    phoneno=request.form['PhoneNo']
    username=request.form['username']
    password=request.form['password']
    t=(emailid,phoneno,username,password)
    addData(t)
    return redirect("/reglink")



@app.route("/loginlink")
def loginFunc():
    return render_template("login.html")

@app.route("/displaylink")
def displayFunc():
    return render_template("display.html")

if __name__=="__main__":
    app.run(debug=True)