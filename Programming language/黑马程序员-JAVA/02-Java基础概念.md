# 注释
`// 单行注释`
`/* 多行注释 */`
`/** 文档注释 */`
注释的内容不参加编译也不参加运行
不要嵌套

# 关键字
* 关键字的字母全部小写
* `class` - 定义和注释类

# 字面量

* Java的字面量类型
	* 整数
	* 小数
	* 字符串（双引号括起来）
	* 字符（单引号，只有一个内容）
	* 布尔类型（true，false）
	* 空类型（值是null）
```java
public class ValueDemo1 {  
    public static void main(String[] args) {  
        // integer  
        System.out.println(666);  
        System.out.println(13.14);  
        System.out.println("panda");  
        System.out.println('A');  
        System.out.println(true);  
        // null不能直接打印  
        System.out.println("null");  
    }  
}
```
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231851611.png)

* `\t`**制表符**
	* 在打印的时候把**前面的**字符串长度补到8或8的倍数，最少补1个空格，最多补8个空格

` \t 会和前一个字符串进行匹配`

```java
public class ValueDemo2 {  
    public static void main(String[] args){  
        // 不使用制表符  
        System.out.println("name" + "ages");  
        System.out.println("tom" + "23");  
        // 在第一列数据后均使用制表符  
        System.out.println("name" + "\tage");  
        System.out.println("tom" + "\t23");  
    }  
}
```
![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202309231849006.png)

# 变量

* 变量的定义格式
	* `数据类型 变量名 = 数据值`
	* `double height = 1.93`
	* `int chance = 2`
	* 变量的名字不能重复 
		`int a = 10; int a = 10;`会报错
	* 变量使用之前要赋值
		`int g;` 可能会报错
		
* 变量的使用方式
	* 输出打印
		`int a = 10; System.out.println(a);`
	* 参与计算
		`int a = 10, b = 10; System.out.println(a + b);`
	* 修改记录的值
		`int a = 10; System.out.println(a); a = 20; System.out.println(a);`
		