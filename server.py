from flask import Flask
from flask import jsonify
import connexion

from api.Vectorizer import Vectorizer
from api.PasswordClassifier import PasswordClassifier

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("main.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "Server active!"}
    return jsonify(msg)


if __name__ == "__main__":
    # localhost:8080 for Docker
    app.run(host="0.0.0.0", port=8080, debug=True)

