## Modifiers
```java
public class Main
```
The `public` keyword is an **access modifier**, meaning that it is used to set the access level for classes, attributes, methods and constructors.

We divide modifiers into two groups:

- **Access Modifiers** - controls the access level
- **Non-Access Modifiers** - do not control access level, but provides other functionality
## ***Access Modifiers***
For **classes**, you can use either `public` or _default_:

|           |                                                                                                                                                                                                                             |                                                                                 |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `public`  | The class is accessible by any other class                                                                                                                                                                                  | [Try it »](https://www.w3schools.com/java/tryjava.asp?filename=demo_mod_public) |
| _default_ | The class is only accessible by classes in the same package. This is used when you don't specify a modifier. You will learn more about packages in the [Packages chapter](https://www.w3schools.com/java/java_packages.asp) |                                                                                 |
For **attributes, methods and constructors**, you can use the one of the following:
For **attributes, methods and constructors**, you can use the one of the following:

| Modifier    | Description                                                                                                                                                                                                     | Try it                                                                                                              |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `public`    | The code is accessible for all classes                                                                                                                                                                          | [Try it »](https://www.w3schools.com/java/tryjava_multi.asp?filename=demo_mod_public2&multi=demo_mod_public2_multi) |
| `private`   | The code is only accessible within the declared class                                                                                                                                                           | [Try it »](https://www.w3schools.com/java/tryjava.asp?filename=demo_access_mod)                                     |
| _default_   | The code is only accessible in the same package. This is used when you don't specify a modifier. You will learn more about packages in the [Packages chapter](https://www.w3schools.com/java/java_packages.asp) | [Try it »](https://www.w3schools.com/java/tryjava.asp?filename=demo_mod_default2)                                   |
| `protected` | The code is accessible in the same package and **subclasses**. You will learn more about subclasses and superclasses in the [Inheritance chapter](https://www.w3schools.com/java/java_inheritance.asp)          | [Try it »](https://www.w3schools.com/java/tryjava.asp?filename=demo_mod_protected)                                  |

---
## Non-Access Modifiers
For **classes**, you can use either `final` or `abstract`:

| Modifier   | Description                                                                                                                                                                                                                                                                                                                     | Try it                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `final`    | The class cannot be inherited by other classes (You will learn more about inheritance in the [Inheritance chapter](https://www.w3schools.com/java/java_inheritance.asp))                                                                                                                                                        | [Try it »](https://www.w3schools.com/java/tryjava.asp?filename=demo_inherit_final)                                    |
| `abstract` | The class cannot be used to create objects (To access an abstract class, it must be inherited from another class. You will learn more about inheritance and abstraction in the [Inheritance](https://www.w3schools.com/java/java_inheritance.asp) and [Abstraction](https://www.w3schools.com/java/java_abstract.asp) chapters) | [Try it »](https://www.w3schools.com/java/tryjava_multi.asp?filename=demo_mod_abstract&multi=demo_mod_abstract_multi) |


For **attributes and methods**, you can use the one of the following:

| Modifier       | Description                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `final`        | Attributes and methods cannot be overridden/modified                                                                                                                                                                                                                                                                                                                                                               |
| `static`       | Attributes and methods belongs to the class, rather than an object                                                                                                                                                                                                                                                                                                                                                 |
| `abstract`     | Can only be used in an abstract class, and can only be used on methods. The method does not have a body, for example **abstract void run();**. The body is provided by the subclass (inherited from). You will learn more about inheritance and abstraction in the [Inheritance](https://www.w3schools.com/java/java_inheritance.asp) and [Abstraction](https://www.w3schools.com/java/java_abstract.asp) chapters |
| `transient`    | Attributes and methods are skipped when serializing the object containing them                                                                                                                                                                                                                                                                                                                                     |
| `synchronized` | Methods can only be accessed by one thread at a time                                                                                                                                                                                                                                                                                                                                                               |
| `volatile`     | The value of an attribute is not cached thread-locally, and is always read from the "main memory"                                                                                                                                                                                                                                                                                                                  |
