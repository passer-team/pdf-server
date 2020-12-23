import logging
import os
import zipfile
import uuid
import json

import pdfkit
from rpc import pdf_pb2, pdf_pb2_grpc
import jinja2

import app_config
from utils import task


class PdfHelper:
    """
    Pdf帮助类，和gRPC的接口的代码分开
    """
    @staticmethod
    def html_to_pdf(html_path: str, pdf_path: str):
        """
        Convert the html to a pdf file with pdfkit(based on wkhtmltopdf)
        """
        # Reference URL: https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
        # NOTE: with patched qt is required
        # Example of margin specific: wkhtmltopdf -T 0 -B 0 -L 0 -R 0 report.html report.pdf
        # 参数的值需是字符串
        options = {
            "--margin-top": "0",
            "--margin-left": "0",
            "--quiet": None
        }
        pdfkit.from_file(html_path, pdf_path, options)

    @staticmethod
    def fill_template(template_path: str, target_path: str, parameters):
        """
        Fill the template file
        """
        template_file = open(template_path, 'r', encoding='utf-8')
        template = jinja2.Template(template_file.read())
        render_res = template.render(data=parameters)
        template_file.close()

        target_file = open(target_path, 'w', encoding='utf-8')
        target_file.write(render_res)
        target_file.close()


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
        # 暂时不使用template＿id，template.html使用文件上传的方式得到
        template_id: str = request.templateId
        uid = uuid.UUID(request.uid)
        parameters: dict = json.loads(request.parameters)
        logging.debug(f'Render request got: {template_id}, {uid}, {parameters}')
        
        # 准备字体
        task.prepare_assets(uid)

        template_path = task.get_template_path(uid, True)
        # Notice: if report.html exsits, it will be overwritten
        report_html_path = task.get_report_html_path(uid, False)
        pdf_path = task.get_pdf_path(uid, False)
        PdfHelper.fill_template(template_path, report_html_path, parameters)
        PdfHelper.html_to_pdf(template_path, pdf_path)

        return pdf_pb2.RenderReply(statusCode=0, templateVersion='todo: get template version')

    def download(self, request, context):
        uid = uuid.UUID(request.uid)
        filename = request.filename

        file_path = task.get_download_path(uid, filename, True)
        task.get
        
        with open(file_path, 'rb') as f:
            chunk = f.read(app_config.CHUNK_SIZE)
            while chunk:
                # logging.debug(f'get a chunk: {len(chunk)}')
                yield pdf_pb2.Chunk(content=chunk)
                chunk = f.read(app_config.CHUNK_SIZE)
            # TODO clean the files
