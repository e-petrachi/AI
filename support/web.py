# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 19:13:04 2017

@author: Claudio
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

if __name__ == "__main__":
	app.run()