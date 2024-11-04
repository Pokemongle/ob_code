# 9.1 vi 与 vim
- 所有的 Unix Like 系统都会内置 vi
- 个别软件接口调用 vi
- vim 可以编辑程序，有字体颜色区分
- 简单快捷

# 9.2 vi 的使用
- 一般指令模式
	- 上下左右移动光标
	- 删除字符、整列
	- 复制粘贴
- 编辑模式
	- 按下 `ioar` 其中一个 进入编辑模式
	- Esc 退出
- 命令行命令模式
	- 按下 `:/?` 其中一个 进入命令行命令模式
	- Esc 退出
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104184927.png)


vimtutor
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104102523.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104102602.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104103049.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104110557.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104173130.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104174134.png)
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241104175408.png)
vimtutor 的总结
**移动**
	`hjkl` 对应←↓↑→
	`0` 移动到行开头
	`$` 移动到行末尾
	可以在前面加入 number 的：
	`w` 向后移动到词头
	`e` 向后移动到词尾
	大片移动的：
	`G` 移动到文本末尾
	`gg` 移动到文本开头
	`NUMBER+G` 移动到 `NUMBER` 行
		可以通过 `Ctrl+G` 和 `set nu` 辅助

---
**编辑**：
基本的 `i` 进入编辑模式，和普通的文本编辑器差不多
1. 插入
	`a` 在词末插入 `A` 在行末插入
	`p` 插入被删除/复制的文本
	`:r` 及其变种：
		`:r FILENAME` 插入 `FILENAME` 的内容
		`:r !command` 插入执行 command 会显示的内容
		注意和 normal mode 下的 `r` 区分
	`o` 上方插入一行
	`O` 下方插入一行
2. 替换
	`r` 光标处单个文本替换
	`c` 立即删除并替换 `ce` 删一个词 `c$` 删一行
	`s/old/new` 及其变种：
		`s/old/new/g` 替换一行
		`#, #s/old/new/g` 替换选中段落
		`%/s/old/new/g` 替换全文
		`%/s/old/new/gc` 替换前询问
3. 选中
	`v` 进入框选文本模式，可以使用移动类指令
	`y` 复制，配合 `v` 和 `p` 使用，也可以 `yw` 选词
4. 删除
	`x` 删除光标处的 char
	`dd` 删除一行
	`dw` 删除一个 word
5. 撤销
	`u` 撤销上一个操作
	`U` 撤销该行的操作
	`Ctrl+R` 撤销撤销
6. 查询
	`/` 向前查询
	`?` 向后查询
	`set ic/is/hls` 忽略大小写、不分搜索、高亮搜索
	`set noic/nois/nohls` 撤销上述设置

---
文件操作
`:q` 不保存退出
`:q!` 不保存强制退出
`:w` 写，相当于保存？
`:wq` 保存并退出
`!command` 暂时退出编辑器并执行 `command`
