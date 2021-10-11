from flask_restful import Resource
import pandas as pd

class FightersListApi(Resource):
    def get(self):
        return {'message' : 'returned whole list'}, 200