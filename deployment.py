from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
import numpy as np
import joblib 
import pandas as pd
from wtforms import StringField, SubmitField

app = Flask(__name__)
bootstrap = Bootstrap5(app)
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)