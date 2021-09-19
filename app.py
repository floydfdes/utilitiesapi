from flask import Flask
from flask import request
from flask_cors import CORS
# from flask_restplusrestplus import Api, Resource, fields
import pickle
import numpy as np
import json

app = Flask(__name__)
CORS(app)
model = pickle.load(open('RandomForestGridModel.pkl', 'rb'))


@app.route('/')
def home():
    return '<h1>Welcome to flask api</h1>'


@app.route('/heartdisease', methods=['POST'])
def predict_outcome():
    data = request.json
    data_array = np.array([data])
    outcome = model.predict(data_array)
    print(outcome)
    if outcome == 1:
        prediction = "You have heart disease"
    else:
        prediction = "You dont have heart disease"
    dictionary = {'prediction': prediction}
    json_string = json.dumps(dictionary, indent=4)
    return json_string


@app.route('/binaryimagedetection', methods=['POST'])
def image_api():
    image_file = request.files['image']
    image_path = "./images/" + 'cats1.jpeg'
    image_file.save(image_path)
    return "success"


if __name__ == '__main__':
    app.run(debug=True, port=5000)
