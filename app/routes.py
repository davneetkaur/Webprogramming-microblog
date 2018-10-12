from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="dkaur1"):
    return render_template('hello.html', name=name)
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    ## if form is not validated, display the same form including any error messages.
    if form.validate_on_submit(): ## returns true only if it is a form i.e. "POST" method
        #flash() will display the below info. Flash message is not displayed on the form page but on the next page no matter whatevr it is.
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    else:
        return render_template('login.html', title='Sign In', form=form)