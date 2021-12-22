import json

settings_file = open('./data/settings.json')
settings_data = json.load(settings_file)
numberOfQuestions = settings_data['settings'][0]['numberOfQuestions']
depName  = settings_data['settings'][0]['depName']
schoolName  = settings_data['settings'][0]['schoolName']