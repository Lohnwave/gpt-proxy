#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-5
#
from util.singleton import Singleton
import jieba
class JiebaWrapper(metaclass=Singleton):
    def __init__(self):
        self.initialized = False
    
    def initialize(self):
        if not self.initialized:
            jieba.initialize()
            self.initialized = True

    def cut(self, *args, **kwargs):
        self.initialize()
        return jieba.cut(*args, **kwargs)
    
    def lcut(self, *args, **kwargs):
        self.initialize()
        return jieba.lcut(*args, **kwargs)
    
    def cut_for_search(self, *args, **kwargs):
        self.initialize()
        return jieba.cut_for_search(*args, **kwargs)
    
    def enable_parallel(self, max_parallel_threads=None):
        self.initialize()
        jieba.enable_parallel(max_parallel_threads)