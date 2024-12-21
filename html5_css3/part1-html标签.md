# 前言
## 网页的相关概念
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412051209734.png)

## 常用浏览器与内核
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412051213846.png)
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412051212734.png)
## Web 标准
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412051221145.png)




# 01
## html 语法规范
- 一般成对出现、用尖括号
	`<html> </html>`
	也有单个的标签 `<br \>`
- 并列关系、包含关系

vscode 快捷键
	ctrl+alt+箭头，添加多个光标
	shift+alt+箭头，复制行
	ctrl+d，选中多个
	ctrl+g，定位到某行
	shift+alt+鼠标拖动，选中区块
	
## html 基本结构标签
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412051249213.png)

## 网页开发工具
`<!DOCTYPE html>` 文档类型声明标签
`<html lang="en"/"zh-CN/fr">`
`<meta charset="UTF-8">` 在 `<head>` 标签内

## html 常用标签
标签语义：理解标签的含义
- 标题标签`<h1>-<h6>`
- 段落标签 `<p>`
	- 根据浏览器大小换行
	- 段落之间有空行
- 换行标签 `<br />`
	- ***单标签***
	- 简单换行，没有空隙
- 文本格式化标签
	- 加粗 `<strong>` 或者 `<b>`
	- 倾斜 `<em>` 或者 `<i>`
	- 删除线 `<del>` 或者 `<s>`
	- 下划线 `<ins>` 或者 `<u>`
- `<div>` 和 `<span>` 没有语义，盒子
- **图像标签** `<img src="path">` 用空格分开各个属性
	- `src` 图片路径
	- `title` 鼠标悬停时显示的文本
	- `alt` 图片无法显示时用文本替代
	- `width` 宽度
	- `height` 高度
	- `border` 设置图片边框
- **超链接标签** `<a href="url">文本或图像等网页元素</a>`
	- `href="url"` 链接
		- 外部链接 `http://`
		- 内部链接同一个文件夹中的
		- ***空链接*** `href="#"`
		- ***下载链接*** `href=".exe或.zip"`
		- ***锚点链接*** `href="#two"` 井号后面接标签
			- 目标位置可以添加标签属性 `<h3 id="two">`
	- `target` 窗口弹出方式
		- `_self` 为默认值
		- `_blank` 为在新窗口中打开方式
- 注释标签 `<!-- content -->`
- 特殊字符
	- `&` 开头 `;` 结尾
	![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202412061236288.png)
