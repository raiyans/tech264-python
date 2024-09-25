### Explain and demonstrate: Numeric data types: int and float
int is for whole numbers (like 10, -5).
float is for numbers with decimals (like 3.14, -0.5).


### Explain and demonstrate: Boolean data type
The bool data type represents truth values: True or False

### Explain why the result is not 0.9999999... with this code and what lesson we should learn:
```
One_third = 1 / 3
print(One_third)

# Python should show 0.3333333333333333

print(One_third * 3)

# python rounds it to 1.0
```

 cannot represent all real numbers with complete precision because of the way floating-point numbers are stored in memory.