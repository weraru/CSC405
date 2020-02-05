from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

#Configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Isawasquirrel1'
app.config['MYSQL_DATABASE_DB'] = 'MYSQL80'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306

mysql.init_app(app)