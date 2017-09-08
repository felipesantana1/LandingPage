from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def displayHtml():
    return render_template('index.html')

@app.route('/ninjas')

def tellMeAboutNinjas():
    return render_template('ninjas.html')

@app.route('/dojo/new')

def myForms():
    return render_template('dojos.html')

app.run(debug=True)
