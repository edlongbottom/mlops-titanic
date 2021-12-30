"""
api.py
~~~~~~~

This module defines a simple REST API for a Machine Learning (ML) model

"""

from flask import Flask, jsonify, request, make_response
import pandas as pd
from yaml import load, Loader
import joblib
import glob

with open('config.yaml','r') as config_file:
    config = load(config_file, Loader=Loader)

service_name = config['SERVICE_NAME']
api_version = config['API_VERSION']

app = Flask(__name__)

model = joblib.load(glob.glob('*.pkl')[0])

@app.route(f'/{service_name}/v{api_version}/predict', methods=['POST'])
def score():
    ''' Prediction web service'''
    try:
        X_inf = pd.DataFrame(request.json)
        scores = model.predict(X_inf).tolist()
        return make_response(jsonify({'predictions': scores}))
    except ValueError:
        raise RuntimeError('Error: Features are not in the correct format.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)