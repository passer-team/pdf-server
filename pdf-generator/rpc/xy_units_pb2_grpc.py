# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import xy_units_pb2 as xy__units__pb2


class ReportsGeneratorStub(object):
  """定义服务
  Sends a greeting
  rpc SayHello (XyAiRequest) returns (XyAiReply) {}
  Sends a greeting again
  rpc SayHelloAgain(XyAiRequest) returns (XyAiReply) {}
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GenBrainReport = channel.unary_unary(
        '/units.ReportsGenerator/GenBrainReport',
        request_serializer=xy__units__pb2.BrainReportRequest.SerializeToString,
        response_deserializer=xy__units__pb2.BrainReportReply.FromString,
        )
    self.SayHello = channel.unary_unary(
        '/units.ReportsGenerator/SayHello',
        request_serializer=xy__units__pb2.HelloRequest.SerializeToString,
        response_deserializer=xy__units__pb2.HelloReply.FromString,
        )
    self.GenPdf = channel.unary_unary(
        '/units.ReportsGenerator/GenPdf',
        request_serializer=xy__units__pb2.GenPdfRequest.SerializeToString,
        response_deserializer=xy__units__pb2.GenPdfReply.FromString,
        )


class ReportsGeneratorServicer(object):
  """定义服务
  Sends a greeting
  rpc SayHello (XyAiRequest) returns (XyAiReply) {}
  Sends a greeting again
  rpc SayHelloAgain(XyAiRequest) returns (XyAiReply) {}
  """

  def GenBrainReport(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GenPdf(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ReportsGeneratorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GenBrainReport': grpc.unary_unary_rpc_method_handler(
          servicer.GenBrainReport,
          request_deserializer=xy__units__pb2.BrainReportRequest.FromString,
          response_serializer=xy__units__pb2.BrainReportReply.SerializeToString,
      ),
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=xy__units__pb2.HelloRequest.FromString,
          response_serializer=xy__units__pb2.HelloReply.SerializeToString,
      ),
      'GenPdf': grpc.unary_unary_rpc_method_handler(
          servicer.GenPdf,
          request_deserializer=xy__units__pb2.GenPdfRequest.FromString,
          response_serializer=xy__units__pb2.GenPdfReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'units.ReportsGenerator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))