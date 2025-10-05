from flask import Flask, render_template, request
from utils.auth import authUser, authKeyCheck, authLogOut
from utils.dbManager import dbChecker, createAccount, dbFiller, wipeTempAuth
app = Flask(__name__)

@app.route('/')
def index():
    wipeTempAuth()
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/createAccount', methods=['POST', 'GET'])
def createAccountapp():

    if request.method == 'POST':
        result = createAccount(request.form['uname'], request.form['upass'], request.form['SID'])
        if result == "accOverLap":
            return render_template("register.html", error = "Account Already Exists")
    else:
        return render_template("register.html", error = "invalid method used")
    
    return render_template("login.html")

@app.route('/logout', methods=['POST', 'GET'])
def logout():

    authLogOut(request.form['authKey'])
    return render_template("index.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template("register.html")

@app.route('/WorkSpace', methods=['POST', 'GET'])
def accessWorkSpace():
    error = None
    if request.method == 'POST':
        authKey = authUser(request.form['uname'], request.form['upass'])
        if  authKey != "failure":
            return studentHome(authKey)
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/StudentHome', methods=['POST', 'GET'])
def studentHome():
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) != "failure":
            return render_template('SH.html', authKey = authKey)
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)
    else:
        print("failed SH post con")

def studentHome(authKey):
    error = None
    if authKeyCheck(authKey) != "failure":
        return render_template('SH.html', authKey = authKey)
    else: 
        error = 'authKey expired/not found'
        return render_template('login.html', error=error)


@app.route('/StudentRegister', methods=['POST', 'GET'])
def studentRegister():
    print("")
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) != "failure":
            return render_template('SR.html', authKey = authKey)
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)
    else:
        print("failed SR post con")
        
@app.route('/StudentScheduleBuilder', methods=['POST', 'GET'])
def studentScheduleBuilder():
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) != "failure":
            return render_template('SSB.html', authKey = authKey)
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)
    else:
        print("failed SB post con")