import sqlite3



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
                     Name TEXT,
                     Faculty TEXT,
                     Department TEXT,
                     DegreeType TEXT
                     );""")
    
    dbCursor.execute("""CREATE TABLE PROGRAMCOURSEREQUIREMENT(
                     ProgramID INTEGER,
                     CourseID TEXT
                     );""")

    dbCursor.execute("""CREATE TABLE STUDENT_USER_PASSWORD(
                     UserName TEXT,
                     PASSWORD TEXT,
                     SID INTEGER
                     );""")
    
    dbCursor.execute("""CREATE TABLE AUTHKEYS(
                     authKey TEXT PRIMARY KEY,
                     SID INTEGER
                     );""")
    
    dbCursor.execute("""CREATE TABLE COURSE(
                     CourseID TEXT PRIMARY KEY, 
                     Name TEXT,
                     Description TEXT,
                     Prerequisites TEXT
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
    
    dbCursor.close()
    dbConnection.close()
    return True

def dbFiller():
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()

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