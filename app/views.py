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

@app.route('/yo')
def yo():
    title = {'title': 'Yo'}
    return render_template('yo.html', title=title)

@app.route('/freshpatterns')
def freshpatterns():
    title = {'title': 'Fresh Patterns'}
    return render_template('freshpatterns.html', title=title)

@app.route('/makemecoffee')
def makemecoffee():
    title = {'title': 'MakeMeCoffee'}
    return render_template('makemecoffee.html', title=title)

@app.route('/primerpeso')
def primerpeso():
    title = {'title': 'Primer Peso'}
    return render_template('primerpeso.html', title=title)

@app.route('/civchoice')
def civchoice():
    title = {'title': 'CivChoice'}
    return render_template('civchoice.html', title=title)

@app.route('/colorchart')
def colorchart():
    title = {'title': 'Color Chart'}
    return render_template('colorchart.html', title=title)

@app.route('/tiles')
def tiles():
    title = {'title': 'Tiles'}
    return render_template('tiles.html', title=title)

@app.route('/ilovepr')
def ilovepr():
    title = {'title': 'I Love Puerto Rico'}
    return render_template('ilovepr.html', title=title)
