# Import necessary libraries
from flask import Flask, render_template, request, json
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

# load model
model = load_model("model/model_vgg16.h5")
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "templates", "plant_info.json")
data = json.load(open(json_url))
print('@@ Model loaded')


def pred_cot_dieas(cott_plant):
    test_image = load_img(cott_plant, target_size=(224, 224))  # load image
    print("@@ Got Image for prediction")

    test_image = img_to_array(test_image) / 255  # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis=0)  # change dimention 3D to 4D

    result = model.predict(test_image).round(3)  # predict diseased palnt or not
    print('@@ Raw result = ', result)

    pred = np.argmax(result)  # get the index of max value

    if pred == 0:
        return (0,'leaf_template.html')
    elif pred == 1:
        return (1,'leaf_template.html')
    elif pred == 2:
        return (2,'leaf_template.html')
    elif pred == 3:
        return (3,'leaf_template.html')
    elif pred == 4:
        return (4,'leaf_template.html')
    elif pred == 5:
        return (5,'leaf_template.html')
    elif pred == 6:
        return (6,'leaf_template.html')
    elif pred == 7:
        return (7,'leaf_template.html')
    elif pred == 8:
        return (8,'leaf_template.html')
    elif pred == 9:
        return (9,'leaf_template.html')
    elif pred == 10:
        return (10,'leaf_template.html')
    elif pred == 11:
        return (11,'leaf_template.html')
    elif pred == 12:
        return (12,'leaf_template.html')
    elif pred == 13:
        return (13,'leaf_template.html')
    elif pred == 14:
        return (14,'leaf_template.html')
    elif pred == 15:
        return (15,'leaf_template.html')
    elif pred == 16:
        return (16,'leaf_template.html')
    elif pred == 17:
        return (17,'leaf_template.html')
    elif pred == 18:
        return (18,'leaf_template.html')
    elif pred == 19:
        return (19,'leaf_template.html')
    elif pred == 20:
        return (20,'leaf_template.html')
    elif pred == 21:
        return (21,'leaf_template.html')
    elif pred == 22:
        return (22,'leaf_template.html')
    elif pred == 23:
        return (23,'leaf_template.html')
    elif pred == 24:
        return (24,'leaf_template.html')
    elif pred == 25:
        return (25,'leaf_template.html')
    elif pred == 26:
        return (26,'leaf_template.html')
    elif pred == 27:
        return (27,'leaf_template.html')
    elif pred == 28:
        return (28,'leaf_template.html')
    elif pred == 29:
        return (29,'leaf_template.html')
    elif pred == 30:
        return (30,'leaf_template.html')
    

    # return (5,'leaf_template.html');

# ------------>>pred_cot_dieas<<--end


# Create flask instance
app = Flask(__name__)


# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html')


# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['image']  # fet input
        filename = file.filename
        print("@@ Input posted = ", filename)

        file_path = os.path.join('static/user uploaded', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_cot_dieas(cott_plant=file_path)

        return render_template(output_page, pred_output=pred, user_image=file_path, data = data)


# For local system &amp; cloud
if __name__ == "__main__":
    app.run(threaded=False)
