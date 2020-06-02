from concurrent import futures
import time
import logging

import grpc

from rpc import xy_units_pb2_grpc
from service.ReportsGeneratorServer import ReportsGenerator

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    xy_units_pb2_grpc.add_ReportsGeneratorServicer_to_server(ReportsGenerator(), server)
    # server.add_insecure_port('[::]:50052')  # production / test
    server.add_insecure_port('[::]:50053')   # development
    server.start()
    logging.info("server running ...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s",
                        datefmt="%H:%M:%S", filemode='W')
    serve()
