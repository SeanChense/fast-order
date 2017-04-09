import sqlite3, os
import secret_config
from Decorator import login_required
from flask import Flask, request
from flask import jsonify
from flaskext.mysql import MySQL

from Models.User import User
from Models.ErrorCode import *


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

@app.route("/user/login", methods = ["POST"])
def login():
	username = request.form['username']
	password = request.form['password']

	user = User.user_filter_name_password(username, password)
	print user
	if user is None:
		resp = { "status":err_password_wrong
		}
		return jsonify(resp)
	else:
		user.generate_auth_token()
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
		return jsonify({"status":err_username_null})
	elif not password:
		return jsonify({"status":err_password_null})
	else:
		user = User(username, password) 
		user.user_save()	
		user.generate_auth_token()
		resp = { "status":0,
		"data" : user.as_dict()
		}
		return jsonify(resp)

@app.route("/user/info", methods = ["GET"])
@login_required
def tableinfo():
	return jsonify("good for you")
if __name__ == "__main__":
	app.run()

