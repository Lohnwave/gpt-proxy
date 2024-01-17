#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-14
#
import grpc
import logging
import time
from util.thread_pool_wrapper import ThreadPoolWrapper
from util.get_ip import get_local_ip
from client.gpt_proto.gpt_request_pb2 import Request, FuncType
from client.gpt_proto.gpt_response_pb2 import Response 
from client.gpt_proto.service_pb2_grpc import GPTStudioStub

logger = logging.getLogger(__name__)
class GPTStudioWrapper:
    def __init__(self, server_address):
        """ python gRPC do not support loadBalance in channel"""
        # TODO multiChannel
        options = [
            ('grpc.max_send_message_length', 16*1024*1024),
            ('grpc.max_receive_message_length', 16*1024*1024)
        ]
        self.channel = grpc.insecure_channel(server_address, options)
        self.stub = GPTStudioStub(self.channel)
        if len(get_local_ip()) > 0:
            self.ip = get_local_ip()[0]

    def CallGPTStudio(self, sessionid, query, encoded_images=None, timeout=1):
        try:
            request = Request()
            request.session_id = sessionid
            request.content.query = query
            if encoded_images and (len(encoded_images) != 0):
                request.content.item_data.images.extend(encoded_images)
            request.context.client_ip = self.ip
            response = self.stub.GPTStudio(request, timeout)
        except grpc.RpcError as e:
            if e.code() != grpc.StatusCode.OK:
                logger.error("CallGPTStudio faild. sessionid:%s with gRPC error: %s %s",
                             sessionid, e.code(), e.details())
            return None
        return response
    
    def ShutDown(self):
        logger.info("resource clean...")
        self.channel.close()