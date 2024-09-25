"""Summary

Print incremented numbers to the screen but substitute multiples of 3 with 'Fizz', multiples of 5 with 'Buzz', and multiples of both with 'FizzBuzz'
Rationale:Great to consolidate control flow topic.
The task

Core:

Make a new 'fizzbuzz.py' file
Write a program that prints the numbers from 1 to 100.
For multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz" instead of the number
For numbers which are multiples of both three and five print "FizzBuzz".
If time:

Improve the script so we can decide which numbers to substitute for "Fizz" and "Buzz"
Refactor using functions

Acceptance Criteria

All core task are done
Core works with no error
"""
for num in range(1, 101):
    # Check if number is a multiple of both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Check if number is a multiple of 3
    elif num % 3 == 0:
        print("Fizz")
    # Check if number is a multiple of 5
    elif num % 5 == 0:
        print("Buzz")
    # If none of the conditions match, print the number
    else:
        print(num)
