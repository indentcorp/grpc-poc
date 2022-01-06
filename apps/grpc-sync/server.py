from concurrent.futures import ThreadPoolExecutor
import grpc

import message_pb2_grpc
from db import connect_to_mongo, close_mongo_connection
from servicer import MessageServicer


class Server:

    @staticmethod
    def run():
        server = grpc.server(ThreadPoolExecutor(max_workers=10))
        message_pb2_grpc.add_MessageServicer_to_server(MessageServicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()

        connect_to_mongo()
        server.wait_for_termination()
        close_mongo_connection()


if __name__ == '__main__':
    Server.run()
