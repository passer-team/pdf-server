#!/bin/sh
echo "在仓库根目录执行本脚本(Execute the script at the root of this git repository)"
pipenv run python -m grpc_tools.protoc --python_out=xy-units/rpc --grpc_python_out=xy-units/rpc --proto_path=grpc-proto/ grpc-proto/xy-units.proto
echo "Success"
