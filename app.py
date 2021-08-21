# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 00:12:09 2021

@author: Saurav
"""

from flask import Flask,render_template,url_for, request
import pickle

pickle_in =  open("Classifier.pkl","rb")
model = pickle.load(pickle_in) 

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/predict',methods = ["POST"])
def predict():
    if request.method == 'POST':
        Variance = request.form['Variance']
        skewness = request.form["skewness"]
        curtosis = request.form["curtosis"]
        entropy = request.form["entropy"]
        my_prediction = model.predict([[Variance,skewness,curtosis,entropy]])
    return render_template('result.html',prediction = my_prediction)
                       
if __name__ == "__main__":
    app.run()