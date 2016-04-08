def product(list_int):
    result = 1
    for elem in list_int:
	result *= int(elem)
    return result

print product([5,5,5])