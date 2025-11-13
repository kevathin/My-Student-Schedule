from flask import Flask, render_template, request
from utils.auth import authUser, authKeyCheck, authLogOut
from utils.dbManager import dbChecker, createAccount, dbFiller, wipeTempAuth, getCompletedCourses, getDegree,getFaculty,getFullName,getGPA,getMajor,getPlannedCourses,getProgram,getSID, getRequiredCourses, getCourseFullName
app = Flask(__name__)

@app.route('/')
def index():
    wipeTempAuth()
    return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/createAccount', methods=['POST', 'GET'])
def createAccount():

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
def WorkSpace():
    error = None
    if request.method == 'POST':
        authKey = authUser(request.form['uname'], request.form['upass'])
        if  authKey != "failure":
            return StudentHome(authKey)
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/StudentHome', methods=['POST', 'GET'])
def StudentHome():
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) != "failure":
            
            return render_template('SH.html', 
                                    authKey = authKey,
                                    SID = getSID(authKey),
                                    FandLName = getFullName(authKey),
                                    degree = getDegree(authKey),
                                    major = getMajor(authKey),
                                    Program = getProgram(authKey),
                                    faculty = getFaculty(authKey),
                                    GPA = getGPA(authKey),
                                    totalCredits = 15,
                                    GPAConclusion = "not",
                                    failedGPA = "you have not completed any courses to calculate GPA",
                                    MajorConclusion = "not",
                                    failedMajor = "you have not completed you major courses",
                                    GNEDConclusion = "not",
                                    failedGNED = "you have not completed your GNED courses",
                                    ElectiveConclusion = "not",
                                    failedElective = "you have not completed your elective courses",
                                    degreeSpecificTable = makeMajorList(getRequiredCourses(authKey)),
                                    GNEDSpecificTable = makeGNEDList(getRequiredCourses(authKey)),
                                    ElectivesSpecificTable = makeElectiveList()
                                   )
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)
    else:
        print("failed SH post con")

def StudentHome(authKey):
    error = None
    if authKeyCheck(authKey) != "failure":
        return render_template('SH.html', authKey = authKey,
                                        SID = getSID(authKey),
                                        FandLName = getFullName(authKey),
                                        degree = getDegree(authKey),
                                        major = getMajor(authKey),
                                        Program = getProgram(authKey),
                                        faculty = getFaculty(authKey),
                                        GPA = getGPA(authKey),
                                        totalCredits = 15,
                                        GPAConclusion = "not",
                                        failedGPA = "you have not completed any courses to calculate GPA",
                                        MajorConclusion = "not",
                                        failedMajor = "you have not completed you major courses",
                                        GNEDConclusion = "not",
                                        failedGNED = "you have not completed your GNED courses",
                                        ElectiveConclusion = "not",
                                        failedElective = "you have not completed your elective courses",
                                        degreeSpecificTable = makeMajorList(getRequiredCourses(authKey)),
                                        GNEDSpecificTable = makeGNEDList(getRequiredCourses(authKey)),
                                        ElectivesSpecificTable = makeElectiveList()
                                        )
    else: 
        error = 'authKey expired/not found'
        return render_template('login.html', error=error)


@app.route('/StudentRegister', methods=['POST', 'GET'])
def StudentRegister():
    print("")
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) != "failure":
            return render_template('SR.html', authKey = authKey,
                                                activeScheduleView = makeVisualSchedule(getPlannedCourses(authKey)),
                                                courseSummaryView = courseOutputTwo(getPlannedCourses(authKey))
                                                )
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)
    else:
        print("failed SR post con")
        
@app.route('/StudentScheduleBuilder', methods=['POST', 'GET'])
def StudentScheduleBuilder():
    error = None
    if request.method == 'POST':
        authKey = request.form['authKey']
        if authKeyCheck(authKey) != "failure":
            return render_template('SSB.html', authKey = authKey,
                                                activeScheduleView = makeVisualSchedule(getPlannedCourses(authKey)),
                                                courseOne = courseOutput(getPlannedCourses(authKey)[0]),
                                                courseTwo = courseOutput(getPlannedCourses(authKey)[1]),
                                                courseThree = courseOutput(getPlannedCourses(authKey)[2]),
                                                courseFour = courseOutput(getPlannedCourses(authKey)[3]),
                                                courseFive =courseOutput(getPlannedCourses(authKey)[4])
                                            )
        else: 
            error = 'authKey expired/not found'
            return render_template('login.html', error=error)
    else:
        print("failed SB post con")

def makeMajorList(tlist):
    output = f""
    i = 0
    output = f"{output}<div class='twowide'>Course Name</div> <div>Course</div> <div>Credits</div>"
    while(i < len(tlist)):
        if tlist[i][4] == "ProgReq":
            output = f"{output}<div class='twowide'>{tlist[i][1]}</div> <div>{tlist[i][0]}</div>  <div>3</div>"
        i = i + 1

    return output

def makeGNEDList(tlist):
    output = f""
    i = 0
    output = f"{output}<div class='twowide'>Course Name</div> <div>Course</div> <div>Credits</div>"
    while(i < len(tlist)):
        if tlist[i][4] == "GNED":
            output = f"{output}<div class='twowide'>{tlist[i][1]}</div> <div>{tlist[i][0]}</div>  <div>3</div>"
        i = i + 1

    return output

def makeElectiveList():
    output = f"<div class='twowide'>Course Name</div> <div>Course</div> <div>Credits</div>"
    return output

def makeVisualSchedule(tlist):
    output = f""
    i = 0 
    hour = 8
    min = 0
    output = f"{output} <div class='time'>monday </div> <div class='time'>tuesday </div>  <div class='time'> wednesday</div>  <div class='time'> thursday</div> <div class='time'> friday</div>"

    for item in tlist:
        if item[3] == 104:
            output = f"{output} <div class='monday' style='grid-row: {calcRow(item[4])}, span 3'>{item[1]}</div> <div class='wednesday' style='grid-row: {calcRow(item[4])}, span 3'>{item[1]}</div>"
        else:
            output = f"{output} <div class='tuesday' style='grid-row: {calcRow(item[4])}, span 3'>{item[1]}</div> <div class='thursday' style='grid-row: {calcRow(item[4])}, span 3'>{item[1]}</div>"
    
    return output

def makeVisualTime():
    output = f""
    i = 0 
    hour = 8
    min = 0
    output = f"{output} <div class='time first'>time </div> "

    while(i < 24):
        min = min + 30
        if min == 60:
            min = 0
            hour = hour + 1
        output = f"{output} <div class='first'> {str(hour)}:{str(min)}</div>"
        i = i +1

def calcRow(time):
    #8:30am = row 1
    #8:30pm = row 25
    counter = 1
    if int(time) % 100 != 0:
        time = time - 800
        time = time - 30
        counter = counter + ((time/100) * 2)
    else:
        counter = counter + ((time/100) * 2) + 1
    return counter

def courseOutput(item):
    output = f"<div class='courseBox'><div class='courseTitleBox'>{item[1]}</div><div class='courseContentBox'>{getCourseFullName(item[1])}</div> </div> "
    return output

def courseOutputTwo(tlist):
    output = f"<div id='courseSumBox'><div>Status</div><div>Course Details</div><div>Title</div><div>Schedule Type</div><div>Credits</div>"

    for item in tlist:
        output = f"{output} <div class='greenGlow'><p>Registered<p></div> <div>{item[0]}</div> <div>{getCourseFullName(item[1])}</div> <div>Lecture</div> <div>3</div>"

    output = f"{output} </div>"

    return output