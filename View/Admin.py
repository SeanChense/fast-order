import sys 
sys.path.append('/home/ubuntu/work/fast-order') 

from flask import Flask, request, Blueprint
from flask import jsonify
from Decorator import login_required
from Models.Admin import Admin
from Models.ErrorCode import *

mod = Blueprint('Admin', __name__, url_prefix='/admin')

@mod.route("/")
def main():
	return "Welcome to admin!"

@mod.route("/login", methods = ["POST"])
def login():
	username = request.form['username']
	password = request.form['password']

	admin = Admin.admin_filter_name_password(username, password)
	print admin
	if admin is None:
		resp = { "status":err_password_wrong
		}
		return jsonify(resp)
	else:
		admin.generate_auth_token()
		data = admin.as_dict()
		del data["password"]

		resp = { "status":0,
		"data" : data
		}
		return jsonify(resp)	