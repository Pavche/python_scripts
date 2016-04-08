def count(sequence, item):
    result = 0
    for elem in sequence:
	if elem	== item:
	    result += 1
    return result

print count(['one','two','three',1,2,3,'one','two'],"three")