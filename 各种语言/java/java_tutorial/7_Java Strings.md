# Java Strings 
[more String methods](https://www.w3schools.com/java/java_ref_string.asp)

## Java Strings
```java
String greeting = "Hello"; // double quotes
```
## String Length
```java
String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
System.out.println("The length of the txt string is: " + txt.length());
```
## More String Methods
```java
String txt = "Hello World";
System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
System.out.println(txt.toLowerCase());   // Outputs "hello world"
```
## Finding a Character in a String
```java
String txt = "Please locate where 'locate' occurs!";
System.out.println(txt.indexOf("locate")); // Outputs 7
```

---
# Java String Concatenation
## String Concatenation
- use `+`
```java
String firstName = "John";
String lastName = "Doe";
System.out.println(firstName + " " + lastName);
```
- use `.concat(new_string)`
```java
String firstName = "John ";
String lastName = "Doe";
System.out.println(firstName.concat(lastName));
```
---
# Java Numbers and Strings
## Adding Numbers and Strings
can use `+`
```java
String x = "10";
int y = 20;
String z = x + y;  // z will be 1020 (a String)
```

---
# Java Special Characters
## Strings - Special Characters
escape character `\`
```java
String txt = "We are the so-called "Vikings" from the north."; // will cause error
```
```java
String txt = "We are the so-called \"Vikings\" from the north."; // added escape character \\
```

![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504042318883.png)
