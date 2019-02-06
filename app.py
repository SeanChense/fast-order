from flask import Flask, redirect
from flaskext.mysql import MySQL
from flask import render_template
from Model.Restaurant import Restaurant
from Model.Admin import Admin
from Decorator import *
from Cookie import SimpleCookie
import json
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = './upload/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# mysql = MySQL()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MYSQL_DATABASE_USER'] = secret_config.database_user
# app.config['MYSQL_DATABASE_PASSWORD'] = secret_config.database_pass
# app.config['MYSQL_DATABASE_DB'] = secret_config.database_name
# app.config['MYSQL_DATABASE_HOST'] = secret_config.database_host
# mysql.init_app(app)


from View import User, DinnerTable, Menu, Order, AdminView, RestaurantView, image_helper

app.register_blueprint(User.mod)
app.register_blueprint(DinnerTable.mod)
app.register_blueprint(Menu.mod)
app.register_blueprint(Order.mod)
app.register_blueprint(AdminView.mod)
app.register_blueprint(RestaurantView.mod)
app.register_blueprint(image_helper.mod)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({
                "status":0
            })
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
# def index():
# 	cookie_str = request.headers.get('Cookie')
# 	token = None
# 	if cookie_str:
# 		print ("get cookie " + cookie_str)
# 		cookie = SimpleCookie((cookie_str).encode("utf-8"))
# 		for v in cookie.values():
# 			if v.key == 'authed':
# 				token = v.value	
# 				print ("get token " + token)
# 	if token:
# 		admin  = Admin.verify_auth_token(token)
# 		if admin != -1 and \
# 		   admin != -2 and \
# 		   admin != -3:
# 		   return redirect('/dashboard', code=302)
# 	return render_template('index.html')

# @app.route('/dashboard', methods = ['GET'])
# @superadmin_required
# def dashboard(admin):
# 	rrt = Restaurant.rrt()
# 	return render_template('dashboard.html', name=rrt.name)



if __name__ == "__main__":
	# app.run(host="0.0.0.0", port="8080")
	app.run(host="127.0.0.1", port="8080")

