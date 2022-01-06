import grpc
from google.protobuf.json_format import MessageToDict

import message_pb2_grpc, message_pb2
from db import mongo_connection


class MessageServicer(message_pb2_grpc.MessageServicer):

    def create(self, request, context):

        request = MessageToDict(request)
        result = mongo_connection.messasges.insert_one(request)

        if not result.acknowledged:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Method not implemented!')
            raise Exception('Database error')

        return message_pb2.MessageResponse(message_id=str(result.inserted_id))
