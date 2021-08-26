from flask import Flask, request
from flask_cors import CORS
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('ModelV3-Neural network/saved_model/adoption_speed_v3')
print(model.summary())

app = Flask(__name__)
CORS(app)

@app.route('/api/adoption-speed', methods=['POST'])
def adoption_speed():
    input = request.json
    print('\n Request:\n', input, '\n')

    print([
        input.get('type'),
        0,
        input.get('age'),
        input.get('gender'),
        input.get('maturitySize'),
        input.get('furLength'),
        input.get('qty'),
        input.get('fee'),
        1,
        input.get('desc'),
        1,
        int(input.get('color1') == 1),
        int(input.get('color1') == 2),
        int(input.get('color1') == 3),
        int(input.get('color1') == 4),
        int(input.get('color1') == 5),
        int(input.get('color1') == 6),
        int(input.get('vaccinated') == 1),
        int(input.get('vaccinated') == 2),
        int(input.get('dewormed') == 1),
        int(input.get('dewormed') == 2),
        int(input.get('sterilized') == 1),
        int(input.get('sterilized') == 2),
        int(input.get('health') == 1),
        int(input.get('health') == 2)
    ])

    pred = model.predict([[input.get('type'),
    0,
    input.get('age'),
    input.get('gender'),
    input.get('maturitySize'),
    input.get('furLength'),
    input.get('qty'),
    input.get('fee'),
    1,
    input.get('desc'),
    1,
    int(input.get('color1_2') == 1),
    int(input.get('color1_3') == 2),
    int(input.get('color1_4') == 3),
    int(input.get('color1_5') == 4),
    int(input.get('color1_6') == 5),
    int(input.get('color1_7') == 6),
    int(input.get('vaccinated_2') == 1),
    int(input.get('vaccinated_3') == 2),
    int(input.get('dewormed_2') == 1),
    int(input.get('dewormed_3') == 2),
    int(input.get('sterilized_2') == 1),
    int(input.get('sterilized_3') == 2),
    int(input.get('health_2') == 1),
    int(input.get('health_3') == 2)]])[0]

    cat = np.argmax(pred)
    print(cat)
   
    if cat == 0:
        return "Pet likely to be adopted on the same day"
    elif cat == 1:
        return "Pet likely to be adopted within the first week"
    elif cat == 2:
        return "Pet likely to be adopted within first month"
    elif cat == 3:
        return "Pet likely to be adopted within first 90 days"
    else:
        return "Pet likely to be adopted after 90 days"
