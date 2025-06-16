from flask import Flask, request, jsonify, url_for, render_template
import os
import cv2
import numpy as np
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def remove_moving_objects_variance(filenames, var_threshold=10):
    images = []
    for f in filenames:
        img = cv2.imread(f)
        if img is None:
            raise ValueError(f"Nie udało się wczytać obrazu: {f}")
        images.append(img)

    h, w = images[0].shape[:2]
    for i in range(1, len(images)):
        if images[i].shape[:2] != (h, w):
            images[i] = cv2.resize(images[i], (w, h))

    stack = np.stack(images, axis=0).astype(np.float32)  # (N, H, W, 3)

    mean_img = np.mean(stack, axis=0)
    std_img = np.std(stack, axis=0)

    mask = std_img < var_threshold  # stabilne piksele

    result = np.zeros_like(mean_img, dtype=np.uint8)

    for c in range(3):
        channel_mean = mean_img[:, :, c]
        channel_median = np.median(stack[:, :, :, c], axis=0)
        channel_mask = mask[:, :, c]

        channel_result = np.where(channel_mask, channel_mean, channel_median)
        result[:, :, c] = channel_result.astype(np.uint8)

    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        uploaded_files = request.files.getlist('images')
        if len(uploaded_files) < 2:
            return jsonify({'error': 'Wybierz minimum 2 zdjęcia'}), 400

        filenames = []
        for file in uploaded_files:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            filenames.append(filepath)

        start_time = time.time()
        result_img = remove_moving_objects_variance(filenames)
        duration = time.time() - start_time
        print(f'Przetwarzanie trwało {duration:.2f} sekund')

        result_path = os.path.join(RESULT_FOLDER, 'result.png')
        cv2.imwrite(result_path, result_img)

        return jsonify({'result_image': url_for('static', filename='result.png'), 'processing_time': f'{duration:.2f} s'})

    except Exception as e:
        print('Błąd:', e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
