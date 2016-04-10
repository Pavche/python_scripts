def censor(text, word):
    # Replace bad with "*" * len(word)
    list_text = text.split(" ")
    # loop through all elements of list_text
    for i in range(0, len(list_text)):
	if list_text[i].lower() == word.lower():
	    list_text[i] = "*" * len(word)
    # Returns the result
    return " ".join(list_text)
    
print censor("This sentence contains a bad word", "bad")