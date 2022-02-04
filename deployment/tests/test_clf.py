import pandas as pd
import numpy as np
from numpy import ndarray, int64
from sklearn.pipeline import Pipeline
from sklearn.compose._column_transformer import ColumnTransformer
import joblib
import os, glob

os.chdir('..')
print(os.getcwd())
model = joblib.load(glob.glob('*.pkl')[0])

def test_accuracy():
    ''' Test model accuracy by scoring it on a sample of the training data'''
    train_df = pd.read_csv("../experimentation/datasets/train.csv")
    features = list(train_df.columns)
    features.remove('Survived')
    X_test, y_test = train_df.iloc[-100:][features], train_df.iloc[-100:]['Survived']
    acc = model.score(X_test,y_test)
    assert acc >= 0.85

def test_pipeline():
    ''' Test if the model is a sklearn.pipeline and includes a data pre-processing step'''
    assert isinstance(model, Pipeline)
    first_step  = [v for v in model.named_steps.values()][0]
    assert isinstance(first_step, ColumnTransformer)

def test_prediction():
    ''' Test if predictions are of correct format, data type, values and without nans'''
    X_pred = pd.read_csv("../experimentation/datasets/test.csv").iloc[:10]
    preds = model.predict(X_pred)
    assert isinstance(preds, ndarray)
    assert isinstance(np.sum(preds),int64)
    assert len(preds) == 10
    assert preds[0] in [0,1]