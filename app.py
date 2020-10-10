import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('strength.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[int(x) for x in request.form.values()]]
    
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0][0]
    if(output > 0.5):
        result = "You have high possibility of Diabetes of"
    else:
        result = "You have less possibility of Diabetes of"
    output = output * 100
    #result = result + " " +
    return render_template('index.html', prediction_text=  result + " " + '{:.2f}'.format(output)+"%")
if __name__ == "__main__":
    #website_url = 'diabetes_prediction : 5000'
    #app.config['SERVER_NAME'] = website_url
    app.run(debug = True)
