#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-6
#
from concurrent.futures import ProcessPoolExecutor

class ProcessPoolWrapper:
    def __init__(self, max_workers=5):
        self.process_pool = ProcessPoolExecutor(max_workers=max_workers)
    # return future for per task, future.result(timeout) block get task res
    # process safty, can call in muti process
    def submit(self, fn, *args, **kwargs):
        return self.process_pool.submit(fn, *args, **kwargs)
    # get all task result in input sequence
    def map(self, fn, *iterables, timeout=None, chunksize=1):
        return self.process_pool.map(fn, *iterables, timeout, chunksize)
    
    def shudown(self, wait=True):
        self.process_pool.shutdown(wait=wait)
    