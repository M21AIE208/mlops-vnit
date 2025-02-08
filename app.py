import time

from flask import Flask, request, jsonify
import pickle
import numpy
from sklearn.tree import DecisionTreeClassifier

#initialise the Flask app
app = Flask(__name__)

with open("./model/iris_classifier.pkl","rb") as f:
    clf = pickle.load(f)

@app.route("/get_status", methods=["GET"])
def foo():
    time.sleep(2)
    return {"training":70,"testing":30}

@app.route("/prediction", methods=["POST"])
def prediction():
    payload = request.json
    X_unknown = [payload["sepal-lenght"],payload["sepal-width"],payload["petal-lenght"],payload["petal-width"]]
    X_unknown = numpy.array(X_unknown).reshape(1,-1)
    prediction = clf.predict(X_unknown)
    return jsonify({"predicted_value":prediction[0]})

@app.route("/training", methods=["GET"])
def training():
    """fill your code here"""


if __name__ == "__main__":
    app.run(port=5002)
