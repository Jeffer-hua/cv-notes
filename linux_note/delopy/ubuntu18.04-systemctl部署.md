1. systemd官方解释
- systemd 是 Linux 下的一款系统和服务管理器，兼容 SysV 和 LSB 的启动脚本。systemd 的特性有：支持并行化任务；同一时候採用 socket 式与 D-Bus 总线式激活服务；按需启动守护进程（daemon）。利用 Linux 的 cgroups 监视进程；支持快照和系统恢复。维护挂载点和自己主动挂载点。各服务间基于依赖关系进行精密控制。 
检视和控制systemd的主要命令是systemctl。  
- 在 systemctl 參数中加入 -H <username>@<主机名>能够实现对其它机器的远程控制
- 全部可用的单元文件存放在/usr/lib/systemd/system/ 和/etc/systemd/system/ 文件夹（后者优先级更高）。
- 使用单元,使用 systemctl 控制单元时，通常须要使用单元文件的全名，包括扩展名（比如 sshd.service）。可是有些单元能够在systemctl中使用简写方式,假设无扩展名，systemctl 默认把扩展名当作 .service
---
2. systemctl 控制单元基本指令
```bash
# 开始单元
systemctl start <单元>
# 停止单元
systemctl stop <单元>
# 重新启动单元
systemctl restart <单元>
# 查看单元输出状态
systemctl status <单元>
# 检查单元是否配置为自己主动启动
systemctl is-enabled <单元>
# 开机自己主动激活单元
systemctl enable <单元>
# 取消开机自己主动激活单元
systemctl disable <单元>
# 禁用一个单元(禁用后，间接启动也是不可能的)
systemctl mask <单元>
# 取消禁用一个单元
systemctl unmask <单元>
# 显示单元的手冊页（必须由单元文件提供）
systemctl help <单元>
# 又一次载入 systemd，扫描新的或有变动的单元
systemctl daemon-reload
```
---
3. service文件配置参数
- [Unit]
- [Service]
- [install]
