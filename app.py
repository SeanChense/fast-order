import secret_config
from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = secret_config.database_user
app.config['MYSQL_DATABASE_PASSWORD'] = secret_config.database_pass
app.config['MYSQL_DATABASE_DB'] = secret_config.database_name
app.config['MYSQL_DATABASE_HOST'] = secret_config.database_host
mysql.init_app(app)


from View import User
from View import DinnerTable

app.register_blueprint(User.mod)
app.register_blueprint(DinnerTable.mod)

if __name__ == "__main__":
	app.run()

