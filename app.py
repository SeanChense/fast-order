import sqlite3, os
import secret_config
from flask import Flask, request
from flask import jsonify
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = secret_config.database_user
app.config['MYSQL_DATABASE_PASSWORD'] = secret_config.database_pass
app.config['MYSQL_DATABASE_DB'] = secret_config.database_name
app.config['MYSQL_DATABASE_HOST'] = secret_config.database_host
mysql.init_app(app)


@app.route("/")
def main():
	return "Welcome!"

@app.route("/login")
def login():
	username = request.args.get('username')
	password = request.args.get('password')

	cursor   = mysql.connect().cursor()
	sql = "SELECT * FROM User WHERE name='" + username + "'\
	AND password='" + password + "'"
	cursor.execute(sql)
	data  = cursor.fetchone()
	if data is None:
		return "username of password is wrong"
	else:
		return "log suss"

@app.route("/register", methods = ["POST"])
def register():
	username = request.form['username']
	password = request.form['password']
	
	if not username or not password:
		return jsonify({"err":1001})
	else:
		return jsonify({"token":"121131"})


if __name__ == "__main__":
	app.run()

