import logging

import grpc

from rpc import xyunit_pb2_grpc, xyunit_pb2


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = xyunit_pb2_grpc.ReportsGeneratorStub(channel)
        response1 = stub.SayHello(xyunit_pb2.HelloRequest(Message='you'))
        # todo test pdf generator
    print("client received: " + response1.Message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
