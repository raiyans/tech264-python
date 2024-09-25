# False: A string is False only if it is an empty string ("").
# True: Any non-empty string (including spaces or special characters) evaluates to True.

non_empty_string = "Hello"
print(bool(non_empty_string))  # Output: True

# Even a single space will evaluate to True
single_space = " "
print(bool(single_space))  # Output: True