import MySQLdb
from datetime import datetime
import bcrypt
from flask import Flask
from flask import jsonify, request
import uuid
import cProfile
import re
from flask_cors import CORS



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
        database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="logindata")
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
        

def adminLogin(UserID, Password):

    try:
        database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="admindata")
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
        database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="logindata")
        Log("Login database connected")
        query=database.cursor()
        query.execute(("SELECT UID FROM login;"))
        data = query.fetchone()
        tempid=uuid.uuid4()
        while data is not None:
            data = query.fetchone()
            if data == tempid:
                return "-1"
        Log("New UID returned")
        database.close()
        return tempid

    except:
        Log("Failed to connect to login database in getNewUID()")

#create user ID, salt, hashed password, other data
def createUser(username, password):
    try:
        salt = bcrypt.gensalt()
        UID=getNewUID()
        storedPass=str(bcrypt.hashpw(str(password),salt))
        database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="logindata")
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
    
def createAdmin(username, password):
    try:
        salt = bcrypt.gensalt()
        UID=getNewUID()
        storedPass=str(bcrypt.hashpw(str(password),salt))
        database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="admindata")
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
    database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="logindata")
    Log("Login database connected")
    query=database.cursor()
    salt= bcrypt.gensalt()
    storedPass = str(bcrypt.hashpw(newpass,salt))
    query.execute(("UPDATE login SET Password='{}', Salt='{}' WHERE Username='{}';".format(storedPass, salt, username)))
    database.commit()
    database.close()

def searchByUser(userid):
    lats=[]
    longs=[]
    times=[]
    database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="gps")
    Log("Login database connected")
    query=database.cursor()
    query.execute(("SELECT * FROM gpsdata WHERE UID={}").format(str(userid)))
    data = query.fetchone()
    while data is not None:
        times.append(data[4])
        lats.append(data[1])
        longs.append(data[2])
        data=query.fetchone()
    database.close()
    return times,lats,longs

def mapValues():
    initial_db=[]
    usernames=[]
    uids=[]
    lats=[]
    longs=[]
    dates=[]
    times=[]

    database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="logindata")
    Log("Login database connected")
    query=database.cursor()
    query.execute(("SELECT Username,UID FROM login"))
    data = query.fetchone()
    
    while data != None:
        uids.append(data[1])
        usernames.append(data[0])
        data = query.fetchone()
    database.close()
    for entry in uids:
        database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="gps")
        query=database.cursor()
        query.execute(("SELECT * FROM gpsdata WHERE UID = '{}' ORDER BY Dates,Times DESC;").format(entry))
        data=query.fetchone()
        lats.append(data[1])
        longs.append(data[2])
        yr=str(data[3].year)
        mo=str(data[3].month)
        day=str(data[3].day)
        finstr=yr + "-" + mo + "-" + day
        dates.append(finstr)
        times.append(str(data[4]))
    return usernames,uids,lats,longs,dates,times
    
mapValues()

#################ROUTES############################################
@app.route("/login", methods = ['POST', 'OPTIONS'])
def netLogin():
    Log("in app")
    cursor = None
    conn = None

    try:
        if request.method=="OPTIONS":
            resp=jsonify("")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
        
        _json = request.json
        _username = str(_json['username'])
        _password = str(_json['password'])
        if _username and _password and request.method == 'POST':
            result = Login(_username,_password)
            print(result)
            if result != "-1":
                resp=jsonify(result)
                resp.headers.add("Access-Control-Allow-Origin", "*")
                resp.headers.add("Access-Control-Allow-Methods", "*")
                resp.headers.add("Access-Control-Allow-Headers", "*")
                resp.status_code = 200
                return resp
            else:
                resp=jsonify(result)
                resp.headers.add("Access-Control-Allow-Origin", "*")
                resp.headers.add("Access-Control-Allow-Methods", "*")
                resp.headers.add("Access-Control-Allow-Headers", "*")
                resp.status_code = 200
                return resp
        else:
            resp =jsonify("wrong format")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp

    except Exception as e:
        print(e)




