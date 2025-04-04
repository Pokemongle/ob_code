# Java Conditions and If Statements
the same as C
## if 
```java
if (20 > 18) {
  System.out.println("20 is greater than 18");
}
```

# Java Else
```java
int time = 20;
if (time < 18) {
  System.out.println("Good day.");
} else {
  System.out.println("Good evening.");
}
// Outputs "Good evening."
```

# Java Else If
```java
int time = 22;
if (time < 10) {
  System.out.println("Good morning.");
} else if (time < 18) {
  System.out.println("Good day.");
} else {
  System.out.println("Good evening.");
}
// Outputs "Good evening."
```

# Java Short Hand If...Else (Ternary Operator)

```java
variable = (condition) ? expressionTrue :  expressionFalse;
```

```java
int time = 20;
String result = (time < 18) ? "Good day." : "Good evening.";
System.out.println(result);
```