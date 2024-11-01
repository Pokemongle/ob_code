# 6.1 目录与路径
相对路径和绝对路径，学过就不赘述了，绝对路径的重要用途在第十五章

目录的相关操作
- cd
	- `cd -` 回到上一个工作目录
- pwd（printing working directory）
	- `pwd -P [FILE]` 显示真实路径而不是“快捷方式”
	- 
- mkdir
	- `mkdir -p [DIR]` 递归地创建文件夹 
		比如 `mkdir -p test1/test2`
	- `mkdir -m [MODE] [DIR]` 创建带权限的文件夹
- rmdir
	- 和 `mkdir` 一样也可以加 `-p`
	- 只能删除空的文件夹

可执行文件路径的变量：$PATH
- `echo $PATH` 可以查看当前路径
-  `PATH="${PATH}:/root"` 可以添加路径到 PATH，最好使用绝对路径增加安全性
# 6.2 文件与目录管理
- 检视 `ls` 与常用的范例
	- `-l` 显示包括权限、用户、修改时间的详细信息
	- `-a` 显示包括隐藏文件在内的所有文件
	- `ls -al ~` 列出主文件夹下包括属性和隐藏文件的所有文件
	- `ls -alF --color=never ~` 不显示颜色但是文件名末显示文件类型（对于纯文字 terminal 貌似比较友好，那个黑底深蓝字看得我...）
	- `ls -al --full-time ~` 完整呈现文件的修改时间
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411012146170.png)

- 复制 `cp`
	看常用的就好了
	注意是否将文件的权限也复制
	`-d` 复制快捷方式的快捷方式
	`-i` 询问是否覆盖
	`-p` 复制文件的权限
	`-r` 复制文件夹
	`-s` 复制一个快捷方式
	`-u` 有更新才复制
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411012151403.png)
