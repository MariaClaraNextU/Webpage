# File: Views.py
# Author: María Clara De La Cuesta
# Project: Webpage

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return

if __name__ == "__main__":
    app.run()