FROM centos:8.1.1911
ARG VERSION="dev"
LABEL org.label-schema.schema-version="${VERSION}" \
    org.label-schema.name="pdf-server" \
    org.label-schema.license="GPLv2" \
    org.label-schema.build-date="20200602" 
ENV LANG=zh_CN.UTF-8

WORKDIR /app

# >>> 安装必备软件
# 不知道centos为什么导入官方gpg也不行
# 参考 https://blog.csdn.net/cy309173854/article/details/69265738
# 1. python3.8
RUN dnf install -y --nogpgcheck python38 rsync which 
RUN pip3 install pipenv
# 2. nodejs
ENV NODE_VERSION=v14.15.4
ENV NODE_DISTRO=linux-x64
ADD https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-${NODE_DISTRO}.tar.xz node.tar.xz
RUN mkdir -p /usr/local/lib/nodejs
RUN tar -xJf node.tar.xz -C /usr/local/lib/nodejs;rm node.tar.xz
# 3. puppeteer
RUN dnf install -y nss atk at-spi2-atk libX11-xcb cups-libs libdrm libXcomposite libXdamage \
libXrandr gtk3 mesa-libgbm alsa-lib libxshmfence

# <<<

# >>> 创建普通用户和创建他可以操作的目录
ARG _USER_UID=10000
# todo 禁止使用root构建
ARG _USER_NAME=pdfServer  
RUN useradd --uid ${_USER_UID} ${_USER_NAME}
RUN mkdir -p /app/workplace
RUN chown -R ${_USER_NAME}  /app
RUN chgrp -R ${_USER_NAME}  /app
# <<< 

# >>> 配置项目环境
USER ${_USER_NAME}
# 1. nodejs
ENV PATH /usr/local/lib/nodejs/node-${NODE_VERSION}-${NODE_DISTRO}/bin/:$PATH
RUN node -v;npm -v;which node
RUN npm install puppeteer@7.1.0
# 2. pipenv
COPY Pipfile* ./
COPY workplace/fonts ./workplace/fonts
COPY pdf_server ./pdf_server
RUN pipenv install
# <<<

# <<< Clean the tmp files
# RUN dnf clean all
# RUN rm -rf .tmp
RUN rm ~/.cache -rf
# >>>

# <<< 配置网络
EXPOSE 50052
EXPOSE 50053
# >>>

RUN echo "sh /app/pdf_server/pro-run.sh" >> /home/${_USER_NAME}/.bashrc
CMD bash
