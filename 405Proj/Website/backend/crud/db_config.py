from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

#Configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Isawasquirrel1'
app.config['MYSQL_DATABASE_DB'] = 'hold'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)