@app.route("/AdminLogin", methods = ['POST','OPTIONS'])
def adLogin():
    Log("in app")
    cursor = None
    conn = None
    try:
        if request.method=="OPTIONS":
            resp=jsonify("0")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
        Log("in try")
        _json = request.json
        _username = str(_json['username'])
        _password = str(_json['password'])
        print(_password)
        print(_username)
        if _username and _password and request.method == 'POST':
            result = adminLogin(_username,_password)
            if result != "-1":
                resp=jsonify(result)
                resp.headers.add("Access-Control-Allow-Origin", "*")
                resp.headers.add("Access-Control-Allow-Methods", "*")
                resp.headers.add("Access-Control-Allow-Headers", "*")
                resp.status_code = 200
                return resp
            else:
                resp=jsonify(result)
                resp.headers.add("Access-Control-Allow-Origin", "*")
                resp.headers.add("Access-Control-Allow-Methods", "*")
                resp.headers.add("Access-Control-Allow-Headers", "*")
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
        if request.method=="OPTIONS":
            resp=jsonify("0")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
        Log("in try")
        _json = request.json
        _username = _json['username']
        _password = _json['password']

        if _username and _password and request.method == 'POST':
            createUser(_username,_password)
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            resp=jsonify('User Created')
            resp.status_code = 200
            return resp
        else:
            resp =jsonify("wrong format")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp

    except Exception as e:
        print(e)

@app.route("/createAdmin", methods = ['POST'])
def netCreateAdmin():
    Log("in app")
    cursor = None
    conn = None
    try:
        if request.method=="OPTIONS":
            resp=jsonify("0")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
        Log("in try")
        _json = request.json
        _username = _json['username']
        _password = _json['password']

        if _username and _password and request.method == 'POST':
            createAdmin(_username,_password)
            
            resp=jsonify('User Created')
            resp.status_code = 200
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
        else:
            resp =jsonify("wrong format")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp

    except Exception as e:
        print(e)

###
@app.route("/gpsdata", methods = ['POST'])
def datalog():
    Log("in log")
    cursor = None
    conn = None
    try:hooo
        if request.method=="OPTIONS":
            resp=jsonify("0")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
        Log("in try")
        _json = request.json
        _uid=str(_json['uid'])
        _long = str(_json['longitude'])
        _lat =str(_json['latitude'])
        _time = timestamp()
        
        if _uid and _long and _lat and request.method == 'POST':
            database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="gps")
            Log("Login database connected")
            query=database.cursor()
            query.execute(("INSERT INTO gpsdata (UID , Latitude, Longitude, Dates, Times) VALUES ( {},{},{}, CURDATE(), CURRENT_TIME() );").format(_uid,_lat,_long))
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
        if request.method=="OPTIONS":
            resp=jsonify("0")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
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


@app.route("/map", methods = ['POST','OPTIONS'])
def mapping():
    cursor = None
    conn = None
    _json = request.json
    try:
        if request.method=="OPTIONS":
            resp=jsonify("0")
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp
        if 1==1:
            usernames,uids,lats,longs,dates,times=mapValues()
            resp=jsonify(usernames,uids,lats,longs,dates,times)
            resp.headers.add("Access-Control-Allow-Origin", "*")
            resp.headers.add("Access-Control-Allow-Methods", "*")
            resp.headers.add("Access-Control-Allow-Headers", "*")
            return resp

        else:
                resp =jsonify("wrong uid")
                resp.headers.add("Access-Control-Allow-Origin", "*")
                resp.headers.add("Access-Control-Allow-Methods", "*")
                resp.headers.add("Access-Control-Allow-Headers", "*")
                return resp

    except Exception as e:
        print(e)

#####MAIN#######################################################################
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, ssl_context=('cert.pem', 'key.pem'))

#CORS(app.run(host='0.0.0.0', port=5005, ssl_context=('cert.pem', 'key.pem')))




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