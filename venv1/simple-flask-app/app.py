import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/how are you")
def hello():
    return 'I am good, how about you?'

if __name__=="__main__":
    app.run()

"""
ubuntu it session commands used to create Dockerfile

docker run -it ubtunu bash
apt update
apt install -y python
apt install -y python3-pip
pip install flask
apt install nano
copy app.py /opt/app.py

FLASK_APP=/opt/app.py flask run --host=0.0.0.0

"""