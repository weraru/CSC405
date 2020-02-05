import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request


@app.route('./add', methods=['POST'])
def add_employee():
    try:
        _json = request.json
        _name = _json['name']
        _email = _json['email']

        if _name and _email and request.method == 'POST':
            sql = "INSERT INTO tbl_employee(employee_name, employee_email) VALUES(%s, %s)"
            data = (_name, _email)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Added successfully')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@app.route('/employees')
def employees():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_employee")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/employee/<int:id>')
def employee(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM tbl_employee WHERE employee_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['POST'])
def update_employee():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_email = _json['email']

		if _name and _email and _id and request.method == 'POST':

			sql = "UPDATE tbl_employee SET employee_name=%s, employee_email=%s, WHERE employee_id=%s"
			data = (_name, _email,  _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('employee updated')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>')
def delete_employee(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM tbl_employee WHERE employee_id=%s", (id,))
		conn.commit()
		resp = jsonify('employee deleted')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
		
if __name__ == "__main__":
    app.run()
        

