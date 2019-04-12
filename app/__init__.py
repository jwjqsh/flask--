from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_redis import FlaskRedis

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123123@192.168.1.155:3306/movie"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"]="b66addfef5b44e5e88a419c3b617d54c"
app.config["REDIS_URL"] = "redis://123123@127.0.0.1:6379/0"
app.config["UP_DIR"]= os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.config["FC_DIR"]= os.path.join(os.path.abspath(os.path.dirname(__file__)),"static/uploads/")
app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from  app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")













