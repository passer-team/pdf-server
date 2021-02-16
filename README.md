# pdf-server

提供 `pdf` 生成服务。因为模板和具体的业务相关，模板不再纳入版本管理。

## 构建docker镜像

- 在代码仓库根目录执行
`docker build -t pdf-server:<版本号> --build-arg VERSION=<版本号> . --no-cache`

> 一般来说，代码仓库的分支名即为版本号，通过 `git branch` 获得

## 启动docker实例

- 启动我们构建好的镜像 `docker run -dit --rm -p 50052:50052 pdf-server:<版本号> bash`
