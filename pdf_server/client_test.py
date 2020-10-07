import logging
from logging import log
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
        
        # >>>>>> pdfService
        stub = pdf_pb2_grpc.PdfStub(channel)
        # service uploadResource
        def gen_stream(file_path: str):
            with open(file_path, 'rb') as f:
                chunk = f.read(app_config.CHUNK_SIZE)
                while chunk:
                    logging.debug('the chunk, size: %d', len(chunk))
                    # stub.uploadResource()
                    yield pdf_pb2.Chunk(content = chunk)
                    chunk = f.read(1024)
        stream = gen_stream(os.path.join(app_config.TEST_DIR, 'test.zip'))
        res = stub.uploadResource(stream)
        task_uid = res.uid
        logging.debug(f'uploadResouce reply: {res.statusCode}, {res.uid}')


        # service render
        res = stub.render(pdf_pb2.RenderRequest(
            templateId = 'tempalte_id', 
            uid = task_uid, 
            parameters = '{"k1": "v1"}'
        ))
        logging.debug(f'render reply: {res.statusCode}, {res.templateVersion}')

        # service download
        target_file = os.path.join(app_config.TEST_DIR, 'report.pdf')
        res = stub.download(pdf_pb2.DownloadRequest(uid=task_uid))
        with open(target_file, 'wb') as f:
            for chunk in res:
                f.write(chunk.content)
        logging.debug(f'download reply: {os.path.getsize(target_file)} bit')
        # <<<<<< pdfService


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s",
                        datefmt="%H:%M:%S", filemode='W')
    run()
