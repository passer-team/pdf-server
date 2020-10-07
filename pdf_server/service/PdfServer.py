import logging
from logging import log
import os
import zipfile
import uuid

from grpc import StatusCode
from rpc import pdf_pb2, pdf_pb2_grpc

import app_config
from utils import task



class Pdf(pdf_pb2_grpc.PdfServicer):
    def uploadResource(self, request_iterator, context):
        uid = task.create_task()
        task_dir = task.get_task_dir(uid)

        resource_path = os.path.join(task_dir, 'resource.zip')
        with open(resource_path, 'wb') as f:
            for chunk in request_iterator:
                logging.debug('chunk received, size: %d', len(chunk.content))
                f.write(chunk.content)
        zipfile.ZipFile(resource_path).extractall(task_dir)

        return pdf_pb2.UploadResourceReply(statusCode=0, uid=str(uid), message="OK")

    def render(self, request, context):
        template_id = request.templateId
        print('the uuid: ', request.uid)
        uid = uuid.UUID(request.uid)
        parameters = request.parameters
        logging.debug(f'Render request got: {template_id}, {uid}, {parameters}')
        
        # TODO render html to pdf
        pdf_path = task.get_pdf_path(uid)
        os.system(f'cp ~/Downloads/VTKTextBook.pdf {pdf_path}')

        return pdf_pb2.RenderReply(statusCode=0, templateVersion='todo: get template version')

    def download(self, request, context):
        uid = uuid.UUID(request.uid)
        pdf_path = task.get_pdf_path(uid, True)
        with open(pdf_path, 'rb') as f:
            chunk = f.read(app_config.CHUNK_SIZE)
            while chunk:
                # logging.debug(f'get a chunk: {len(chunk)}')
                yield pdf_pb2.Chunk(content=chunk)
                chunk = f.read(app_config.CHUNK_SIZE)
            # TODO clean the files