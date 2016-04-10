def median(input_list):
    # Sort the list
    new_list = sorted(input_list)
    L = len(new_list)
    
    # Does the list have odd num of elements?
    if L % 2 != 0:
	# Return the middle element
	result = new_list[int(L / 2)]
    else:
	# Return the average of the two middle elements
	a = new_list[int(L / 2)-1]
	b = new_list[int(L / 2)]
	result = (a + b) / float(2)
    return result

print median([1,2,3,4])