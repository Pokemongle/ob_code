# Variables
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504042213848.png)
![image.png](https://cdn.jsdelivr.net/gh/Pokemongle/img_bed_0@main/img/202504042215337.png)

## Declaring (Creating) Variables
```java
type variableName = value;
```
`String name = "John";`
`int myNum = 32;`

## Final variables
keyword `final` makes a variable ***unchangeable***
```java
final int myNum = 15;
myNum = 20; // will cause an error
```

---

# Print Variables
## Display Variables 
- use `println`
	- can use `+` to combine String
```java
String name = "John";
System.out.println("Hello " + name);
```

---

# Java Declare Multiple Variables 
## Declare Many Variables 
- multiple variables of the ***same type***
	`int x = 5, y = 6, z = 50;`

## One Value to Multiple Variables 
```java
int x, y, z; // Firstly declare the variables 
x = y = z = 50; // Then assign the value
```

---

# Java Identifiers
就是变量名
## Identifiers
- descriptive identifiers are recommended
```java
// Good
int minutesPerHour = 60;

// OK, but not so easy to understand what m actually is
int m = 60;
```
general rules:
- Names can contain letters, digits, underscores, and dollar signs `$`
- Names must begin with a letter
- Names should start with a lowercase letter, and cannot contain whitespace
- Names can also begin with $ and _
- Names are case-sensitive ("myVar" and "myvar" are different variables)
- Reserved words (like Java keywords, such as `int` or `boolean`) ***cannot*** be used as names (it is ok in python)

---

# Java Variables - examples
```java
// Student data
String studentName = "John Doe";
int studentID = 15;
int studentAge = 23;
float studentFee = 75.25f; // the f is not compulsory
char studentGrade = 'B';

// Print variables
System.out.println("Student name: " + studentName);
System.out.println("Student id: " + studentID);
System.out.println("Student age: " + studentAge);
System.out.println("Student fee: " + studentFee);
System.out.println("Student grade: " + studentGrade);
```

## Calculate the Area of a Rectangle
```java
// Create integer variables
int length = 4;
int width = 6;
int area;

// Calculate the area of a rectangle
area = length * width;

// Print variables
System.out.println("Length is: " + length);
System.out.println("Width is: " + width);
System.out.println("Area of the rectangle is: " + area);
```