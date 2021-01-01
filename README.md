# pdf-server

提供 `pdf` 生成服务。因为模板和具体的业务相关，模板不再纳入版本管理。

## 构建docker镜像

- 准备好安装包 `docker/wkhtmltox-0.12.5-1.centos8.x86_64.rpm`
- 在代码仓库根目录执行
`docker build -t pdf-server:[版本号] --build-arg _USER_UID=$UID --build-arg _USER_NAME=${USER} . --no-cache`

## 启动docker实例

- 首先运行脚本 `copy-docker-requires.sh`，准备执行所需代码

- 再启动我们构建好的镜像 `docker run -dit --rm --name pdf-generator -v $PWD/docker/workplace:/workplace -v /home:/host-home -p 50052:50052 pdf-server:[版本号] bash`
