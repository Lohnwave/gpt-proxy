#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-14
#
from flask import Flask, request, jsonify
from flasgger import Swagger
from PIL import Image
from io import BytesIO
import signal
import gflags
import base64
import os
import sys
import time
import logging

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
WORK_DIR = os.path.join(CUR_DIR, "..")
UTILS_DIR = os.path.join(CUR_DIR, "../util")
CLIENT_DIR = os.path.join(CUR_DIR, "../client")
sys.path.insert(0, WORK_DIR)
sys.path.insert(1, UTILS_DIR)
sys.path.insert(2, CLIENT_DIR)

from util.logging_wrapper import LogInit
from client.gpt_studio_wrapper import GPTStudioWrapper
from client.gpt_proto.gpt_request_pb2 import Request, FuncType
from client.gpt_proto.gpt_response_pb2 import Result

app = Flask(__name__)
swagger = Swagger(app)

# define glfags
FLAGS = gflags.FLAGS
gflags.DEFINE_string('gpt_server_address', 'localhost:50051', 'Address of gpt server')

@app.route('/gpt-chat', methods=['POST'])
def chat():
    """
    chat, search, generate images with GPT & MJ
    ---
    tags:
      - GPT Chat API
    consumers:
      -multipart/form-data
    parameters:
      - name: images
        in: formData
        type: file
        required: false
        description: The images to be processed
      - name: text
        in: formData
        type: string
        required: true
        description: query or  desciption for images
    responses:
      200:
        description: List of base64-encoded images with a common description or answar for quesion
        examples:
            application/json: { "images" : ["data:image/png;base64,iisds...."],
              "text" : "Description for the generate images, or answer",
              "resultType": "CHAR or SEARCH or GENERATE"}
    """
    text = request.form.get('text', '')
    image_files = request.files.getlist('images')
    logger.info("recv desc:%s images size:%d", text, len(image_files))
    # Process each image and collect base64-encoded images
    encoded_images = []
    for image in image_files:
        # Open image using PIL
        pil_image = Image.open(image)
        # Process the image if needed

        # Convert PIL Image to base64
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        encoded_images.append(encoded_image)
   # call remote gpt-studio
    logger.info("CallGPT begin. text=%s", text)
    t0 = time.time()
    session_id = request.remote_addr + '-' + str(int(t0))
    response = remote_gpt.CallGPTStudio(session_id, text, encoded_images)
    
    result_images = encoded_images # for test
    result_type = 'UNKNOW'
    answer = ''
    if response:
        if response.result.type == Result.ResultType.SEARCH:
            result_type = 'SEARCH'
            answer = response.result.search_result.texts
            result_images = response.result.search_result.images
        if response.result.type == Result.ResultType.GENERATE:
            result_type = 'GENERATE'
            answer = response.result.generate_result.text
            result_images = response.result.generate_result.images
        if response.result.type == Result.ResultType.CHAT:
            result_type = 'CHAT'
            answer = response.result.generate_result.text
    t1 = time.time()
    logger.info("CallGPT done. cost=%dms, reponse=%s", (t1-t0)*1000, response)

    # Store image information with the common description
    chat_result = {"images": result_images, "text": answer, "resultType": result_type}
    
    return jsonify(chat_result)

@app.route('/gpt-search', methods=['GET'])
def search():
    """
    Search for URLs based on query
    ---
    tags:
      - search API
    parameters:
      - name: query
        in: query
        type: string
        required: true
    responses:
      200:
        description: List of URLs matching the query
        examples:
            application/json: { "result_urls": ["https://example.com/search?q=query&page=1"]}
    """
    query = request.args.get('query', '')
    # call remote gpt-studio
    logger.info("CallGPT begin. query=%s", query)
    t0 = time.time()
    session_id = request.remote_addr + '-' + str(int(t0))
    response = remote_gpt.CallGPTStudio(session_id, query, FuncType.SEARCH)
    t1 = time.time()
    logger.info("CallGPT done. cost=%dms, reponse=%s", (t0-t1)*1000, response)

    # For demonstration, let's return a dummy result
    result_urls = [
        f"https://example.com/search?q={query}&page=1",
        f"https://example.com/search?q={query}&page=2",
    ]
    return jsonify({'result_urls': result_urls})

@app.route('/gpt-generate', methods=['POST'])
def generate():
    """
    Generate base64-encoded images with a single description
    ---
    tags:
      - generate API
    consumers:
      -multipart/form-data
    parameters:
      - name: images
        in: formData
        type: file
        required: true
        description: The images to be processed
      - name: description
        in: formData
        type: string
        required: true
        description: Description for all the images
    responses:
      200:
        description: List of base64-encoded images with a common description
        examples:
            application/json: { "images" : ["data:image/png;base64,iisds...."], "description" : "Description for the generate images"}
    """
    description = request.form.get('description', '')
    image_files = request.files.getlist('images')
    logger.info("recv desc:%s images size:%d", description, len(image_files))
    # Process each image and collect base64-encoded images
    encoded_images = []
    for image in image_files:
        # Open image using PIL
        pil_image = Image.open(image)
        # Process the image if needed

        # Convert PIL Image to base64
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
        encoded_images.append(encoded_image)
   # call remote gpt-studio
    logger.info("CallGPT begin. query=%s", description)
    t0 = time.time()
    session_id = request.remote_addr + '-' + str(int(t0))
    response = remote_gpt.CallGPTStudio(session_id, description, FuncType.GENERATE)
    t1 = time.time()
    logger.info("CallGPT done. cost=%dms, reponse=%s", (t0-t1)*1000, response)

    # Store image information with the common description
    image_result = {"images": encoded_images, "description": description}
    
    return jsonify(image_result)

def InterruptedCallback(signum, frame, gpt_server):
    logger.warning("Recived Signal:%d exit server..." ,signum)
    if gpt_server:
        gpt_server.ShutDown()
    time.sleep(3)
    sys.exit(0)

if __name__ == '__main__':
    FLAGS(sys.argv)
    LogInit()
    logger = logging.getLogger(__name__)
    remote_gpt = GPTStudioWrapper(FLAGS.gpt_server_address)
    signal.signal(signal.SIGUSR1, lambda signum, frame
            : InterruptedCallback(signum, frame, remote_gpt))
    app.run(debug=False)

