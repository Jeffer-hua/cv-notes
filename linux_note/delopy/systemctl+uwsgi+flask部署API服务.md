1. uwsgi的ini文件配置
```bash
[uwsgi]
#项目主目录
chdir=/opt/snt/icv_client
# 项目启动文件
wsgi-file=client_app.py
# 主应用名
callable=app
# master模式
master=true
 #开启进程数
processes=2
#开启线程数
threads=4
#timeout超时时间
harakiri=30
# ip端口
socket=0.0.0.0:7002
# uwsgi 查看此服务状态
stats=/opt/snt/icv_client/utils/uwsgi.status
# uwsgi 停止此服务
pidfile=/opt/snt/icv_client/utils/uwsgi.pid
# 日志存放位置
logto=/opt/snt/icv_client/logging/uwsgi_client.log
# 协议
protocol=http
```
---
2. service文件配置
```bash
[Unit] #服务解释，相关依赖的配置
Description=The anjian icv client
After=network.target

[Service] #服务的一些具体运行参数的设置
WorkingDirectory=/opt/snt/icv_client/utils
ExecStart=/usr/local/bin/uwsgi --ini /opt/snt/icv_client/utils/uwsgi.ini
ExecStop=/usr/local/bin/uwsgi --stop /opt/snt/icv_client/utils/uwsgi.pid
Restart=on-failure


[Install] #服务挂载的相关设置，可设置为多用户的
WantedBy=multi-user.target
```