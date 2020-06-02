# 因为pb2_grpc.py要导入pb2.py
# 直接使用了import xxx_pb2.py as xxx__pb2.py
# 所以把当前目录添加到pythonpath环境变量
import sys
import os

pwd = os.path.dirname(__file__)
# print(pwd)
sys.path.append(pwd)
