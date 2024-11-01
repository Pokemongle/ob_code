- 三种身份
	- user
	- group
	- others
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241101162703.png)
`/etc/passwd` 存放账号信息
`/etc/shadow` 存放密码信息
`/etc/group` 存放群组信息
# 5.2 Linux 文件权限概念
- 三种文件权限
	- read
	- write
	- execute

使用 `su` 来切换当前用户

可以使用 `ls -al` **查看文件权限**
	`-al` 不是一个 option 是两个，等价于 `-a -l`
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241101164001.png)
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241101164017.png)
	第一栏
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241101164219.png)
		如果是 d（文件夹），没有 `x` 权限的话不能进入此文件夹
	第四栏 文件大小默认单位 Bytes

改变文件属性和权限
	对于文件夹及其下属所有文件来说加上 `-R` 这个 OPTION 
	`chgrp` 改变文件所属群组
		`chgrp [GROUP] [FILE]`
		已有的群组名称在 `/etc/group` 中
	`chown` 改变文件拥有者
		`chown [User] [FILE]`
		已有的用户名称在 `/etc/passwd` 中
	`chmod` 改变文件的权限等特性
		`chmod [MODE] [FILENAME]`
			方法一：
			 `MODE` 是三种对象的权限，每种由 (r=4, w=2,  x=1) 的组合之和决定
			 `-rwx-rwx-rwx` 就是 `chmod 777 [FILENAME]`
			方法二：
			分别用一个字母 `ugo` 表示 user, group, others，以及用 `a` 表示以上所有人
			用 `+（添加） -（移除） =（设置）` 来对不同的对象权限进行设置
				e.g. 直接设置权限 `chmod u=rwx, go=rx .bashrc` 为 `u` 设置所有的权限， ` g ` 和 ` o ` 设置相同的权限，不同的用户之间使用 `,` 来分割，最后加上需要修改的文件名
				e.g. 添加/移除权限 `chmod a+w .bashrc` 为所有人添加可写权限，移除的话把 `+` 改成 ` - `

权限对于文件和文件夹的不同意义
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241101173009.png)
	文件权限不能决定用户是否能**删除**该文件，但是文件夹权限 `w` 可以
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241101194342.png)

文件种类，一般由文件权限的第一个字符表示
- 正规文件`-`
	- 纯文本文件 (ASCII) 可以用 `cat` 命令读取
	- 二进制可执行文件(binary)比如 `cat`
	- 数据格式文件 (data)
- 目录 `d`
- 链接文件 `l` 类似于 win 的快捷方式
- 设备与设备文件（device）`b` 一般在 `/dev` 下 
	- 区块设备文件（储存数据，比如硬盘软盘设备）比如 `/dev/sda` 
	- 字符设备文件
- 数据接口文件（sockets）`s` 一般在 `/run` `/tmp`
- 数据输送档（FIFO, pipe）`p`
> Linux 系统中文件扩展名只是能够让用户了解文件的用途，能否执行要看10位的文件权限

# 5.3 Linux 目录配置
Filesystem Hierarchy Standard（FHS）（看5.3.1）
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241101184405.png)
对于目录树架构：
- / （root，根目录）：与开机系统有关
- /usr（unix software resource）：与软件安装/执行有关
- /var（variable）：与系统运行过程有关
