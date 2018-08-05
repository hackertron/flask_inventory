from flask import Flask
from flask_mysqldb import MySQL
import sys

# placeholder for current module
app = Flask(__name__)


#config MySql
app.config.from_pyfile('config.py')

# init MYSQL
mysql = MySQL(app)

# import views
from views import *



if __name__ == '__main__':
    app.run()
