from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
login = LoginManager()

db = SQLAlchemy()
class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String())
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))

#---------------------------
class triggerModel(db.Model):
    __tablename__ = "triggers"

    trigger_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, trigger_id,name,age,position):
        self.trigger_id = trigger_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.trigger_id}"

#---------------------------

class experimentModel(db.Model):
    __tablename__ = "experiments"

    experiment_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, experiment_id,name,age,position):
        self.experiment_id = experiment_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.experiment_id}"

#---------------------------
class configModel(db.Model):
    __tablename__ = "config"

    config_id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self, config_id,name,age,position):
        self.config_id = config_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.config_id}"
