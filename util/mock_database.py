#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-18
#
import threading
from collections import deque

class MockDataBase():
    def __init__(self, max_size):
        self.max_size = max_size
        self.lock = threading.Lock()
        self.images_queue = deque()
        self.text_queue = deque()
        self.image_size = 0
        self.text_size = 0

    def add_image(self, image_base64):
        with self.lock:
            if len(self.images_queue) >= self.max_size:
                self.images_queue.popleft()  # FIFO
                self.image_size -=1
            self.images_queue.append(image_base64)
            self.image_size += 1

    def add_text(self, text):
        with self.lock:
            if len(self.text_queue) >= self.max_size:
                self.text_queue.popleft()  # FIFO
                self.text_size -= 1
            self.text_queue.append(text)
            self.text_size += 1

    def get_images(self):
        with self.lock:
            return list(self.images_queue)

    def get_texts(self):
        with self.lock:
            return list(self.text_queue)
    
    def get_texts_size(self):
        with self.lock:
            return self.text_size

    def get_images_size(self):
        with self.lock:
            return self.image_size
     