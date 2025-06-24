from flask import Flask, request, render_template, redirect, url_for
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
model_path = "C:/Users/rahul/OneDrive/Desktop/mini project/sugarcane-app/sugarcane_leaf_model.h5"
model = tf.keras.models.load_model(model_path)

# Define class names as per your dataset
class_names = ['Diseases', 'Dried', 'Healthy']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    # Read the image
    image = Image.open(file.stream)
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Predict
    predictions = model.predict(image)
    class_idx = np.argmax(predictions[0])
    predicted_class = class_names[class_idx]

    return render_template('result.html', predicted_class=predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
