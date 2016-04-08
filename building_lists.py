# Demonstrating list comprehension in Python which is specific for the language
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,12) if(x**2) % 2 == 0]

cubes_by_four = [x**3 for x in range(1,12) if(x**3) % 4 == 0]

print even_squares
print cubes_by_four


# List Slicing
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print my_list[::2]
    
backwards = my_list[::-1]
print backwards

to_one_hundred = range(101)

# Add your code below!
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

print middle_third

# Lambdas
