import MySQLdb
from datetime import datetime
import bcrypt
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
    word = bcrypt.hashpw(password,salt)
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
        
        try:
            query=database.cursor()
            query.execute(("SELECT * FROM login WHERE Username='{}'".format(UserID)))
            data=query.fetchone()
            UID=data[0]
            PW=data[2]
            SALT=data[3]
            database.close()
            Log("Data succesfully retrieved from login database in Login")
        except:
            Log("Data failed to retrieve from login database in Login")
            
    except:
        Log("Login database failed to connect in Login")
        
#Communicate with website results
    #validateLogin = verify(Password,SALT,PW,UID)
    #if (validateLogin == True):
        #print("Validated")
        #allow access
    #else:
        #print("Denied")
        #deny acess

def getNewUID():
    try:
        database = MySQLdb.connect(host="localhost",user="root",passwd="watchmen",db="logindata")
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
        storedPass=str(bcrypt.hashpw(password,salt))
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
    except:
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