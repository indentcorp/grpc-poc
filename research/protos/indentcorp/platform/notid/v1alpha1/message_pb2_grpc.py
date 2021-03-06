# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from indentcorp.platform.notid.v1alpha1 import message_pb2 as indentcorp_dot_platform_dot_notid_dot_v1alpha1_dot_message__pb2


class MessageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/indentcorp.platform.notid.v1alpha1.Message/create',
                request_serializer=indentcorp_dot_platform_dot_notid_dot_v1alpha1_dot_message__pb2.MessageRequest.SerializeToString,
                response_deserializer=indentcorp_dot_platform_dot_notid_dot_v1alpha1_dot_message__pb2.MessageResponse.FromString,
                )


class MessageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MessageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=indentcorp_dot_platform_dot_notid_dot_v1alpha1_dot_message__pb2.MessageRequest.FromString,
                    response_serializer=indentcorp_dot_platform_dot_notid_dot_v1alpha1_dot_message__pb2.MessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'indentcorp.platform.notid.v1alpha1.Message', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Message(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/indentcorp.platform.notid.v1alpha1.Message/create',
            indentcorp_dot_platform_dot_notid_dot_v1alpha1_dot_message__pb2.MessageRequest.SerializeToString,
            indentcorp_dot_platform_dot_notid_dot_v1alpha1_dot_message__pb2.MessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
