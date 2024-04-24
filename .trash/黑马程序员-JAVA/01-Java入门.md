# 1. CMD
## 人机交互小故事
xerox创造了图形化界面

缺点：
- 消耗内存
- 运行速度慢

## 打开CMD
`win+R`，输入`cmd

## 常用CMD命令

`盘符名称+冒号 `切换到盘
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231509599.png)

`dir`查看当前路径下的内容，可以显示隐藏的文件
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231510077.png)

`cd` 进入单级目录
`cd ..` 回退到上一级目录
`cd \` 回退到根目录
`cd dir1\dir2\...` 进入多级目录
`Ctrl+Alt+鼠标滚轮`缩放界面
`cls` 清屏
`exit` 退出CMD

## 用cmd打开QQ
方法1：
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231518427.png)
**方法2：环境变量**
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231520834.png)
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231613021.png)

___

# 2. Java基础学习


## Hello world 经典程序

用记事本编写程序
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231608459.png)

编译
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231606277.png)
`javac` 是JDK提供的编译工具，将java文件编译成class文件

运行
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231606409.png)
`java` 是JDK提供的运行代码的工具，运行的时候文件不加后缀

## Java环境变量
创建 JAVA_HOME包括java.exe的bin路径，删掉bin，
在path中加入一行%JAVA_HOME%

## JRE和JDK

1. JDK是java开发工具包
	1. JVM-java虚拟机：java程序运行的地方
	2. 核心类库：java已经写好的东西，可以直接用
	3. 开发工具：javac编译，java运行，jdb调试，jhat内存分析工具
2. JRE(Java Runtime Environment)
	1. java运行环境
	2. JVM，核心类库，运行工具
3. JDK, JRE, JVM的包含关系
	`JDK > JRE > JVM`




