#!/usr/bin/python3

import re

# Passing a string value representing your regular expression to re.compile()
# returns a Regex pattern object (or simply, a Regex object).
# To create a Regex object that matches the phone number pattern, enter
# the following into the interactive shell. (Remember that \d means “a digit
# character” and \d\d\d-\d\d\d-\d\d\d\d is the regular expression for the cor-
# rect phone number pattern.)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is 415-555-4242.')
print('Phone number found: ' + mo.group())
