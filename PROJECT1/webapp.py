#!/usr/bin/env python3
'''
here are the library we will be using for the deplyement of teh model
'''
from flask import Flask, render_template, request, jsonify
import os
from PIL import Image
import numpy as np
import pickle

app = Flask(__name__)

# Load pickle model 
# Load the pre-trained model
with open('/models/model.pkl', 'rb') as model_file:
	loaded_model = pickle.load(model_file)

# Define a function to preprocess the image
def preprocess_image(image):
	# Resize the image to match the input size of the model (e.g., 224x224 for many image classification models)
	image = image.resize((224, 224))
	
	# Convert the image to a NumPy array
	image_array = np.array(image)
	
	# Preprocess the image data (you may need to adapt this preprocessing based on your model)
	image_array = image_array / 255.0  # Normalize pixel values to [0, 1]
	image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
	return image_array

def allowed_file(filename):
	# Define a list of allowed image extensions
	allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


'''
Load the first page first
'''
@app.route("/", methods=["GET"])
def Home():
	return render_template('index.html')

'''
Predict the picture inserted
'''
@app.route("/", methods=['POST'])
def predict():
	uploaded_file = request.files.get("imagefile")
	if uploaded_file and allowed_file(uploaded_file.filename):
		# Open and preprocess the image using PIL
		image = Image.open(uploaded_file)
		preprocessed_image = preprocess_image(image)
		# Make a prediction using the loaded model
		predictions = model.predict(preprocess_image)
		prediction = f'The leaf prediction is {predictions}'
	else:
		prediction = "ERROR! file"
		
	return render_template("index.html", prediction= prediction)


if __name__ == '__main__':
	app.run(port=3000, debug=True)
	