# sugarane-leaf-disease-detection

This project is a machine learning-based approach to detect diseases in sugarcane leaves. It uses a ResNet50 model for classification.

## Project Structure

- `app.py`: Python file for running the web app.
- `templates/`: Folder containing HTML files (`index.html` and `result.html`).
- `venv/`: Virtual environment for managing dependencies.

## How to Use

### Requirements

- Python 3.x
- Flask
- TensorFlow
- Keras
- Git LFS (for large model files)

### Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Rahulmariyappagoudar/sugarane-leaf-disease-detetion.git
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Activate virtual environment** (optional):
    ```bash
    venv\Scripts\activate       # For Windows
    ```

### Training and Validation

To train and validate the model using your own dataset:
1. Prepare your dataset with images categorized into appropriate folders (e.g., Healthy, Diseased, etc.).
2. Modify the `app.py` script or create a new training script to load and preprocess your dataset.
3. Train the model and save it in `.h5` format.

### Running the App

1. Run the web application using Flask:
    ```bash
    python app.py
    ```
2. Visit the application in your browser at `http://127.0.0.1:5000/`.

## License

This project is licensed under the MIT License.
