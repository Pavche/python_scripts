def remove_duplicates(list_of_items):
    new_list = []
    for item in list_of_items:
	for elem in new_list:
	    # is this item present in new_list
	    if elem == item:
		break
	else:
	    new_list.append(item)
    result = new_list
    return result

print remove_duplicates(['a','b','c','a','b','c'])