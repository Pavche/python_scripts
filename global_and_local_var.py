#!/usr/bin/python

global_var = 12

def func():
    local_var = 100
    print(global_var)
    
func()

xy = 100

def func2():
    xy = 200
    print(xy)
    
func2()