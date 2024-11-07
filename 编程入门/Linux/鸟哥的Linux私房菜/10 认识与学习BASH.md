# 10.1 认识 BASH 这个 Shell
Shell：能够操作指挥 kernel 的应用程序的接口

`/etc/shells` 查看系统可以使用的 shell
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241106170239.png)

用户登录后可以取得 shell，记录在 `/etc/passwd`
每一行的最后一个数据就是登录后的默认 shell
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241106182549.png)

Bash 的主要优点：
1. history 使用过的指令记录在 ~`/.bash_history`
2. 命令补全 按 `Tab`
3. 别名设置 `alias`
4. 程序化脚本 shell scripts
5. 万用字符 `*`

Bash 有一堆内置命令
用 `type` 查询*可执行文件*命令，类似 `which`：
	`-a` 所有的同名命令
	`-t` 仅显示命令类型

快速编辑指令的技巧：
`\<Enter>` 换行
`^u/^e` 向前向后删除
`^a/^e` 移动到最前最后

# 10.2 Shell 的变量功能
- 环境变量 `PATH HOME MAIL SHELL` 等
- 用于 shell scripts

取用变量 `echo ${command}`
设置变量  `command=content`
	双引号内 `$command` 起作用，单引号内为纯文本
	`\` 可以跳脱特殊字符 `<Enter> $ \ <Space>` 等
	`$(command)` 可以优先处理
	`export argument` 可以在子程序使用
	`unset command` 可以取消设置

`env` 查看已有环境变量
`set` 查看环境变量和自定义变量
`PS1` 命令提示字符
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241106190321.png)
`locale -a` 查看语系变量
`read -p <hint> command` 带提示符的读取指令
`declare` 定义变量类型
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241106190648.png)
