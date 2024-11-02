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
	考虑：
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411012201107.png)
	`-a` 是 `-dr` 的综合，无论是快捷方式、文件夹还是文件以及复制属性
	`-d` 复制快捷方式的快捷方式以及属性
	`-i` 询问是否覆盖
	`-p` 复制文件的属性
	`-r` 复制文件夹
	`-s` 复制一个快捷方式
	`-u` 有更新才复制
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411012151403.png)

- 移除文件或目录 `rm`
	`-f` 强制删除
	`-i` 询问是否删除
	`-r` 递归删除文件夹
	- root 用户删除文件默认会一直询问，使用 `\rm` 来规避询问
	- 可以使用通配符 `*` 删除
	- 删除开头为 `-` 的文件系统会误判为 option，加上 `./` 就可以删除

- 移动文件或目录或**更名** `mv`
	copy 的阉割版
	`-f` 强制移动
	`-i` 询问是否移动
	`-r` 递归移动文件夹


# 6.3 文件内容查阅
直接查阅文件内容
`cat`（concatenate）
	主要使用 `-A -n -b`
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411012230038.png)

`tac` 是 `cat` 反过来，从最后一行开始显示

`nl` 添加行号打印
	与 `cat -n` 的区别主要在于可以设计行号打印格式

---
可翻页检视
`more`
	和 info 一样除了可以用 vim 的上下控制还可以用 `/` 输入命令

`less`
	和 `more` 相比可以向上翻阅和用 `?` 向上查询
	`man` 就是调用 `less` 实现的

---
数据撷取
`head [-n NUMBER]`：提取文件前 `NUMBER` 行，默认10行
	如果 `NUMBER` 是负数，表示不列出后 NUMBER 行

`tail [-n NUMBER]`：提取文件后 `NUMBER` 行
	`+NUMBER` 表示列出 `NUMBER` 行后的数据

组合使用：
	`head -n 20 /etc/man_db.conf | tail -n 10` 11-20行
	`cat -n /etc/man_db.conf | head -n 20 | tail -n 10` 11-20行并列出行数
	使用**管线** `|`

---
非纯文本文件读取
`od [-t TYPE] [FILE]`
	`od -t oCc FILE`
	综合应用 `echo password | od -t oCc echo`
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411012312501.png)

---
修改文件时间或创建新文件
文件的三个时间
	`modification time（mtime）` 指文件内容数据被修改的时间
	`status time（ctime）` 指文件属性、权限被修改的时间
	`access time（atime）` 文件内容被取用（比如被 `cat` 取用）的时间
	用于 `ls -l --time=ctime/atime` 默认是 `mtime`

`touch`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411012313812.png)

>可以用分号 `;` 一次执行多个指令


# 6.4 文件与目录的默认权限与隐藏权限
e.g.1 `root` 把文件 `~/.bashrc` 复制给 `user1`
1. 因为怕覆盖 `user1` 原有的文件，可以复制为 `cp ~/.bashrc ~user1/bashrc`
2. 修改属性 `chown user1:user1 ~user1/bashrc`

e.g.2 修改权限 `chmod -R 755 /tmp/chapter6_1`

---
文件默认权限 `umask`
	`umask` 是指在默认的权限上减掉多少权限
	文件默认权限为666，因为一般的文件不需要执行；文件夹默认权限为777
	`umask` 一般用户默认为002，即 others 在文件权限默认 `rw` 的情况下去掉 `w`；`root` 用户默认为022
	`umask` 的设置直接在后面加3位数e.g.`umask 002`

---
文件隐藏属性

修改隐藏属性
`chattr [+-=][aAcCdDeFijmPsStTux] [FILE]`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411021154738.png)
	常用 
	`a` 只能写入
	`i` 不能被删除、改名、写入

查看隐藏属性
`lsattr`
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202411021159091.png)

---
文件特殊权限 SUID, SGID, SBIT
`SUID`: s 出现在 user 的 x 上
看不懂，先别管了

---
观察文件类型 
`file [FILE]`

# 6.5 指令与文件的搜寻
指令文件名的搜寻
`which [-a] [FILENAME]`
	可以找到完整的指令路径
	仅限在 PATH 路径当中包含的指令

文件文件名的搜寻
`whereis [option] [FILE]`
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102141050.png)

`locate [option] keyword` 
	在数据库中输入文件名的一部分进行查找，找不到可先 `updatedb`
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102141242.png)

`find [PATH] [option] [action]`
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102144204.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102144150.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102144317.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102144544.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102145016.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102145159.png)

![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102150739.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102150807.png)


