#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-6
#
from concurrent.futures import ThreadPoolExecutor

class ThreadPoolWrapper:
    def __init__(self, max_workers=5):
        self.thread_pool= ThreadPoolExecutor(max_workers=max_workers)
    # return future for per task, future.result(timeout) block get task res
    # thread safty, can call in muti thread
    def submit(self, fn, *args, **kwargs):
        return self.thread_pool.submit(fn, *args, **kwargs)
    # get all task result in input sequence
    def map(self, fn, *iterables, timeout=None, chunksize=1):
        return self.thread_pool.map(fn, *iterables, timeout, chunksize)
    
    def shutdown(self, wait=True):
        self.thread_pool.shutdown(wait=wait)