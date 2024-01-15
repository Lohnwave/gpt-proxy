import unittest
import requests
from PIL import Image
from io import BytesIO
import base64

import os
import sys
import time
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
WORK_DIR = os.path.join(CUR_DIR, "..")
UTILS_DIR = os.path.join(CUR_DIR, "../util")
TEMPLATES_DIR = os.path.join(CUR_DIR, "./templates")
sys.path.insert(0, WORK_DIR)
sys.path.insert(1, UTILS_DIR)
sys.path.insert(2, TEMPLATES_DIR)

from util.logging_wrapper import LogInit
import logging

class GPTGenerateEndpointTest(unittest.TestCase):
    def test_generate_endpoint(self):
        # test content
        description = 'dongdong在海边吃冰淇淋'
        image_path = TEMPLATES_DIR + '/image1.jpg'
        # send files
        files = {
            'description': (None, description),
            'images': (image_path,open(image_path, 'rb'), 'image/jpeg')
        }
        
        url = 'http://127.0.0.1:5000/gpt-generate'
        response = requests.post(url, files=files)

        files['images'][1].close()
        # Ensure the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Decode the response JSON
        response_json = response.json()
        # Extract base64-encoded image from the response
        combined_images = response_json['images']
        # Split the combined_images string into a list of base64-encoded images
        image_list = combined_images.split(',')

        # Save each image to a local file
        for idx, encoded_image in enumerate(image_list):
            # Base64 decode
            image_data = base64.b64decode(encoded_image)

            image_io = BytesIO(image_data)
            image = Image.open(image_io)
            saved_path = TEMPLATES_DIR + '/' + f'new_image_{idx}.jpg'
            image.save(saved_path)
            logger.info(f"Image saved to {saved_path}")
            
            self.assertTrue(os.path.exists(saved_path))
            # os.remove(saved_path)

if __name__ == '__main__':
    LogInit()
    logger = logging.getLogger(__name__)
    unittest.main()
