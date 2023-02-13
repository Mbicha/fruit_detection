#!/usr/bin/env python3

import os
from flask import Flask, render_template, request, url_for
from utils import classify_fruit


app = Flask(__name__)

image_folder = os.path.join('static', 'images')
app.config["UPLOAD_FOLDER"] = image_folder

@app.route("/", methods=['GET'], strict_slashes=False)
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'], strict_slashes=False)
def predict():
    fruit_image = request.files['fruit_image']
    img_path = "./static/images/" + fruit_image.filename

    fruit_image.save(img_path)

    img = os.path.join(app.config['UPLOAD_FOLDER'], fruit_image.filename)

    image_size = 100
    prediction = classify_fruit(img_path, image_size)
    return render_template('index.html', pic=img, prediction=prediction)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
