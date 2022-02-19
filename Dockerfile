FROM dev.passer.zyheal.com:8087/zyheal/pdf-server:0.1.0

ARG VERSION="dev"
LABEL org.label-schema.schema-version="${VERSION}" \
    org.label-schema.name="pdf-server" \
    org.label-schema.version="v0.1.1"
ENV LANG=zh_CN.UTF-8

WORKDIR /app

# >>> 创建普通用户和创建他可以操作的目录
ARG _USER_UID=10000
ARG _USER_NAME=pdfServer

# >>> 配置项目环境
USER ${_USER_NAME}
# 1. nodejs
ENV PATH /usr/local/lib/nodejs/node-${NODE_VERSION}-${NODE_DISTRO}/bin/:$PATH

# COPY workplace/fonts ./workplace/fonts
COPY pdf_server ./pdf_server
# <<<

# <<< 配置网络
EXPOSE 50054
# >>>

CMD bash
