"""
api.py
~~~~~~~

This module defines a simple REST API for a Machine Learning (ML) model

"""

from flask import Flask, jsonify, request, make_response
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('dtc_model.sav','rb'))

@app.route('/predict', methods=['POST'])
def score():
    ''' Prediction web service'''
    try:
        X = request.json['X']
        prediction = int(model.predict(np.array(X).reshape(1,-1)))
        return make_response(jsonify({'prediction': prediction}))
    except ValueError:
        raise RuntimeError('Error: Features are not in the correct format.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)