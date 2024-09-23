# Python variable basics

### What is a Variable in Python?
It acts like a container that holds data, such as numbers, strings, or more complex types, that you can refer to later in your code. You can assign a value to a variable using the = operator. 
 
### Why is it Called a Variable?
It is called a "variable" because the value it holds can change or "vary" throughout the execution of the program.

### Dynamically Typed Language (Python) vs Statically typed:
In a dynamically typed language, you don’t have to declare the type of a variable when you create it. The type is determined automatically at runtime based on the value assigned.
A strongly typed language enforces strict rules about type. You cannot easily mix types without explicitly converting them. they are often compiled at runtime.
 example:
```python
x= 'raiyan'
x= 10
# you successfully changed the variable
```
```java
int x= 10;
x = "hello";

// You will get an error in java
```

### Why does the id() of the variable change?
The id() returns the objects memory address and will be different each time run. while changing a variable in runtime the variable will take a new address in memory