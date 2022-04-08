# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request
import numpy as np
import pickle

app =Flask(__name__)
model=pickle.load(open('yattra_modRan.pkl','rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method == 'POST':
        DurationOfPitch = float(request.form['DurationOfPitch'])
        Age = float(request.form['Age'])
        MonthlyIncome = float(request.form['MonthlyIncome'])
        PitchSatisfactionScore =float(request.form['PitchSatisfactionScore'])
        NumberOfTrips = float(request.form['NumberOfTrips'])
        Passport = float(request.form['Passport'])
        
        CityTier = float(request.form['CityTier'])
        
        
        values = np.array([[DurationOfPitch,Age,MonthlyIncome,PitchSatisfactionScore,NumberOfTrips,Passport,CityTier]])
        prediction = model.predict(values)
        
        
        return render_template('result.html',prediction= prediction)
    
if __name__=='__main__':
    app.run(debug=True)
