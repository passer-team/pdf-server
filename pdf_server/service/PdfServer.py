import logging
import os
import zipfile

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
        uid = request.uid
        parameters = request.parameters
        pdf_name = request.pdfName
        print('Render request got:', template_id, uid, parameters, pdf_name)
        return pdf_pb2.RenderReply(statusCode=0)
