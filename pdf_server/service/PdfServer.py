from grpc import StatusCode
from rpc import pdf_pb2, pdf_pb2_grpc


class Pdf(pdf_pb2_grpc.PdfServicer):
    def uploadResource(self, request_iterator, context):
        # TODO save the uploaded resources
        pass

    def render(self, request, context):
        template_id = request.templateId
        uid = request.uid
        parameters = request.parameters
        pdf_name = request.pdfName
        print('Render request got:', template_id, uid, parameters, pdf_name)
        return pdf_pb2.RenderReply(statusCode=0)
