import MySQLdb
from datetime import datetime
import bcrypt
from flask import Flask
from flask import jsonify, request
app = Flask(__name__)
#establish variables


#log everything that happens to Logs.txt with timestamps and commands
def Log(data):
    file = open("Logs.txt","a")
    time = str(timestamp())
    file.write(time + ": " + data + '\n')
    file.close

def timestamp():
    today = datetime.now()
    timestamp = today.strftime("%H:%M:%S")
    return timestamp


#hash and return and verify

def verify(password, salt, dbstored, UID):
    word = bcrypt.hashpw(str(password),salt)
    if word == dbstored:
        return True
        Log("User {} granted access.".format(UID))
    else:
        return False
        Log("User {} denied access".format(UID))


#process information and retrieve information from database
#connect to the database
def Login(UserID, Password):

    try:
        database = MySQLdb.connect(host="database-2.ca5zjjy9qj09.us-east-1.rds.amazonaws.com",user="admin",passwd="password",db="logindata")
        Log("Login database connected in Login")
        print("connected")
        try:
            query=database.cursor()
            query.execute(("SELECT * FROM login WHERE Username='{}'".format(UserID)))
            data=query.fetchone()
            UID=data[0]
            PW=data[1]
            SALT=data[3]
            database.close()
            #Communicate with website results
            if verify(Password,SALT,PW,UID) == True:
                return(str(UID))
                Log("Data succesfully retrieved from login database in Login")
            else:
                return("-1")
            
        except Exception as e:
            print(e)
            Log("Data failed to retrieve from login database in Login")
            
    except:
        Log("Login database failed to connect in Login")
        


def getNewUID():
    try:
        database = MySQLdb.connect(host="database-2.ca5zjjy9qj09.us-east-1.rds.amazonaws.com",user="admin",passwd="password",db="logindata")
        Log("Login database connected")
        query=database.cursor()
        query.execute(("SELECT UID FROM login;"))
        data = query.fetchone()
        numids=1
        Log("New UID generated")
        while data is not None:
            data = query.fetchone()
            numids+=1
        Log("New UID returned")
        database.close()
        return numids

    except:
        Log("Failed to connect to login database in getNewUID()")

#create user ID, salt, hashed password, other data
def createUser(username, password):
    try:
        salt = bcrypt.gensalt()
        UID=getNewUID()
        storedPass=str(bcrypt.hashpw(str(password),salt))
        database = MySQLdb.connect(host="database-2.ca5zjjy9qj09.us-east-1.rds.amazonaws.com",user="admin",passwd="password",db="logindata")
        Log("Login database connected")
        query=database.cursor()
        query.execute(("SELECT Username FROM login;"))
        data = query.fetchone()
        dup=False
        while data is not None:
            data=query.fetchone()
            name = str(query.fetchone())
            name = name.strip("(',)")
            if name == username:
                dup=True
            else:
                pass
        if dup==True:
            Log("Invalid username")
        else:
            query.execute(("INSERT INTO login (UID, Password, Username, Salt) VALUES ('{}','{}','{}','{}');".format(UID,storedPass,username,salt)))
            database.commit()
            Log("New User created and committed to database")
        database.close()
    except Exception as e:
        print(e)
        Log("Failed to create new user")
    
def changePassword(username, newpass):
    database = MySQLdb.connect(host="database-2.ca5zjjy9qj09.us-east-1.rds.amazonaws.com",user="admin",passwd="password",db="logindata")
    Log("Login database connected")
    query=database.cursor()
    salt= bcrypt.gensalt()
    storedPass = str(bcrypt.hashpw(newpass,salt))
    query.execute(("UPDATE login SET Password='{}', Salt='{}' WHERE Username='{}';".format(storedPass, salt, username)))
    database.commit()
    database.close()
#######################################################3
def searchByUser(userid):
    lats=[]
    longs=[]
    times=[]
    database = MySQLdb.connect(host="database-2.ca5zjjy9qj09.us-east-1.rds.amazonaws.com",user="admin",passwd="password",db="gps")
    Log("Login database connected")
    query=database.cursor()
    query.execute(("SELECT * FROM gpsdata WHERE id={}").format(str(userid)))
    data = query.fetchone()
    while data is not None:
        times.append(data[1])
        lats.append(data[2])
        longs.append(data[3])
        data=query.fetchone()
    database.close()
    return times,lats,longs


#################MAIN############################################
@app.route("/login", methods = ['POST'])
def netLogin():
    Log("in app")
    cursor = None
    conn = None
    try:
        Log("in try")
        _json = request.json
        _username = str(_json['username'])
        _password = str(_json['password'])
        print(_password)
        print(_username)
        if _username and _password and request.method == 'POST':
            result = Login(_username,_password)
            if result != "-1":
                resp=jsonify(result)
                resp.status_code = 200
                return resp
            else:
                resp=jsonify(result)
                resp.status_code = 200
                return resp
        else:
            resp =jsonify("wrong format")
            return resp

    except Exception as e:
        print(e)

@app.route("/createUser", methods = ['POST'])
def netCreateUser():
    Log("in app")
    cursor = None
    conn = None
    try:
        Log("in try")
        _json = request.json
        _username = _json['username']
        _password = _json['password']

        if _username and _password and request.method == 'POST':
            createUser(_username,_password)
            
            resp=jsonify('User Created')
            resp.status_code = 200
            return resp
        else:
            resp =jsonify("wrong format")
            return resp

    except Exception as e:
        print(e)


###
@app.route("/gpsdata", methods = ['POST'])
def datalog():
    Log("in log")
    cursor = None
    conn = None
    try:
        Log("in try")
        _json = request.json
        _uid=str(_json['uid'])
        _long = str(_json['longitude'])
        _lat =str(_json['latitude'])
        _time = timestamp()
        
        if _uid and _long and _lat and request.method == 'POST':
            database = MySQLdb.connect(host="database-2.ca5zjjy9qj09.us-east-1.rds.amazonaws.com",user="admin",passwd="password",db="gps")
            Log("Login database connected")
            query=database.cursor()
            query.execute(("INSERT INTO gpsdata (UID , Latitude, Longitude, Date, time) VALUES ( {},{},{}, CURDATE(), CURRENT_TIME() );").format(_uid,_lat,_long))
            database.commit()
            database.close()
            resp = jsonify("data entered")
            return resp
        else:
            resp =jsonify("wrong format")
            return resp

    except Exception as e:
        print(e)


@app.route("/searchuser", methods = ['POST'])
def searchUser():
    cursor = None
    conn = None
    _json = request.json
    try:
        if 1==1:
            _uid = str(_json['uid'])
            times,lats,longs = searchByUser(_uid)
            resp=jsonify(times,lats,longs)
            return resp

        else:
                resp =jsonify("wrong uid")
                return resp

    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, ssl_context=('cert.pem', 'key.pem'))





######DEBUGGING##########
#Login("Geralt","password123")
##
#state=verify("Blob","$2a$12$BRZv4tU9bmf3.5s3cu4ONO","$2a$12$BRZv4tU9bmf3.5s3cu4ONOp3IuCGYBa3h9KGO7ZoJNBCFmqr1u.DW","3")
#if state==True:
    #print("verify successful")
##
#createUser("Stehf","Blob")
##
#data=getNewUID()
#print(data)
##
#changePassword("Stehf","Sterile")