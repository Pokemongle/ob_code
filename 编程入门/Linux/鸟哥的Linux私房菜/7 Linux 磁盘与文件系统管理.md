# 7.1 认识 Linux 文件系统
索引式文件系统
	superblock 记录文件系统的整体信息，包括 inode/block 的总量、使用量、剩余量以及文件系统的格式与相关信息
	inode 记录文件的属性和文件数据所在的 block 的号码，一个文件一个 inode
	block 实际记录文件的内容，一个文件可能有多个 block
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102170331.png)

FAT 格式的文件系统（U 盘闪存）
没有 inode，每个 block 的号码记录在前一个 block 中
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102170426.png)

---
Linux 是 Ext2 索引式文件系统，一般不需要磁盘重组（现在又兼容 XFS 系统了）
Linux 的索引式文件系统中 inode 和 block 不是全部放在一起管理的而是分群组
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102170849.png)
`Boot Sector` 开机扇区，安装开机管理程序
每个 Block group 中：
`Data Block` 数据区块
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102171056.png)
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102171242.png)
`inode table`
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102171714.png)
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102171730.png)

VFS (Virtual Filesystem Switch) 的作用
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102180704.png)

---
# 7.2 文件系统的简单操作
`df` 和 `du` 感觉用不上，之后再说吧

创建目录时，分配一个 inode 和至少一块 block 给该目录，目录的 block 如下：
![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102183859.png)

实体链接与符号链接 `ln`
	使用：加-s 就是符号链接，不加就是实体链接
	1. 实体链接 Hard Link（硬式链接或实际链接）
	由于：
		每个文件都占用一个 inode，文件内容由 inode 指向
		读取文件必须经过目录记录的文件名指向对应的 inode
	所以创建 hard link 实际上是：
		在某个目录下新增一个文件名链接到某个 inode 号码，文件名不一定相同
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102184435.png)
	不能做目录的 hard link
	2. 符号链接 Symbolic Link（捷径）
	![image.png](https://raw.githubusercontent.com/Pokemongle/img_bed_0/main/img/20241102190714.png)
	对符号链接进行修改会修改原本的文件

---
# 7.3 磁盘的分区、格式化、检验与挂载
`lsblk`（list block device）列出系统上的所有磁盘列表
`blkid` 列出设备的 UUID 等参数
`parted device_name print` 查看磁盘分区信息

GPT 分区表用 `gdisk` 分区
MBR 分区表用 `fdisk` 分区
