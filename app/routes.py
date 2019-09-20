from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/files')
def files():
    return render_template('files.html', title='Files')

@app.route('/symbols')
def symbols():
    return render_template('symbols.html', title='Symbols')

@app.route('/xml')
def xml():
    
    return render_template('xml.html', title='XML')    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash(f'这是一条消息闪现包含值{form.username.data}和{form.remember_me.data}')
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
