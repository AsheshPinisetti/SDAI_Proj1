# SDAI_Proj1
# Image Classification Flask Application

This is a simple Flask web application for image classification using a pre-trained deep learning model. Users can upload an image, and the application will classify it using the pre-trained model and display the results.

## Prerequisites

Before running this application, you need to have the following installed:

- Python 3.x
- Flask
- Pillow (PIL)
- NumPy

You can install the required Python packages using pip:
```
pip install Flask Pillow numpy
```

## Usage

1. Clone this repository to your local machine:
   	```
	git clone https://github.com/AsheshPinisetti/SDAI_Proj1.git
	cd SDAI_Proj1
	```

3. Create a virtual environment (optional but recommended):
	```
	python -m venv venv
	```

4. Activate Environment
	On Windows:
	```
	venv\Scripts\activate
	```
	
	On macOS and Linux:
	```
	source venv/bin/activate
	```
5. Run the Flask App
	```
	python webapp.py
	 ```

	Access the application in your web browser by navigating to http://localhost:3000.

	Upload an image and click the "Classify" button to see the classification result.

## Customization

Model: You should replace the placeholder code for loading and using the pre-trained model in app.py with your actual model loading and classification code.

Preprocessing: Modify the preprocess_image function in app.py to match the preprocessing requirements of your model.

Output Formatting: Adjust the code for converting model output to a human-readable format based on your model's output structure and labels.

HTML Templates: Customize the HTML templates in the templates folder to match your application's design.

## Acknowledgments

- Flask
- Pillow (PIL)
- NumPy

