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
`ulimit` 限制文件/程序的大小
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241107165134.png)

[变量内容的删除、取代与替换](https://zq99299.github.io/linux-tutorial/tutorial-basis/10/02.html#%E5%8F%98%E9%87%8F%E5%86%85%E5%AE%B9%E7%9A%84%E5%88%A0%E9%99%A4)
`${argument#pattern}` 从前往后匹配最短的
	`${PATH#/*:}` 删除第一个路径
`${argument##pattern}` 从前往后匹配最长的
	`${PATH##/*:}` 仅保留最后一个路径
`${argument%pattern}` 从后往前匹配最短的
	`${PATH%/*}` 删除最后一个路径
`${argument%%pattern}` 从后往前匹配最长的
	`${PATH%%/*}` 仅保留第一个路径

**变量的测试与内容替换**
`${argument/old/new}`替换一个
`${argument//old/new}`替换所有
	有点像 vim 的语法

`var=${str[:][-+=?]expr}`
`:` 将空字符视为不存在
`-`  `str` 存在使用原始值，不存在使用默认值
`+` 存在使用默认值，不存在使用原始值
`=` 会改变 `str`。存在使用原始值，不存在使用默认值
`?` 存在使用原始值，不存在则报错

# 10.3 命令别名与历史命令
`alias ll='ls -al'` 设置别名
`alias` 查看所有别名
`unalias` 删除别名

# 10.4 Bash Shell 的操作环境

同名指令的执行顺序
	相对、绝对路径执行命令 `bin/ls ./ls`
	`alias` 中的命令
	bash 内置的指令
	`$PATH` 搜寻到的第一个指令
	可以用 `type -a command` 查看

---
进站与欢迎信息（和 PS1不一样那个是命令行提示符）
- 进站信息（不用登录就能看到）
	在 `/etc/issue` 中
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241107174958.png)
	注意要识别转义字符
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241107181108.png)
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241107181042.png)![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411071901384.png)

- 欢迎信息（用户登录后显示）
	
---
bash 的环境配置文件（可以对应 win 系统）

login 与 non-login shell 很好理解,读取的配置文件不同
- login shell 首先读取 `/etc/profile` 和 `~/.bash_profile` 或 `~/.bash_login` 或 `~/profile`（我的虚拟机上是/etc/profile）
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411071908821.png)
	然后依顺序调用 
		`~/.bash_profile`
		`~/.bash_login`
		`~/.profile`（虚拟机中的）
	这两个文件都会再调用别的文件
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411072126362.png)
	`source` 可以更新配置
	
- non-login shell
	只读取 `/.bashrc`

`~/.bash_history` 历史命令
`~/.bash_logout` 登出 bash 后系统继续完成的事

一些快捷键设置：
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411072135766.png)

万用字符与特殊符号：
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411072136891.png)
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411072137306.png)

# 10.5 数据流重导向
- 数据流类型
	 标准输入stdin ，代码0 `<或<<`
	 标准输出stdout，代码1 `>或>>`
		 `>` 会覆盖原有数据
		 `>>` 会 append
	 标准错误输出，代码2 `2>或2>>`
`/dev/null` 垃圾桶黑洞装置
---
命令执行的判断依据
	`command1;command2` 命令1和2之间没有关联性
	`command1||command2` 1执行了2就不执行
	`command1&&command2` 1执行了2才执行
	 常用 `cmd1 && cmd2 || cmd3`

# 10.6 管线命令 pipe
- 截取命令
	`cut -d keyword -f number`
		`cut -d ' ' -f 1,5` 以`<space>`划分，取第 number 个
		注意**从1开始计数不是从0开始**
	`cut -c num_char`
		`cur -c 12-` 每行取第12个 char 之后的
	
	`grep [-acinv] [--color=auto] string filename`
		如果一行中包含了 string 则列出
		![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411072247835.png)

- [排序命令](https://zq99299.github.io/linux-tutorial/tutorial-basis/10/06.html#sort)
	`sort [-fbMnrtuk] [file or stdin]` 排序
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411072248108.png)
	`uniq [-ic]` 去重
		`-i` 忽略大小写
		`-c` 计数
	`wc [-lwm]` 统计
		`-l` 仅列出 lines
		`-w` 仅列出 words
		`-m` 仅列出多少 char
	`tee [-a] file` 双向重导向

- [字符转换命令](https://zq99299.github.io/linux-tutorial/tutorial-basis/10/06.html#%E5%AD%97%E7%AC%A6%E8%BD%AC%E6%8D%A2%E5%91%BD%E4%BB%A4%EF%BC%9Atr%E3%80%81col%E3%80%81join%E3%80%81paste%E3%80%81expand)
```Shell
tr [-ds] SET1 ... 正则替换或删除
	-d：删除信息当中的 SET1 这个字符串
	-s：替换重复的字符

col [-xb] 过滤某些符号，有点抽象
	-x:将 tab 键转换成对等的空格键

```
使用 `-` 作为一个暂存区