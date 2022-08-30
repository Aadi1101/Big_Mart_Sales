from flask import Flask, jsonify, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def result():
    item_weight = float(request.form["item_weight"])
    item_fat_weight = float(request.form["item_fat_content"])
    item_visibility = float(request.form["item_visibility"])
    item_type = float(request.form["item_type"])
    item_mrp = float(request.form["item_mrp"])
    outlet_establishment_year = float(request.form["outlet_establishment_year"])
    outlet_size = float(request.form["outlet_size"])
    outlet_location_type = float(request.form["outlet_location_type"])

    x= np.array([[item_weight,item_fat_weight,item_visibility,item_type,item_mrp,outlet_establishment_year,outlet_size,outlet_location_type]])

    model = joblib.load("./models/regressor.sav")
    y_pred = model.predict(x)
    output = y_pred[0]
    return render_template('predict.html',pred="Prediction of Outlet Sales is {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
 