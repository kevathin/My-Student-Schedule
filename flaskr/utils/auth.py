import sqlite3
import hashlib


def authUser(user, password):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    md5_hash = hashlib.md5()
    md5_hash.update(password.encode('utf-8'))
    dbCursor.execute(f"SELECT * FROM STUDENTUSERPASSWORD WHERE UserName = '{user}' AND Password = '{md5_hash.hexdigest()}'")
    result = dbCursor.fetchone()
    if result:
        md5_authKey = hashlib.md5()
        combo = result[0] + result[1]
        md5_authKey.update(combo.encode('utf-8'))
        authkey = md5_authKey.hexdigest()
        dbCursor.execute(f"INSERT INTO AUTHKEYS VALUES ( '{authkey}' , {result[2]} );")
        dbConnection.commit()
        dbCursor.close()
        dbConnection.close()
        return authkey
    else:
        dbCursor.close()
        dbConnection.close()
        return "failure"

def authKeyCheck(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute(f"SELECT * FROM AUTHKEYS WHERE AuthKey = '{authKey}'")
    result = dbCursor.fetchone()
    if result:
        dbCursor.close()
        dbConnection.close()
        return authKey
    else:
        dbCursor.close()
        dbConnection.close()
        return "failure"

def authLogOut(authKey):
    dbConnection = sqlite3.connect('flaskr/example.db')
    dbCursor = dbConnection.cursor()
    dbCursor.execute(f"DELETE FROM AUTHKEYS WHERE AuthKey = '{authKey}'")
    dbConnection.commit()
    dbCursor.close()
    dbConnection.close()
    return