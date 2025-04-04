# Java Arrays
```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
```
```java
int[] myNum = {10, 20, 30, 40};
```

## Access the Elements of an Array
```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
System.out.println(cars[0]);
// Outputs Volvo
```

## Array Length
```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
System.out.println(cars.length);
// Outputs 4
```
---
# Java Arrays Loop
```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (int i = 0; i < cars.length; i++) {
  System.out.println(cars[i]);
}
```
```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (String i : cars) {
  System.out.println(i);
}
```

---
# Java Multi-Dimensional Arrays
```java
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
```
```java
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
System.out.println(myNumbers[1][2]); // Outputs 7
```
```java
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
for (int[] row : myNumbers) {
  for (int i : row) {
    System.out.println(i);
  
```
