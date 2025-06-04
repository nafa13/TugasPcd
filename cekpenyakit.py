from flask import Flask, render_template, request
import os
import cv2
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy deteksi penyakit (nanti bisa diganti model)
def deteksi_penyakit(filepath):
    img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img_resized = cv2.resize(img, (128, 128))
    mean_intensity = np.mean(img_resized)
    if mean_intensity < 100:
        return "Kemungkinan Tumor Terdeteksi"
    else:
        return "Citra Otak Normal"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "Tidak ada file diunggah"

    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    result = deteksi_penyakit(filepath)
    return render_template('result.html', result=result, filename=file.filename)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
