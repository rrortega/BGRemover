from flask import Flask, send_file, abort
from flask_caching import Cache
from io import BytesIO
import os
import base64
import requests
from urllib.parse import unquote
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_THRESHOLD': 500})

@app.route('/bgrmv/<path:encoded_url>', methods=['GET'])
@cache.cached(timeout=50)  # Change timeout to the desired cache time
def get_image(encoded_url):
    try:
        decoded_url = base64.b64decode(encoded_url).decode()
    except:
        abort(400, "Invalid base64 encoding")

    # If we've already cached this URL, serve the cached file
    cached_file = cache.get(decoded_url)
    if cached_file is not None:
        return send_file(cached_file, mimetype='image/png')

    # Fetch image from URL
    response = requests.get(decoded_url)
    if response.status_code != 200:
        abort(400, "Failed to fetch image from URL")

    # Save the image as a BytesIO object
    img = Image.open(BytesIO(response.content))
    img.save("input.png")

    # Run backgroundremover
    os.system(f'backgroundremover -i input.png -o output.png')

    # Check if the output image is all white
    img_output = Image.open('output.png')
    if np.all(np.array(img_output) == 255):
        # If the image is all white, serve the original image instead
        return send_file(BytesIO(response.content), mimetype='image/png')

    # Cache the output file
    with open('output.png', 'rb') as f:
        cache.set(decoded_url, BytesIO(f.read()))

    # Delete the input and output files
    os.remove("input.png")
    os.remove("output.png")

    # Send the output file from cache
    return send_file(cache.get(decoded_url), mimetype='image/png'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
