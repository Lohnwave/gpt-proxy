#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-14
#
import unittest
import os
import sys
import time
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
WORK_DIR = os.path.join(CUR_DIR, "..")
UTILS_DIR = os.path.join(CUR_DIR, "../util")
CLIENT_DIR = os.path.join(CUR_DIR, "../client")
sys.path.insert(0, WORK_DIR)
sys.path.insert(1, UTILS_DIR)
sys.path.insert(2, CLIENT_DIR)

from client.gpt_studio_wrapper import GPTStudioWrapper
from util.logging_wrapper import LogInit
import logging

class TestGPTStudioWrapper(unittest.TestCase):
    def test_nomal(self):
        quary = "找下去年成都的照片,帮我生成一个画廊"
        t0 = time.time()
        remote = GPTStudioWrapper("192.168.123.86:50051")
        sessionid = f"{t0}"
        logger.info("CallGPTStudio sessionid=%s, query=%s", sessionid, quary)
        response = remote.CallGPTStudio(sessionid, query=quary, timeout=1)
        print(response)
        t1 = time.time()
        logger.info("nomal cost=%dms", (t1-t0)*1000)
        self.assertEqual(2, 2)

if __name__ == '__main__':
    LogInit()
    logger = logging.getLogger(__name__)
    unittest.main()