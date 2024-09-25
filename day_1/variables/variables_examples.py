number_value= 10
decimal_value= 10.0
string_value= 'Raiyan'

# the memory address before change
print(id(decimal_value))
# print all the variables
print(number_value,decimal_value,string_value)
# the memory address after change
decimal_value= 'ten'
print(id(decimal_value))


print("Write something,I'm gonna copy you")
x = input()
print(x + "-nya")