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
