from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline
app=Flask(__name__)


@app.route('/')
def home_pagge():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def index():
    os.system("python main.py") 
    return "Training completed!"   

@app.route('/predict', methods=['POST', 'GET'])
def result():
    categoried_1={'Fair':0.0, 'Good':1.0, 'Very Good':2.0, 'Premium':3.0, 'Ideal':4.0}
    clarity_mapping = {'I1':0,'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}
    color_mapping = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
    if request.method == 'POST':
        carat = float(request.form['carat'])
        cut = request.form['cut']
        cut= categoried_1[cut]
        color = request.form['color']
        color = color_mapping[color]
        clarity = request.form['clarity']
        clarity = clarity_mapping[clarity]
        depth = float(request.form['depth'])
        table = float(request.form['table'])
        x = float(request.form['x'])
        y = float(request.form['y'])
        z = float(request.form['z'])
        data=[[carat, cut, color, clarity, depth, table, x, y, z]]
        prediction=PredictionPipeline()
        prediction = prediction.predict(data)
        prediction = np.round(prediction, 4)
    return render_template('result.html',prediction=prediction[0])
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)