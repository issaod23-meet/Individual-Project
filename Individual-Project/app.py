from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

Config = {
  "apiKey": "AIzaSyDLiUWZo_ozK7uwE5L9wZqJ84bnoBFvt_E",
  "authDomain": "individual-csproject-y2-summer.firebaseapp.com",
  "databaseURL": "https://individual-csproject-y2-summer-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "individual-csproject-y2-summer",
  "storageBucket": "individual-csproject-y2-summer.appspot.com",
  "messagingSenderId": "635400044982",
  "appId": "1:635400044982:web:46634681b877eb97d90117",
  "measurementId": "G-ZJ4QHSE2CM",
  "databaseURL":"https://individual-csproject-y2-summer-default-rtdb.europe-west1.firebasedatabase.app"
  }

firebase= pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("Login.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("Signup.html")








#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)