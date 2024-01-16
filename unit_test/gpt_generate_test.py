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
from requests_toolbelt.multipart import MultipartEncoder
import logging

class GPTGenerateEndpointTest(unittest.TestCase):
    def test_generate_endpoint(self):
        # test content
        description = 'dongdong在海边吃冰淇淋'
        image_paths = [TEMPLATES_DIR + '/image1.jpg']
        images = []
        fields = []
        for i, path in enumerate(image_paths):
            image = open(path, 'rb')
            images.append(image)
            fields.append(('images', (path, image, 'image/jpeg')))
        fields.append(('description', description))
        multipart_data = MultipartEncoder(fields=fields)

        # send files
        url = 'http://127.0.0.1:5000/gpt-generate'
        response = requests.post(url, data=multipart_data, headers={'Content-Type': multipart_data.content_type})

        # close the file after send
        for image in images:
            image.close()
        # Ensure the request was successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Decode the response JSON
        response_json = response.json()
        description_json = response_json.get('description')
        images_encoded = response_json['images']

        # Save each image to a local file
        for idx, encoded_image in enumerate(images_encoded):
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
