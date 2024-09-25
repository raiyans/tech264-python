"""
Initialise x with the value of 0
Create a while statement so that it loops while x is less than 10. Everytime it loops it should:
Print the value of x to the screen in an f-string
Increment (add 1 to x)
Running this code should produce:

```

print x -> 0

print x -> 1

print x -> 2

print x -> 3

print x -> 4

print x -> 5

print x -> 6

print x -> 7

print x -> 8

print x -> 9

```

Once your code works, find out what happens when you run the code if you comment out the first line which initialises 'x'.
Write a brief comment on the line before the code which increments x to explain what would happen if you don't increment x.
Copy and paste your working 'while loop' underneath the 'while loop'. Modify the second copy of the 'while loop' so that it breaks out of the loop when x equals 4.
The output should be:

```

print x -> 0

print x -> 1

print x -> 2

print x -> 3

print x -> 4

``` """
counter = 0
while counter < 10:
    print(f"print {counter} -> 0")
    counter+=1

# If you comment out the counter = 0 initialization, you'll get a NameError because x will not be defined when the loop starts.

counter = 0
while counter < 10:
    print(f"print {counter} -> 0")
    if counter == 4:
        break
    counter += 1
