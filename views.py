# File: Views.py
# Author: Maria Clara De La Cuesta
# Project: Webpage

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():

    return render_template('index.html')
 
@app.route('/<string:name>')
def welcome(name):

    return render_template('welcome.html', name=name)
    
if __name__ == "__main__":
    app.run()