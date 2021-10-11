from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse, request
from Handlers.FightersHandler import FighterId, FighterName
from Handlers.FightersListHandler import FightersListApi


app = Flask(__name__)
app_api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

app_api.add_resource(FighterId, '/api/v1/fighters/<int:id>')
app_api.add_resource(FighterName, '/api/v1/fighters/<name>')
app_api.add_resource(FightersListApi, '/api/v1/fighters')

if __name__ == '__main__':
    app.run(port=5050)