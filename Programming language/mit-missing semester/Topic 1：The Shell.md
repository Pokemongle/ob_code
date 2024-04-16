execute command and pipe them together
# What is the shell?
* Interfaces
	* effects: used by users to *give computers commands*
		* voice
		* graphical
		* AR/VR
	* shortcuts:
		* cannot give a command that has not been programmed
	* shell:
		* textual interface
		* all platforms

# Using the shell
 *learn from examples*
* basic contents
	>`missing:~$`
	
	* `missing`: the machine name
	* `~`: current working directory
	* `$`: you are not the root user

* command
	> `missing:~$ date`
	> `Mon Jul 31 21:11:37 2023`
	
	* `date` is the command to show you the current date and time


	> `missing:~$ echo hello`
	> `hello`
	
	* `echo` prints out the arguments following it
	* `echo` split every word as an *argument* by whitespace:
		![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308022209428.png)
	> `missing:~$ echo $PATH`

	* `echo $PATH` lists which directories the shell should search for programs when it is given a command

	> `missing:~$ which argument`
	
	*  `which` can find out which file is executed for a given program name:
		![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308041219408.png)

# Navigating in the shell
* path
	* Description:
		* Linux, macOS, git bash: `/`
		* Windows: `\`
	* Classification:
		* **absolute path**
			* any path start with the root of the file system
		* **relative path**
			* relative to the current working directory
		* can see with the `pwd` command
			 ![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101245949.png)
			* can change with the `cd` command
				*  . refers to the current directory
				![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101248415.png)
				* .. refers to the parent directory
				![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101249833.png)	
* command
	* `ls`
		* see what lives in a directory
		![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101253753.png)
		* `ls [FILE]`
		![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101255642.png)
		* `ls [OPTION]`  
			* use `--help` or `man ls` to see what options can be used by the command
			![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101258434.png)
			* combination of `[OPTION]` and `[FILE]
			![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101304343.png)
			* the owner of the file -- the owning group -- everyone else
			*    `rwx`   `r-x`   `r-x`
			* **d** at the beginning of the line tells us that *mit* is a dir
			* **rwx** means that the users can **read write** and **execute** this file
			* **-** means that the given principal does not have the given permission


# Connecting Programs
rewire the input and output stream
* ` > file`  or ` < file`
	rewire: change the input and output stream direction of the shell
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308101416744.png)
	`>` will rewrite the file from the beginning
	`>>` will add info along the end of the file
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308182145188.png)

* `cat`
	`cat [FILE]` prints the content of the FILE to the terminal
	`cat < FILE1 > FILE2` write content in FILE1 into FILE2
	use `cat --help`  or `man cat` to see more

  * `echo`
	`echo TEXT` prints TEXT to the terminal

  * `tail`
	`tail -n+NUM` prints the last  `NUM` lines of the input
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308182225806.png)
	
  * **pipe character** `|` 
	take the output of the left as the input of the left
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308182229642.png)

# A versatile and powerful tool

`sudo`	: let you do something as super user  
	  
# Exercise
1. `echo $SHELL`: shows which shell you are using
2. `mkdir DIRECTORY`: create a new directory under current path
3. `man command` (for example `man touch`) shows the detailed information of the command
4. `touch FILE` : 
	1. update existed files' time
	2. create a new file if not existed
5. write something into a file in linux
	`#!/bin/sh`
	`curl --head --silent https://missing.csail.mit.edu`
	To remind you, the text above contains an ENTER.
	As we all know, **escape character** with 'n' stands for ENTER in computer language as: `\n` 
	Also, if you try to only write like this: `echo '#!/bin/sh\ncurl'`, what you'll get is `#!/bin/sh\ncurl`
	Use  `man echo`  to see detailed information:
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308171833447.png)
	seems like the SHORT-OPTION `-e` can help
	Thus, input `echo -e '#!/bin/sh\ncurl --head --silent https://missing.csail.mit.edu'`, you'll get the right answer
6. Why can't you execute the `semester` file I've just created?
	Use `ls -l FILENAME`, and you'll see:
		![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308171839985.png)
		`rw-` means the user have the rights to read and write the file except *execute* it
7. User authority
	first install `curl` command
	in order to execute the file, we use `sh semester`, it works
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308171859454.png)
	but `./semester` doesn't work
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308171901112.png)
	see https://en.wikipedia.org/wiki/Shebang_(Unix)
	
8. `chmod`: change permission settings for three kinds of users
	u: user
	g: group
	o: other
	+: add permission
	-: delete permission
    =:set permission
    file mode bits:
		r - 4
		w - 2
		x - 1
    format: `chmod u+rwx,g+rwx,o+rwx FILENAME`
    or: `chmod 777 FILENAME` = `chmod u+rwx,g+rwx,o+rwx FILENAME`
    ![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308171919408.png)
	![image.png](https://pokemongle-images-1319763739.cos.ap-nanjing.myqcloud.com/sandox/img/202308171920635.png)

	`chmod` see: https://en.wikipedia.org/wiki/Chmod
	
9. shebang, see: https://zh.wikipedia.org/zh-cn/Shebang
10. `grep` and `cut`
11. skip


