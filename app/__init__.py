from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "235EWewr346f3534764"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
login_manager = LoginManager(app=app)

admin = Admin(app=app, name="QUAN LY KHACH SAN", template_mode="bootstrap4")