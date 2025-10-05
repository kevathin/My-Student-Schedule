from flask import Flask, render_template, request
from utils.auth import authUser, authKeyCheck
from utils.dbManager import dbChecker
app = Flask(__name__)

@app.route('/')
def index():
    dbChecker()
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template("register.html")

@app.route('/WorkSpace/', methods=['POST', 'GET'])
def accessWorkSpace():
    error = None
    if request.method == 'POST':
        authKey = authUser(request.form['username'], request.form['password'])
        if  authKey != "failure":
            return studentHome(authKey)
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/WorkSpace/StudentHome', methods=['POST', 'GET'])
def studentHome():
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) == True:
            return render_template('SH.html', authKey = authKey)
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)

def studentHome(authKey):
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) == True:
            return render_template('SH.html', authKey = authKey)
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)

@app.route('/WorkSpace/StudentRegister', methods=['POST', 'GET'])
def studentRegister():
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) == True:
            return render_template('SH.html', authKey = authKey)
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)
        
@app.route('/WorkSpace/StudentScheduleBuilder', methods=['POST', 'GET'])
def studentScheduleBuilder():
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) == True:
            return render_template('SH.html', authKey = authKey)
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)