FROM centos:8.1.1911

LABEL org.label-schema.schema-version="0.0.1" \
    org.label-schema.name="pdf-server" \
    org.label-schema.license="GPLv2" \
    org.label-schema.build-date="20200602" 
ENV LANG=zh_CN.UTF-8

WORKDIR /workplace
# >>> 安装必备软件
RUN mkdir .tmp
COPY docker/*.rpm .tmp
RUN dnf install -y .tmp/*.rpm
# 不知道centos为什么导入官方gpg也不行
# 参考 https://blog.csdn.net/cy309173854/article/details/69265738
RUN dnf install -y --nogpgcheck python38 rsync which
RUN pip3 install --user pipenv
# <<<

# >>> 创建普通用户和创建他可以操作的目录
ARG _USER_UID
# todo 禁止使用root构建
ARG _USER_NAME  
RUN useradd --uid ${_USER_UID} ${_USER_NAME}
RUN mkdir /${_USER_NAME}
RUN chown -R ${_USER_NAME}  /${_USER_NAME}
RUN chgrp -R ${_USER_NAME}  /${_USER_NAME}
# <<< 

# >>> 配置项目环境
USER ${_USER_NAME}
COPY Pipfile* ./
RUN pipenv install
# <<<

# <<< Clean the tmp files
# RUN dnf clean all
# RUN rm -rf .tmp
# >>>

# <<< 配置网络
EXPOSE 50052
EXPOSE 50053
# >>>

RUN echo "sh /workplace/pdf-generator/pro-run.sh" >> /home/${_USER_NAME}/.bashrc
CMD bash
# 启动容器的时候挂载home和workplace
#
