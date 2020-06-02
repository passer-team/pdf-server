import logging

import grpc

from rpc import xyunit_pb2_grpc, xyunit_pb2


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = xyunit_pb2_grpc.ReportsGeneratorStub(channel)
        response1 = stub.SayHello(xyunit_pb2.HelloRequest(Message='you'))
        # response2 = stub.GenBrain(xyunit_pb2.BrainRequest(patientName="daryl", patientAge=10))
        response2 = stub.GenBrainReport(xyunit_pb2.BrainReportRequest(seriesPath="",
                                                                      patientId=""))
    print("client received: " + response1.Message)
    print("client received: " + response2.path)


if __name__ == '__main__':
    logging.basicConfig()
    run()
