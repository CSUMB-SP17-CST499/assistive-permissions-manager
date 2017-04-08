import flask, os

from flask import render_template, flash, request, json, make_response
from hashlib import md5

from views.roles import roles
from views.employees import employees
from db.database import init_db, Session 
from db import query, hashPassword, models
from db.models import User


app = flask.Flask(__name__)
app.register_blueprint(roles)
app.register_blueprint(employees)

# Initalize the database
init_db()

@app.route('/')
def index():
    # If there is no userName, then route to loginScreen. Else, route to the main page.
    return flask.render_template("index.html")


@app.route('/showcreateaccount')
def showcreateaccount():
    return render_template("createAccount.html")


@app.route('/createaccount', methods=['POST'])
def createaccount():

    if request.method == 'POST':
        data = request.get_json()
        
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        is_admin = data.get('is_admin')

        if firstname and lastname and email and username and password:
            
            if query.does_user_email_exist(email):
                resp = json.dumps({'message': 'The entered email is already in use.' +
                        ' Please entere a different one.'})
                return (resp, 400)
                
            else: 
                #creates a password hash to store in the database 
                hashpassword = hashPassword(password)
                hashpassword.set_password(password)
                user = User(firstname, lastname, email, username, hashpassword, is_admin)
                query.add_user(user)
                flask.redirect('/login')
          
        else:
            resp = json.dumps({'message': 'There is a missing field. ' +
                    'Please fill all required fields'})
            return (resp, 400)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        if username and password:
            if query.is_usermane_correct(username):
                if query.is_password_correct(password):
                    resp = json.dumps({'message': 'You have logd in'})
                    return flask.redirect('/')
        if False:
            error = 'Unkown error. Please contact support.'
        else:
             resp = json.dumps({'message': 'you have not entereted the correct details'})
             return (resp, 400)

    return flask.render_template('login.html', message = error)


@app.route('/add')
def addEmp():
    # data = request.get_json()
        
    # firstname = data.get('firstname')
    # lastname = data.get('lastname')
    # email = data.get('email')
    # role = data.get('role')
    return flask.render_template("add.html")


@app.route('/employee')
def empGroup():
    return flask.render_template("employee.html")


@app.route('/edits')
def edits():
    return flask.render_template("edits.html")


@app.teardown_appcontext
def shutdown_session(exception = None):
    Session.remove()


if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
    )
