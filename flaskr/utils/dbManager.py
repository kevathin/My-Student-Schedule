import sqlite3
import hashlib


def createDB():
    dbConnection = sqlite3.connect('flaskr/example.db')

    dbCursor = dbConnection.cursor()

    dbCursor.execute("""CREATE TABLE ACTIVECOURSE(
                     ID TEXT PRIMARY KEY,
                     CourseID TEXT, 
                     Section INTEGER,
                     Schedule_ID INTEGER,
                     LectureStartTime INTEGER,
                     LectureEndTime INTEGER,
                     TutorialStartTime INTEGER,
                     TutorialEndTime INTEGER,
                     LabStartTime INTEGER,
                     LabEndTime INTEGER,
                     ProfessorID INTEGER,
                     ProfessorPrivacy INTEGER,
                     Seats INTEGER, 
                     SeatsFilled INTEGER
                     );""")
    
    dbCursor.execute("""CREATE TABLE LECTURE_TYPE(
                     Schedule_ID INTEGER PRIMARY KEY,
                     Lecture_Dates TEXT,
                     Lab_Date TEXT,
                     Tutorial_Date TEXT
                     );""")
    
    dbCursor.execute("""CREATE TABLE PROFESSOR(
                     ID INTEGER PRIMARY KEY,
                     FirstName TEXT,
                     LastName TEXT
                     );""")
    
    dbCursor.execute("""CREATE TABLE STUDENT(
                     SID INTEGER PRIMARY KEY,
                     Email TEXT,
                     FirstName TEXT,
                     LastName TEXT,
                     ProgramID INTEGER
                     );""")
    
    dbCursor.execute("""CREATE TABLE PROGRAM(
                     ID INTEGER PRIMARY KEY,
                     Program TEXT,
                     Major TEXT,
                     Faculty TEXT,
                     Degree TEXT
                     );""")
    
    dbCursor.execute("""CREATE TABLE PROGRAMCOURSEREQUIREMENT(
                     ProgramID INTEGER,
                     CourseID TEXT
                     );""")

    dbCursor.execute("""CREATE TABLE STUDENTUSERPASSWORD(
                     UserName TEXT,
                     Password TEXT,
                     SID INTEGER
                     );""")
    
    dbCursor.execute("""CREATE TABLE AUTHKEYS(
                     AuthKey TEXT PRIMARY KEY,
                     SID INTEGER
                     );""")
    
    dbCursor.execute("""CREATE TABLE COURSE(
                     CourseID TEXT PRIMARY KEY, 
                     Name TEXT,
                     Description TEXT,
                     Prerequisites TEXT,
                     Classification TEXT
                     );""")
    
    dbCursor.execute("""CREATE TABLE STUDENTCOURSECOMPLETION(
                     CourseID TEXT,
                     SID int,
                     Grade int
                     );""")
    
    dbCursor.execute("""CREATE TABLE STUDENTCOURSEPLAN(
                     CourseID TEXT,
                     SID int
                     );""")
    
    dbCursor.execute(f"SELECT * FROM STUDENTUSERPASSWORD")
    dbConnection.commit()
    dbCursor.close()
    dbConnection.close()
    return True

