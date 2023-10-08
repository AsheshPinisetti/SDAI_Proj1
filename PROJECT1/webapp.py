#!/usr/bin/env python3
from flask import Flask, render_template, request
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

# Define the path to your SavedModel directory
saved_model_path = "my_model"

# Load the SavedModel and specify input/output names
model = tf.saved_model.load(saved_model_path)

# Define a function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))
    image_array = np.array(image, dtype=np.float32) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

# Define a function to check if the file extension is allowed
def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Define routes
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        uploaded_file = request.files.get("imagefile")

        if uploaded_file and allowed_file(uploaded_file.filename):
            try:
                # Open and preprocess the image using PIL
                image = Image.open(uploaded_file)
                preprocessed_image = preprocess_image(image)

                # Make predictions
                predictions = model.signatures["serving_default"](tf.constant(preprocessed_image, dtype=tf.float32))
                predicted_probabilities = predictions['dense_2'][0]  # Extract the probability values
                predicted_class_index = np.argmax(predicted_probabilities)  # Find the index with the highest probability
                predicted_class_probability = predicted_probabilities[predicted_class_index]  # Get the probability of the predicted class

                # Calculate the percentage (multiply by 100)
                predicted_class_percentage = predicted_class_probability * 100

                # Provide the prediction as a string
                prediction = f'The leaf prediction is class {predicted_class_index} at {predicted_class_percentage:.2f}%'
            except Exception as e:
                prediction = f'Error: {str(e)}'
        else:
            prediction = "ERROR! Invalid file format."

    return render_template("index.html", prediction=prediction)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
