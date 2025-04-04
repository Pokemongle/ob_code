# Java Data Types  
Primitive data types: byte, short, int, long, float, double, boolean, char
Non-primitive data types: String, Arrays, Classes etc.

## Primitive Data Types 
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504042234882.png)

---
# Java Numbers 
## Numbers 
Integer types: byte short int long
Floating point types: float double 

## Integer Types 
### Byte 
```java
byte myNum = 100; // signed number, 1byte, 8bits
System.out.println(myNum);
```

### Short 
```java
short myNum = 5000; // signed short, 2byte, 16bits
System.out.println(myNum);
```

### Int 
```java
int myNum = 100000; // signed int, 4byte, 32bits
System.out.println(myNum);
```

### Long
```java
// need the L at the end
long myNum = 15000000000L; // signed long, 8byte, 64bits
System.out.println(myNum);
```

## Floating Point Types 
```java
float myNum = 5.75f; // add f
System.out.println(myNum);
```

```java
double myNum = 19.99d; // add d
System.out.println(myNum);
```

## Scientific Numbers 
```java
float f1 = 35e3f;
double d1 = 12E4d;
System.out.println(f1);
System.out.println(d1);
```

---
# Java Boolean Data Types 
## Boolean Types 
```java
boolean isJavaFun = true;
boolean isFishTasty = false;
System.out.println(isJavaFun);     // Outputs true
System.out.println(isFishTasty);   // Outputs false
```
- boolean values 
	- true or false (not the same as python)

---
# Java Characters 
## Characters 
- a single character (***or its ASCII value***)
- surrounded by single quotes 
```java
char myGrade = 'B';
System.out.println(myGrade);
```

```java
char myVar1 = 65, myVar2 = 66, myVar3 = 67;
System.out.println(myVar1); // A
System.out.println(myVar2); // B
System.out.println(myVar3); // C
```

## Strings 
- surrounded by double quotes
```java
String greeting = "Hello World";
System.out.println(greeting);
```

---
# Java Data Types Example 
## Real-Life Example 
```java
// Create variables of different data types
int items = 50;
float costPerItem = 9.99f;
float totalCost = items * costPerItem;
char currency = '$';

// Print variables
System.out.println("Number of items: " + items);
System.out.println("Cost per item: " + costPerItem + currency);
System.out.println("Total cost = " + totalCost + currency);
```

---
# Java Non-Primitive Data Types
## Non-Primitive Data Types
Non-primitive data types are called **reference types** because they refer to objects.

The main differences between **primitive** and **non-primitive** data types are:

- Primitive types in Java are predefined and built into the language, while non-primitive types are created by the programmer (except for `String`).
- Non-primitive types can be used to call methods to perform certain operations, whereas primitive types cannot.
- Primitive types start with a lowercase letter (like `int`), while non-primitive types typically starts with an uppercase letter (like `String`).
- Primitive types always hold a value, whereas non-primitive types can be `null`.