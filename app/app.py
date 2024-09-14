from flask import Flask, request, send_file, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from PIL import Image
import logging

app = Flask(__name__)

# Use absolute paths for directories
UPLOAD_FOLDER = os.path.abspath('app/uploads')
COMPRESSED_FOLDER = os.path.abspath('app/compressed')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['COMPRESSED_FOLDER'] = COMPRESSED_FOLDER

# Ensure the upload and compressed folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(COMPRESSED_FOLDER, exist_ok=True)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Compress image function
def compress_image(original_filepath, compressed_path):
    with Image.open(original_filepath) as img:
        img = img.convert("RGB")
        img.save(compressed_path, "JPEG", quality=85)
        logging.debug(f"Compressed image saved at: {compressed_path}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['image']
    if file.filename == '':
        return redirect(url_for('index'))
    
    if file and file.filename.lower().endswith(('png', 'jpg', 'jpeg')):
        filename = secure_filename(file.filename)
        original_filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(original_filepath)
        logging.debug(f"Original file saved at: {original_filepath}")
        
        compressed_filename = os.path.splitext(filename)[0] + ".jpg"
        compressed_path = os.path.join(app.config['COMPRESSED_FOLDER'], compressed_filename)
        compress_image(original_filepath, compressed_path)
        
        return send_file(compressed_path, as_attachment=True)
    
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)

