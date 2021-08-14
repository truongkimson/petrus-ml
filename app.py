from flask import Flask, request
from flask_cors import CORS
import pickle

with open('adoption_speed.model', 'rb') as f:
    model = pickle.load(f)


app = Flask(__name__)
CORS(app)

@app.route('/api/adoption-speed', methods=['POST'])
def adoption_speed():
    input = request.json
    print('\n Request:\n', input, '\n')
    pred = round(model.predict([[input.get('age'), input.get('notVaccinated'), input.get('notSterilized')]])[0])
    
    if pred == 0:
        return "Pet likely to be adopted on the same day"
    elif pred == 1:
        return "Pet likely to be adopted within the first week"
    elif pred == 2:
        return "Pet likely to be adopted within first month"
    elif pred == 3:
        return "Pet likely to be adopted within first 90 days"
    else:
        return "Pet likely to be adopted after 90 days"
