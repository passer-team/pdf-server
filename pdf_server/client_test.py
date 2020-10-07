import logging
import os

import grpc

from rpc import xy_units_pb2_grpc, xy_units_pb2, pdf_pb2, pdf_pb2_grpc
import app_config


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel(f'localhost:{app_config.LISTEN_PORT}') as channel:
        stub = xy_units_pb2_grpc.ReportsGeneratorStub(channel)
        response1 = stub.SayHello(xy_units_pb2.HelloRequest(Message='you'))
        # todo test pdf generator
        logging.debug("client received: " + response1.Message)
    
        stub = pdf_pb2_grpc.PdfStub(channel)
        response = stub.render(pdf_pb2.RenderRequest(
            templateId = 'tempalte_id', 
            uid = 'the_uid', 
            parameters = '{"k1": "v1"}',
            pdfName = 'the_pdf_name'))
        logging.debug('render tested:', response.statusCode)
        
        def gen_stream(file_path: str):
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
                while chunk:
                    logging.debug('the chunk, size: %d', len(chunk))
                    # stub.uploadResource()
                    yield pdf_pb2.Chunk(content = chunk)
                    chunk = f.read(1024)
        stream = gen_stream(os.path.join(app_config.WORKPLACE, 'test-data/test.zip'))
        res = stub.uploadResource(stream)
        logging.debug(f'uploadResouce reply: {res.statusCode}, {res.uid}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
