from flask_restful import Resource
from flask.json import jsonify
import pandas as pd
import math

class FighterId(Resource):
    def get(self, id):
        df = pd.read_csv('./scraping/fighters.csv')
        print(df.columns)
        # TODO: add error handling for when csv input is NaN (not a number) using math.isnan()
        fighter = df.loc[df['Unnamed: 0'] == id]
        fighter_name = fighter['FIRST'][id]
        last_name = fighter['LAST'][id]
        wins = fighter['W'][id]
        losses = fighter['L'][id]
        draw = fighter['D'][id]
        return {'first name': fighter_name,
                'last name': last_name,
                'wins': str(wins),
                'losses': str(losses),
                'draws': str(draw)}, 200

class FighterName(Resource):
    def get(self, name):
        df = pd.read_csv('./scraping/fighters.csv')
        name = name.capitalize()
        # TODO: add error handling for when csv input is NaN (not a number) using math.isnan()

        fighter = df.loc[df['FIRST'] == name]
        first_names = fighter['FIRST']
        print(first_names.index.tolist()[0])
        last_names = fighter['LAST'][first_names.index.tolist()[0]]
        names_list = first_names.to_list()
        wins = fighter['W'][first_names.index.tolist()[0]]
        losses = fighter['L'][first_names.index.tolist()[0]]
        draws = fighter['D'][first_names.index.tolist()[0]]
        
        
        return {'message': 'retrieved by name',
        'first name': name,
        'last name': last_names,
        'wins': str(wins),
        'losses': str(losses),
        'draw': str(draws)}, 200