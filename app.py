# Import Libraries
from flask import Flask, request, render_template

import model  # load model.py

app = Flask(__name__, template_folder='template')


# render html page
@app.route('/')
def home():

    return render_template('index.html')


# get user input, and they predict the output and return to user
@app.route('/predict', methods=['POST'])
def predict():
    # take data from form and store in each feature
    input_features = [x for x in request.form.values()]
    location = input_features[0]
    bhk = input_features[1]
    total_sqft_int = input_features[2]
    price_per_sqft = input_features[3]
    availability = input_features[4]

    # predict the price of house by calling model.py
    predicted_price = model.predict_house_price(location, bhk, total_sqft_int, price_per_sqft, availability)

    # render the html page and show the output
    return render_template('index.html',
                           prediction_text='Predicted Price of House is {} Lakh.'.format(predicted_price))


# if _name_ == "_main_":
#     app.run(host="0.0.0.0", port="8080")

if __name__ == "__main__":
    app.run(debug=True, port=5003)