#!/bin/sh
echo "在仓库根目录执行本脚本(Execute the script at the root of this git repository)"
pipenv run python -m grpc_tools.protoc --python_out=pdf_server/rpc --grpc_python_out=pdf_server/rpc \
--proto_path=grpc-proto/ grpc-proto/xy-units.proto grpc-proto/pdf.proto
echo "Success"
