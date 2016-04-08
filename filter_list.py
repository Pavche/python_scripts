def purify(list_num):
    new_list_num = []
    for elem in list_num:
	if elem % 2 == 0:
	    new_list_num.append(elem)
    return new_list_num

print purify([1,2,3,4,5,6,7,8,9,10,11,12])
    