from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()