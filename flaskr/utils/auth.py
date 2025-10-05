import sqlite3



def authUser():
    dbConnection = sqlite3.connect('example.db')
    dbCursor = dbConnection.cursor()

    dbCursor.close()
    dbConnection.close()
    return True

def authKeyCheck(authKey):
    dbConnection = sqlite3.connect('example.db')
    dbCursor = dbConnection.cursor()

    dbCursor.close()
    dbConnection.close()
    return True

