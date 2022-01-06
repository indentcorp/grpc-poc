import grpc
import json

import arrow
from google.protobuf import json_format

import message_pb2, message_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = message_pb2_grpc.MessageStub(channel=channel)

    data = {
        'platform': {
            'name': 'KAKAO',
            'context': {
                'cellphone': '01012345678'
            }
        },
        'metadata': {
            'origin_mall_id': 'grpc-tester-01'
        },
        'target_schedule': {
            'send_time': arrow.now().isoformat()
        },
        'string_payload': 'ITSDAMESSAGE'
    }

    buff = json_format.ParseDict(data, message_pb2.MessageRequest())

    response = stub.create(buff)
    return response

if __name__ == '__main__':
    run()