def dbFiller():
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute("""INSERT INTO PROFESSOR VALUES (101, "john", "doe");""")
    dbCursor.execute("""INSERT INTO PROFESSOR VALUES (102, "jane", "doe");""")
    dbCursor.execute("""INSERT INTO PROFESSOR VALUES (103, "jack", "black");""")
    dbCursor.execute("""INSERT INTO PROFESSOR VALUES (104, "morgan", "freeman");""")
    dbCursor.execute("""INSERT INTO PROGRAM VALUES (101, "Bachelor of Comp Info Systems", "Comp Info Systems", "Science and Technology", "Bachelor of Computer Information Systems");""")
    dbCursor.execute("""INSERT INTO PROGRAM VALUES (102, "Bachelor of Computer Science", "Computer Science", "Science and Technology", "Bachelor of Science");""")
    dbCursor.execute("""INSERT INTO STUDENT VALUES (201745395, "kbert395@mtroyal.ca", "Kevin", "Bertasius", 101);""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (101, "mw", 'f', 'f');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (102, "mw", 'n', 'f');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (103, "mw", 'f', 'n');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (104, "mw", 'n', 'n');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (105, "th", 'f', 'f');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (106, "th", 'n', 'f');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (107, "th", 'f', 'n');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (108, "th", 'n', 'n');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (109, "h", 'n', 'n');""")
    dbCursor.execute("""INSERT INTO LECTURE_TYPE VALUES (110, "m", 'n', 'n');""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("ACCT 2121", "Financial Accounting Concepts", "money", "", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("COMP 1701", "Introduction to Programming", "python", "", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("COMP 1502", "Programming 2", "java", "COMP 1701", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("COMP 2503", "Programming 3", "java but funny", "COMP 1502", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("COMP 2511", "Web 1", "HTML go Burr", "COMP 1701", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("COMP 2531", "Arch & OS", "cpuuuuuu", "COMP 1701", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("HRES 2170", "Introduction to Human Resources", "ctrl c ctrl v the same concepts", "", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("GNED 1404", "Writing about Images", "easy ah course", "", "GNED");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("GNED 1303", "Conflict in a social context", "my prof looked like jack black", "", "GNED");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("PSYC 1105", "Introduction to Psychology", "Pain", "", "GNED");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("PHYS 1201", "Classical Physics", "Snoozed", "", "GNED");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("COMP 2521", "Database 1", "pretty fun", "COMP 1701", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("MATH 1505", "Puzzling Adventures in Math", "headache", "", "ProgReq");""")
    dbCursor.execute("""INSERT INTO COURSE VALUES ("MGMT 3210", "Business Communication", "Prof yapped most of the time", "", "ProgReq");""")
    dbCursor.execute("""INSERT INTO STUDENTCOURSEPLAN VALUES ("ACCT 2121-001", 201745395);""")
    dbCursor.execute("""INSERT INTO STUDENTCOURSEPLAN VALUES ("PHYS 1201-001", 201745395);""")
    dbCursor.execute("""INSERT INTO STUDENTCOURSEPLAN VALUES ("MATH 1505-001", 201745395);""")
    dbCursor.execute("""INSERT INTO STUDENTCOURSEPLAN VALUES ("COMP 2511-001", 201745395);""")
    dbCursor.execute("""INSERT INTO STUDENTCOURSEPLAN VALUES ("COMP 1502-001", 201745395);""")
    dbCursor.execute("""INSERT INTO ACTIVECOURSE VALUES ("ACCT 2121-001", "ACCT 2121", 001, 104, 1000,1130 ,0 ,0 ,0 ,0,102, 0, 40,23 );""")
    dbCursor.execute("""INSERT INTO ACTIVECOURSE VALUES ("PHYS 1201-001", "PHYS 1201", 001, 104, 1130,1300 ,0 ,0 ,0 ,0,101, 0, 40,24 );""")
    dbCursor.execute("""INSERT INTO ACTIVECOURSE VALUES ("MATH 1505-001", "MATH 1505", 001, 108, 1130,1300 ,0 ,0 ,0 ,0,102, 0, 40,27 );""")
    dbCursor.execute("""INSERT INTO ACTIVECOURSE VALUES ("COMP 2511-001", "COMP 2511", 001, 108, 1000,1130 ,0 ,0 ,0 ,0,103, 0, 40,20 );""")
    dbCursor.execute("""INSERT INTO ACTIVECOURSE VALUES ("COMP 1502-001", "COMP 1502", 001, 108, 1300,1430 ,0 ,0 ,0 ,0,104, 0, 40,39 );""")
    dbConnection.commit()
    dbCursor.close()
    dbConnection.close()

def dbChecker():
    try: 
        dbConnection = sqlite3.connect('flaskr/example.db')
        dbCursor = dbConnection.cursor()

        dbCursor.execute("""SELECT SID
                        FROM STUDENT
                        """).fetchall()

        dbCursor.close()
        dbConnection.close()
    except:
        createDB()

