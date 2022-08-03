
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here
Config = {
  'apiKey': "AIzaSyDLiUWZo_ozK7uwE5L9wZqJ84bnoBFvt_E",
  'authDomain': "individual-csproject-y2-summer.firebaseapp.com",
  'databaseURL': "https://individual-csproject-y2-summer-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "individual-csproject-y2-summer",
  'storageBucket': "individual-csproject-y2-summer.appspot.com",
  'messagingSenderId': "635400044982",
  'appId': "1:635400044982:web:46634681b877eb97d90117",
  'measurementId': "G-ZJ4QHSE2CM", 'databaseURL':'https://individual-csproject-y2-summer-default-rtdb.europe-west1.firebasedatabase.app/'
  }

firebase= pyrebase.initialize_app(Config)
auth = firebase.auth()  
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
    
       login_session['user'] = auth.sign_in_with_email_and_password(email, password)
       return redirect(url_for('food_page'))

    return render_template("Login.html")



@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        # address = request.form['address']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"full_name": full_name, "email": email}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('food_page'))
        except:
            error = "Authentication failed"
    return render_template("Signup.html")


@app.route('/food_page', methods=['GET', 'POST'])
def food_page():
    return render_template("Food_page.html")

@app.route('/add_review', methods=['GET', 'POST'])
def food_add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        review = {"name":name,"email":email,"message":message}
        db.child("Reviews").push(review)
        x = db.child("Reviews").get().val()


    return render_template("reviews.html", y = x)




@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
   
    x = db.child("Reviews").get().val()


    return render_template("reviews.html", y = x)








#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)