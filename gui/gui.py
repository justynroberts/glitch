from flask import Flask,render_template,request,redirect
from flask_login import login_required, current_user, login_user, logout_user
from flask_login.utils import _secret_key
from models import UserModel,db,login,triggerModel,experimentModel,configModel

from flask_cors import CORS
app = Flask(__name__)


app.secret_key = ('welcometoglitch')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///glitch.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db.init_app(app)
login.init_app(app)
login.login_view = 'login'

@app.before_first_request
def create_all():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main')
@login_required
def experiments():
    return render_template('experiments.html')

@app.route('/setup')
@login_required
def setup():
    return render_template('setup.html')


@app.route('/rules')
@login_required
def rules():
    return ('json')




 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect('/main')
     
    if request.method == 'POST':
        email = request.form['email']
        user = UserModel.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/main')
     
    return render_template('login.html')
 
@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        if email == "" or username =="" or password =="":
            return ()
        if UserModel.query.filter_by(email=email).first():
            return ('Email already Present')
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

app.run(host='localhost', port=5000)
