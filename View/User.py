import sys 
sys.path.append('..') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import login_required
from Models.User import User
from Models.ErrorCode import *

mod = Blueprint('User', __name__, url_prefix='/user')

@mod.route("/")
def main():
	return "Welcome!"

@mod.route("/login", methods = ["POST"])
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

@mod.route("/register", methods = ["POST"])
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

@mod.route("/info", methods = ["GET"])
@login_required
def tableinfo():
	return jsonify("good for you")