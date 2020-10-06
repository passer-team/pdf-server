import logging

import grpc

from rpc import xy_units_pb2_grpc, xy_units_pb2, pdf_pb2, pdf_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = xy_units_pb2_grpc.ReportsGeneratorStub(channel)
        response1 = stub.SayHello(xy_units_pb2.HelloRequest(Message='you'))
        # todo test pdf generator
        print("client received: " + response1.Message)
    
        stub = pdf_pb2_grpc.PdfStub(channel)
        response = stub.render(pdf_pb2.RenderRequest(
            templateId = 'tempalte_id', 
            uid = 'the_uid', 
            parameters = '{"k1": "v1"}',
            pdfName = 'the_pdf_name'))
        print('render tested:', response.statusCode)


if __name__ == '__main__':
    logging.basicConfig()
    run()