def createAccount(username, password, SID):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute(f"SELECT * FROM STUDENTUSERPASSWORD WHERE UserName = '{username}'")
    result = dbCursor.fetchone()
    if result:
        dbCursor.close()
        dbConnection.close()
        return "accOverLap"
    dbCursor = dbConnection.cursor()
    md5_conv = hashlib.md5()
    md5_conv.update(password.encode('utf-8'))
    dbCursor.execute(f"INSERT INTO STUDENTUSERPASSWORD VALUES ('{username}', '{md5_conv.hexdigest()}', {SID})")
    dbConnection.commit()
    dbCursor.close()
    dbConnection.close()
    return

def wipeTempAuth():
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute("DELETE FROM AUTHKEYS")
    dbConnection.commit()
    dbCursor.close()
    dbConnection.close()
    return
    
def getSID(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute(f"SELECT * FROM AUTHKEYS WHERE AuthKey = '{authKey}'")
    result = dbCursor.fetchone()
    dbCursor.close()
    dbConnection.close()
    if result:
        print(result[1])
        return result[1]
    print("damn")
    return None

def getFullName(authKey):
    
    SIDt = getSID(authKey)
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute(f"SELECT * FROM STUDENT WHERE SID = {SIDt}")
    result2 = dbCursor.fetchone()
    print(result2[3])
    if result2:
        FullName = f"{result2[2]}  {result2[3]}"
        dbCursor.close()
        dbConnection.close()
        return FullName
    
    

def getGPA(authKey):
    return "N/a"

def getDegree(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    SID = getSID(authKey)
    if SID:
        dbCursor.execute(f"SELECT * FROM STUDENT WHERE SID = {SID}")
        result = dbCursor.fetchone()
        programID = result[4]
        dbCursor.close()
        dbCursor = dbConnection.cursor()
        dbCursor.execute(f"SELECT * FROM PROGRAM WHERE ID = {programID}")
        result = dbCursor.fetchone()
        Degree = result[4]
        dbCursor.close()
        dbConnection.close()
        return Degree
    dbCursor.close()
    dbConnection.close()
    return

def getMajor(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    SID = getSID(authKey)
    if SID:
        dbCursor.execute(f"SELECT * FROM STUDENT WHERE SID = {SID}")
        result = dbCursor.fetchone()
        programID = result[4]
        dbCursor.close()
        dbCursor = dbConnection.cursor()
        dbCursor.execute(f"SELECT * FROM PROGRAM WHERE ID = {programID}")
        result = dbCursor.fetchone()
        Degree = result[2]
        dbCursor.close()
        dbConnection.close()
        return Degree
    dbCursor.close()
    dbConnection.close()
    return

def getProgram(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    SID = getSID(authKey)
    if SID:
        dbCursor.execute(f"SELECT * FROM STUDENT WHERE SID = {SID}")
        result = dbCursor.fetchone()
        programID = result[4]
        dbCursor.close()
        dbCursor = dbConnection.cursor()
        dbCursor.execute(f"SELECT * FROM PROGRAM WHERE ID = {programID}")
        result = dbCursor.fetchone()
        Degree = result[1]
        dbCursor.close()
        dbConnection.close()
        return Degree
    dbCursor.close()
    dbConnection.close()
    return

def getFaculty(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    SID = getSID(authKey)
    if SID:
        dbCursor.execute(f"SELECT * FROM STUDENT WHERE SID = {SID}")
        result = dbCursor.fetchone()
        programID = result[4]
        dbCursor.close()
        dbCursor = dbConnection.cursor()
        dbCursor.execute(f"SELECT * FROM PROGRAM WHERE ID = {programID}")
        result = dbCursor.fetchone()
        Degree = result[3]
        dbCursor.close()
        dbConnection.close()
        return Degree
    dbCursor.close()
    dbConnection.close()
    return

def getCompletedCourses(authKey):
    return "N/a"

def getPlannedCourses(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute("SELECT * FROM ACTIVECOURSE")
    result = dbCursor.fetchall()
    dbCursor.close()
    dbConnection.close()
    return result

def getRequiredCourses(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute("SELECT * FROM COURSE")
    result = dbCursor.fetchall()
    dbCursor.close()
    dbConnection.close()
    return result

def getCourseFullName(courseID):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute(f"SELECT * FROM COURSE WHERE CourseID = '{courseID}'")
    result = dbCursor.fetchone()
    dbCursor.close()
    dbConnection.close()
    return result[1]