from Cookie import SimpleCookie
from functools import wraps
from flask import g, request, redirect, url_for
from flask import jsonify

from Model.User import User
from Model.Admin import Admin
from Model import ErrorCode



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
		token = request.headers.get('token')
		print token
		if not token:
			return jsonify({"status" : ErrorCode.err_token_null})

		user  = User.verify_auth_token(token)
		if user == -1:
			return jsonify({"status" : ErrorCode.err_token_expired})
		if user == -2 or user == -3:
			return jsonify({"status" : ErrorCode.err_token_invalid})
		return f(user)
    return decorated_function

def superadmin_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		cookie_str = request.headers.get('Cookie')
		token = None
		if cookie_str:
			print "get cookie " + cookie_str
			cookie = SimpleCookie((cookie_str).encode("utf-8"))
			for v in cookie.values():
				if v.key == 'authed':
					token = v.value	
					print "get token " + token
		if not token:
			return jsonify({"status" : ErrorCode.err_token_null})
		admin  = Admin.verify_auth_token(token)
		if admin == -1:
			return jsonify({"status" : ErrorCode.err_token_expired})
		if admin == -2 or admin == -3:
			return jsonify({"status" : ErrorCode.err_token_invalid})

		if admin.permission > 0:
			return jsonify({'status': ErrorCode.err_permission_denied})

		return f(admin)
	return decorated_function

def waiter_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		cookie_str = request.headers.get('Cookie')
		token = None
		if cookie_str:
			print "get cookie " + cookie_str
			cookie = SimpleCookie((cookie_str).encode("utf-8"))
			for v in cookie.values():
				if v.key == 'authed':
					token = v.value	
					print "get token " + token
		if not token:
			return jsonify({"status" : ErrorCode.err_token_null})

		admin  = Admin.verify_auth_token(token)
		if admin == -1:
			return jsonify({"status" : ErrorCode.err_token_expired})
		if admin == -2 or admin == -3:
			return jsonify({"status" : ErrorCode.err_token_invalid})

		if admin.permission > 1:
			return jsonify({'status': ErrorCode.err_permission_denied})

		return f(admin)
	return decorated_function

