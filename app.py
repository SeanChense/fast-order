import sqlite3, os
import secret_config
from flask import Flask, request
from flask import jsonify
from flaskext.mysql import MySQL

from Models import Model
from Models import ErrorCode

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = secret_config.database_user
app.config['MYSQL_DATABASE_PASSWORD'] = secret_config.database_pass
app.config['MYSQL_DATABASE_DB'] = secret_config.database_name
app.config['MYSQL_DATABASE_HOST'] = secret_config.database_host
mysql.init_app(app)

session = Model.session

@app.route("/")
def main():
	return "Welcome!"

@app.route("/user/login", methods = ["POST"])
def login():
	username = request.form['username']
	password = request.form['password']

	user = session.query(Model.User).filter(Model.User.name == username, Model.User.password == password).first()
	print user
	if user is None:
		resp = { "status":ErrorCode.err_password_wrong
		}
		return jsonify(resp)
	else:
		data = user.as_dict()
		del data["password"]

		resp = { "status":0,
		"data" : data
		}
		return jsonify(resp)

@app.route("/user/register", methods = ["POST"])
def register():
	username = request.form['username']
	password = request.form['password']
	
	if not username:
		return jsonify({"status":ErrorCode.err_username_null})
	elif not password:
		return jsonify({"status":ErrorCode.err_password_null})
	else:
		return jsonify({"token":"121131"})


if __name__ == "__main__":
	app.run()

