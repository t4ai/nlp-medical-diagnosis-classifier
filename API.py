# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 11:03:14 2023

@author: test
"""

from flask import Flask, request, jsonify
import pickle
from sklearn.preprocessing import FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import joblib
import nltk
import numpy as np
import pandas as pd
from nltk.corpus import stopwords

app = Flask(__name__)
def string_clean(df, column_name):
    
        # remove punctuation marks
        punctuation = '!"#$%&()*+-/:;<=>?@[\\]^_`{|}~'
        df[column_name] = df[column_name].apply(lambda x: ''.join(ch for ch in x if ch not in set(punctuation)))
    
        # convert text to lowercase
        df[column_name] = df[column_name].str.lower()
    
        # remove numbers
        df[column_name] = df[column_name].str.replace("[0-9]", " ", regex=True)
    
        # remove whitespaces
        df[column_name] = df[column_name].apply(lambda x:' '.join(x.split()))
    
        return df
    
def remove_stop_words(df, column_name):
        nltk.download('stopwords', quiet=True) 
        stop = stopwords.words('english')
        df[column_name] = df[column_name].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
        return df
    
def preprocess_text(text_arr):
        temp_df = pd.DataFrame({'text': text_arr})
        temp_df = string_clean(temp_df, 'text')
        temp_df = remove_stop_words(temp_df, 'text')
        return temp_df['text'].to_numpy()
class TextPreprocessTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = preprocess_text(X)
        return X
with open('nbc_model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)



@app.route('/predict', methods=['POST'])
def predict_disease():
    try:
        data = request.json['data']  # Assuming you send input data as JSON
        prediction = model.predict([data])  # Make prediction using the ML model
        result = {'prediction': prediction[0]}
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8080)

    
    