from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    title = {'title': 'Ainsley Wagoner'}
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = {'title': 'About Me'}
    return render_template('about.html', title=title)

@app.route('/resume')
def resume():
    title = {'title': 'My Resume'}
    return render_template('resume.html', title=title)
