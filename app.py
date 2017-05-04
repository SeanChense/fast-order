import secret_config
from flask import Flask
from flaskext.mysql import MySQL
from flask import render_template
from Models.Restaurant import Restaurant
from Decorator import *


mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = secret_config.database_user
app.config['MYSQL_DATABASE_PASSWORD'] = secret_config.database_pass
app.config['MYSQL_DATABASE_DB'] = secret_config.database_name
app.config['MYSQL_DATABASE_HOST'] = secret_config.database_host
mysql.init_app(app)


from View import User, DinnerTable, Menu, Order, Admin, RestaurantView

app.register_blueprint(User.mod)
app.register_blueprint(DinnerTable.mod)
app.register_blueprint(Menu.mod)
app.register_blueprint(Order.mod)
app.register_blueprint(Admin.mod)
app.register_blueprint(RestaurantView.mod)

@app.route('/', methods = ['GET'])
def index():
	return render_template('index.html')

@app.route('/dashboard', methods = ['GET'])
@superadmin_required
def dashboard(admin):
	rrt = Restaurant.rrt()
	return render_template('dashboard.html', name=admin.name)



if __name__ == "__main__":
	app.run(host="127.0.0.1", port="8080")
	# app.run()

