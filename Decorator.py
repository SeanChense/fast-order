from functools import wraps
from flask import g, request, redirect, url_for
from flask import jsonify

from Models.User import User
from Models.Admin import Admin
from Models import ErrorCode

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
		token = request.headers.get('token')
		if not token:
			return jsonify({"status" : ErrorCode.err_token_null})

		user  = User.verify_auth_token(token)
		if user == -1:
			return jsonify({"status" : ErrorCode.err_token_expired})
		if user == -2:
			return jsonify({"status" : ErrorCode.err_token_invalid})
		return f(user)
    return decorated_function

def admin_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		token = request.headers.get('token')
		if not token:
			return jsonify({"status" : ErrorCode.err_token_null})

		admin  = Admin.verify_auth_token(token)
		if admin == -1:
			return jsonify({"status" : ErrorCode.err_token_expired})
		if admin == -2:
			return jsonify({"status" : ErrorCode.err_token_invalid})
		return f(admin)
	return decorated_function