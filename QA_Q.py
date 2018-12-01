#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from time import sleep
import sys
import os
from subprocess import *

# 202 Software Testing Interview Questions and Answers

QUESTION_DICT= {
	1: {'What is a Bug?': """
When actual result deviates from the expected result while testing a software application or product
then it results into a defect. Hence, any deviation from the specification mentioned in the product
functional specification document is a defect. In different organizations it's called a Bug."""
	},
	2: {'What is a Defect?':"""
If software misses some feature or function from what is there in requirement it is called as defect."""
	},
	3: {'What is CMM?':"""
The Capability Maturity Model for Software (CMM or SW-CMM) is a model for judging the maturity of
the software processes of an organization and for identifying the key practices that are required to
increase the maturity of these processes."""
	}
}

# print('{}\n{}'.format(QUESTION_DICT[1].keys()[0], QUESTION_DICT[1].values()[0]))
# Create a list of questions.
question_list = QUESTION_DICT.keys()
if not question_list:
	sys.exit(1)

# Randomize the list of questions.
random.shuffle(question_list)

# Define number of asked questions.
q_count = 5
try:
    ask_q_list = question_list[:q_count]
except ValueError as e:
    print('Invalid number of questions.')
    sys.exit(1)
    

for q in ask_q_list:
	# Ask questions.
	print(QUESTION_DICT[q].keys()[0])
	# Show answers.
	print(QUESTION_DICT[q].values()[0])
	print('---')


