
import logging

import pdfkit

from rpc import xy_units_pb2_grpc, xy_units_pb2
import os
from jinja2 import Template
import json
import shutil
import app_config

TEMPLATE_ROOT = "../templates"
PUBLIC_PATH = os.path.abspath(
    os.path.join(TEMPLATE_ROOT, 'public')
)

def get_docker_path(src):
    return "/host-home" + src[5:]

def get_host_path(src):
    return "/home" + src[10:]

def get_template(path: str):
    return os.path.join(TEMPLATE_ROOT, path, "template.html")


class ReportsGenerator(xy_units_pb2_grpc.ReportsGeneratorServicer):

    def SayHello(self, request, context):
        print("SayHello called:" + request.Message)
        return xy_units_pb2.HelloReply(Message='Hello, %s!' % request.Message)

    @staticmethod
    def html_to_pdf(template_path: str, resource_path: str, save_name: str, parameters: str):
        """
        用html生成pdf
        :param template_path: html的路径
        :param resource_path: html引用资源的路径
        :param save_name: pdf的输出名
        :param parameters: 要填充到html的参数
        :return:
        """
        if app_config.IS_DOCKER:
            resource_path = get_docker_path(resource_path)
        template_local_path = get_template(template_path)
        # Prepare assets
        # todo if template.html file not exist, create symbol link
        if not os.path.exists(
            os.path.join(resource_path, "template.html")
            ):
            # 将模板目录和public目录一同复制过去到资源目录
            cmd = "rsync -a {}/* {} {}".format(
                os.path.dirname(template_local_path), PUBLIC_PATH, resource_path
                )
            print("command execute:", cmd)
            os.system(cmd)

        # Render the template
        with open(template_local_path, 'r', encoding='utf-8') as f:
            tmp_src = f.read()
            template_: Template = Template(tmp_src)
            render_res = template_.render(data=parameters)
        # Save html file
        dir_name = os.path.join(resource_path)
        html_path = os.path.join(dir_name, "report.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            # rewrite the previous file
            f.write(render_res)

        # Convert to pdf file
        report_path = os.path.join(dir_name, save_name)
        # Reference URL: https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
        # NOTE: with patched qt is required
        # Example of margin specific: wkhtmltopdf -T 0 -B 0 -L 0 -R 0 report.html report.pdf
        # 参数的值需是字符串
        options = {
            "--margin-top": "0",
            "--margin-left": "0",
            "--quiet": None
        }
        pdfkit.from_file(html_path, report_path, options)
        # pdfkit.configuration()
        if app_config.IS_DOCKER:
            report_path = get_host_path(report_path)
        return report_path

    def GenPdf(self, request: xy_units_pb2.GenPdfRequest, context):
        """
        Generate pdf files, fields which templates requires store in the request.parameters
        :param request:
        :param context:
        :return:
        """
        template_path: str = request.template
        parameters: str = json.loads(request.parameters)
        save_name: str = request.saveName
        resource_path: str = request.resourcePath
        print(template_path, parameters, save_name, resource_path)
        # Check parameters
        if not template_path or not parameters or not save_name or not resource_path:
            raise Exception("parameters missing")

        report_path: str = ReportsGenerator.html_to_pdf(
            template_path, resource_path, save_name, parameters)
        return xy_units_pb2.GenPdfReply(pdfPath=report_path)
